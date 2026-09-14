## 01_load.R -- read the dataset and construct the derived matrices.
## Sourced by the other scripts. No side effects other than objects in memory.

read_di <- function(f) utils::read.csv(file.path("data", f), stringsAsFactors = FALSE,
                                       na.strings = c("NA", ""), encoding = "UTF-8")

## The register includes firms that no longer operate, so that consolidation and
## failure are visible rather than silently dropped. Every coverage and gap table
## in this repository describes the CURRENT industry and therefore uses operating
## firms only. `companies_all` retains the full set for the historical section.
companies_all <- read_di("companies.csv")
companies_all$operating <- companies_all$status %in% c("active", "acquired_active")
companies <- companies_all[companies_all$operating, ]
regions   <- read_di("regions.csv")
segments  <- read_di("segments.csv")
domains   <- read_di("domains.csv")
modalities<- read_di("modalities.csv")
spatial   <- read_di("coverage_spatial.csv")

REGION_CODES <- regions$region_code
DOMAIN_CODES <- domains$domain_code

## Spatial coverage as a numeric matrix: firms x regions, ordinal 0-3.
spatial_mat <- as.matrix(spatial[, REGION_CODES])
rownames(spatial_mat) <- spatial$company_id
storage.mode(spatial_mat) <- "integer"

## Substantive coverage as a binary matrix: firms x domains.
## A firm counts as covering a domain if it appears in either the primary or
## secondary domain list. Primary membership is retained separately as weight 2.
split_domains <- function(x) {
  if (is.na(x)) return(character(0))
  trimws(unlist(strsplit(x, "|", fixed = TRUE)))
}
domain_mat <- matrix(0L, nrow = nrow(companies), ncol = length(DOMAIN_CODES),
                     dimnames = list(companies$company_id, DOMAIN_CODES))
for (i in seq_len(nrow(companies))) {
  p <- split_domains(companies$domains_primary[i])
  s <- split_domains(companies$domains_secondary[i])
  domain_mat[i, p] <- 2L
  domain_mat[i, setdiff(s, p)] <- 1L
}

stopifnot(all(companies$company_id %in% rownames(spatial_mat)))
spatial_mat_all <- spatial_mat
spatial_mat <- spatial_mat[companies$company_id, , drop = FALSE]

## Long-format versions for export and for anyone who prefers tidy data.
spatial_long <- data.frame(
  company_id = rep(companies$company_id, times = length(REGION_CODES)),
  region_code = rep(REGION_CODES, each = nrow(companies)),
  coverage = as.vector(spatial_mat),
  stringsAsFactors = FALSE)

domain_long <- data.frame(
  company_id = rep(companies$company_id, times = length(DOMAIN_CODES)),
  domain_code = rep(DOMAIN_CODES, each = nrow(companies)),
  weight = as.vector(domain_mat),
  stringsAsFactors = FALSE)

message(sprintf("loaded %d companies (%d operating, %d exited) | %d regions | %d domains",
                nrow(companies_all), nrow(companies),
                nrow(companies_all) - nrow(companies),
                length(REGION_CODES), length(DOMAIN_CODES)))

## ---- country layer ---------------------------------------------------------
countries <- read_di("countries.csv")
ccov_all  <- read_di("coverage_country.csv")
ccov      <- ccov_all[ccov_all$company_id %in% companies$company_id, ]

countries$income_group    <- factor(countries$income_group, c("LIC","LMIC","UMIC","HIC"))
countries$population_band <- factor(countries$population_band, c("XS","S","M","L","XL"))
countries$internet_band   <- factor(countries$internet_band, c("low","medium","high"))

## Provider counts per country, on the same coverage>=2 threshold used for regions.
ccov_sub <- ccov[ccov$coverage >= 2, ]
cmp <- companies[, c("company_id","human_subjects","microdata_access","maturity_class",
                     "segment_primary","ownership_type")]
ccov_j <- merge(ccov_sub, cmp, by = "company_id")

tally <- function(sub) {
  t <- table(factor(sub$iso3, levels = countries$iso3))
  as.integer(t)
}
countries$n_providers    <- tally(ccov_j)
countries$n_primary      <- tally(ccov_j[ccov_j$human_subjects == "direct", ])
countries$n_accessible   <- tally(ccov_j[ccov_j$microdata_access %in%
                                           c("open","researcher_restricted"), ])
countries$n_any          <- tally(merge(ccov, cmp, by = "company_id"))

## Observed-only counts. `manual` and `hq_exact` rows are hand-coded footprints;
## `allocated` rows are model output. Anything that holds only in the full file
## and not here is a property of the allocation rule, not of the industry.
obs_rows <- ccov_j[ccov_j$basis %in% c("manual", "hq_exact"), ]
countries$n_observed <- tally(obs_rows)

## Like-for-like sensitivity outcome. n_primary counts direct-contact firms over
## the whole file; this counts direct-contact firms over observed rows only, so
## the two differ in basis and nothing else. Comparing n_primary against the
## all-firm n_observed instead confounds the basis restriction with a change of
## outcome, which matters because hand-coded footprints for satellite and
## open-source firms are far easier to establish than survey footprints.
countries$n_observed_primary <- tally(obs_rows[obs_rows$human_subjects == "direct", ])

message(sprintf("loaded %d countries | %d company-country rows",
                nrow(countries), nrow(ccov)))

## ---- historical layer ------------------------------------------------------
## Exited firms, for the consolidation analysis in 05_history.R. Not included in
## any current-coverage table.
exited <- companies_all[!companies_all$operating, ]
exited$ceased_year_n <- suppressWarnings(as.numeric(exited$ceased_year))
exited$founded_year_n <- suppressWarnings(as.numeric(exited$founded_year))
exited$lifespan <- exited$ceased_year_n - exited$founded_year_n

## ---- ownership and funding layer -------------------------------------------
ownership <- read_di("ownership.csv")
ownership <- merge(ownership,
                   companies_all[, c("company_id", "hq_region", "hq_country",
                                     "ownership_type", "microdata_access", "segment_primary")],
                   by = "company_id", all.x = TRUE)
## Is the stakeholder in the same region as the organisation it backs?
ownership$stakeholder_region <- countries$region_code[
  match(ownership$stakeholder_country, countries$iso3)]
ownership$domestic <- ownership$stakeholder_country == ownership$hq_country
