## 01_load.R -- read the dataset and construct the derived matrices.
## Sourced by the other scripts. No side effects other than objects in memory.

read_di <- function(f) utils::read.csv(file.path("data", f), stringsAsFactors = FALSE,
                                       na.strings = c("NA", ""), encoding = "UTF-8")

companies <- read_di("companies.csv")
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

stopifnot(identical(sort(rownames(spatial_mat)), sort(companies$company_id)))
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

message(sprintf("loaded %d companies | %d regions | %d domains | %d segments",
                nrow(companies), length(REGION_CODES), length(DOMAIN_CODES),
                nrow(segments)))
