## 04_country_gaps.R -- country-level coverage, by data type and by method.

source("scripts/01_load.R")
library(stargazer)
dir.create("output", showWarnings = FALSE)

emit <- function(obj, name, title, ...) {
  obj <- as.data.frame.matrix(as.matrix(obj))
  for (ty in c("text", "latex")) {
    ext <- if (ty == "text") "txt" else "tex"
    stargazer(obj, type = ty, title = title, summary = FALSE, rownames = TRUE,
              out = file.path("output", paste0(name, ".", ext)), ...)
  }
}

## Expand the pipe-delimited method and domain columns to long form.
expand_col <- function(df, col) {
  parts <- strsplit(df[[col]], "|", fixed = TRUE)
  data.frame(iso3 = rep(df$iso3, lengths(parts)),
             company_id = rep(df$company_id, lengths(parts)),
             value = unlist(parts), stringsAsFactors = FALSE)
}
dom_long <- expand_col(ccov_j, "domains")
met_long <- expand_col(ccov_j, "methods")

acc_ids <- companies$company_id[companies$microdata_access %in%
                                  c("open", "researcher_restricted")]

## ---- 1. Country rankings ---------------------------------------------------
rank_df <- countries[order(countries$n_providers),
                     c("iso3","country_name","region_code","income_group",
                       "population_band","n_any","n_providers","n_primary","n_accessible")]
write.csv(rank_df, "output/country_provider_counts.csv", row.names = FALSE)

worst <- head(rank_df, 25); best <- tail(rank_df, 15)
emit(as.matrix(worst[, -1]), "tab12_countries_worst",
     "Twenty-five least served countries by number of providers")
emit(as.matrix(best[, -1]), "tab13_countries_best",
     "Fifteen best served countries by number of providers")

## ---- 2. Data type availability by country ----------------------------------
## For each domain: in how many of the 194 countries is it obtainable at all,
## and in how many from a provider a researcher can reach?
dom_ctry <- tapply(dom_long$iso3, dom_long$value, function(x) length(unique(x)))
dom_ctry_acc <- tapply(dom_long$iso3[dom_long$company_id %in% acc_ids],
                       dom_long$value[dom_long$company_id %in% acc_ids],
                       function(x) length(unique(x)))
dom_tab <- data.frame(
  countries_with_any = as.integer(dom_ctry[DOMAIN_CODES]),
  countries_missing  = 194L - as.integer(dom_ctry[DOMAIN_CODES]),
  countries_accessible = as.integer(ifelse(is.na(dom_ctry_acc[DOMAIN_CODES]), 0,
                                           dom_ctry_acc[DOMAIN_CODES])),
  row.names = DOMAIN_CODES)
dom_tab$closed_countries <- dom_tab$countries_with_any - dom_tab$countries_accessible
dom_tab <- dom_tab[order(dom_tab$countries_with_any), ]
emit(dom_tab, "tab14_domain_country_availability",
     "Country availability of each data type out of 194")

## ---- 3. Method availability by country --------------------------------------
met_ctry <- tapply(met_long$iso3, met_long$value, function(x) length(unique(x)))
met_prov <- table(met_long$value)
met_tab <- data.frame(
  countries_with_any = as.integer(met_ctry[names(met_prov)]),
  provider_country_pairs = as.integer(met_prov),
  row.names = names(met_prov))
met_tab <- met_tab[order(-met_tab$countries_with_any), ]
emit(met_tab, "tab15_method_country_availability",
     "Country availability of each collection method out of 194")

## Methods available in the least served countries, which is where method
## narrowness bites hardest.
thin_iso <- rank_df$iso3[rank_df$n_providers <= quantile(countries$n_providers, 0.25)]
met_thin <- table(met_long$value[met_long$iso3 %in% thin_iso])
met_rich <- table(met_long$value[!met_long$iso3 %in% thin_iso])
met_cmp <- data.frame(
  bottom_quartile_share = round(100 * as.numeric(met_thin[names(met_prov)]) /
                                  sum(met_thin, na.rm = TRUE), 1),
  rest_share = round(100 * as.numeric(met_rich[names(met_prov)]) /
                       sum(met_rich, na.rm = TRUE), 1),
  row.names = names(met_prov))
met_cmp[is.na(met_cmp)] <- 0
emit(met_cmp, "tab16_method_mix", "Method mix in the least served quartile versus the rest")

## ---- 4. What predicts how many providers a country attracts ----------------
countries$conflict <- as.integer(countries$conflict_affected)
countries$restrictive <- as.integer(countries$restrictive_research_regime)
countries$log_providers <- log1p(countries$n_providers)

m1 <- lm(log_providers ~ income_group + population_band + internet_band, data = countries)
m2 <- lm(log_providers ~ income_group + population_band + internet_band +
           conflict + restrictive, data = countries)
m3 <- glm(n_primary ~ income_group + population_band + internet_band +
            conflict + restrictive, family = poisson, data = countries)
m4 <- glm(n_accessible ~ income_group + population_band + internet_band +
            conflict + restrictive, family = poisson, data = countries)

lbl <- c("Income: LMIC","Income: UMIC","Income: HIC",
         "Population: S","Population: M","Population: L","Population: XL",
         "Internet: medium","Internet: high",
         "Conflict-affected","Restrictive research regime")
for (ty in c("text","latex")) {
  ext <- if (ty == "text") "txt" else "tex"
  stargazer(m1, m2, m3, m4, type = ty,
            title = "What predicts the number of data collectors present in a country",
            covariate.labels = lbl,
            dep.var.labels = c("log(1 + providers)", "primary collectors", "accessible providers"),
            column.labels = c("OLS","OLS","Poisson","Poisson"),
            omit.stat = c("ser","f"), digits = 2,
            notes = "Baselines: low income, XS population, low internet penetration.",
            out = file.path("output", paste0("tab17_country_model.", ext)))
}

## ---- 4b. Sensitivity: do the results survive without the allocated rows? ----
## 97 percent of company-country rows are allocated by the model in
## 00_build_country_coverage.py. Any claim that does not also appear in the
## observed-only column is a property of that model.
## Column 2 is the like-for-like test: same outcome definition as column 1,
## restricted to observed rows. Column 3 keeps the all-firm count for comparison
## and is NOT like-for-like, because hand-coded footprints are much easier to
## establish for satellite and open-source firms than for survey firms, so it
## mixes the basis restriction with a shift in the composition of collectors.
m5 <- glm(n_observed_primary ~ income_group + population_band + internet_band +
            conflict + restrictive, family = poisson, data = countries)
m6 <- glm(n_observed ~ income_group + population_band + internet_band +
            conflict + restrictive, family = poisson, data = countries)
for (ty in c("text","latex")) {
  ext <- if (ty == "text") "txt" else "tex"
  stargazer(m3, m5, m6, type = ty,
            title = "Sensitivity: modelled coverage versus hand-coded footprints only",
            covariate.labels = lbl,
            dep.var.labels = c("primary collectors", "all providers"),
            column.labels = c("full file","observed only","observed, all firms"),
            omit.stat = c("ser","f"), digits = 2,
            notes = paste("Columns 1 and 2 share an outcome and differ only in basis.",
                          "Column 3 changes the outcome and is not like-for-like."),
            out = file.path("output", paste0("tab19_sensitivity.", ext)))
}
cat("\ncorrelation, modelled vs observed provider counts: ",
    round(cor(countries$n_providers, countries$n_observed, method = "spearman"), 3), "\n", sep = "")
cat("correlation, primary collectors, full vs observed: ",
    round(cor(countries$n_primary, countries$n_observed_primary, method = "spearman"), 3), "\n", sep = "")

## ---- 5. Underserved relative to population ---------------------------------
pop_mid <- c(XS = 0.5, S = 5, M = 25, L = 70, XL = 200)   # midpoint of each band, millions
countries$pop_m <- pop_mid[as.character(countries$population_band)]
countries$providers_per_10m <- round(countries$n_providers / (countries$pop_m / 10), 1)
under <- countries[countries$pop_m >= 25, ]
under <- under[order(under$providers_per_10m),
               c("iso3","country_name","region_code","income_group","population_band",
                 "n_providers","n_primary","providers_per_10m")]
write.csv(under, "output/underserved_by_population.csv", row.names = FALSE)
emit(as.matrix(head(under, 20)[, -1]), "tab18_underserved_population",
     "Twenty worst served large countries per 10 million population")

## ---- 6. Headline figures ---------------------------------------------------
cat("\n--- country layer ---\n")
cat(sprintf("company-country rows: %d (manual %d, hq_exact %d, allocated %d)\n",
            nrow(ccov), sum(ccov$basis=="manual"), sum(ccov$basis=="hq_exact"),
            sum(ccov$basis=="allocated")))
cat(sprintf("countries with at least one provider: %d of 194\n", sum(countries$n_any > 0)))
cat(sprintf("countries with no primary collector: %d\n", sum(countries$n_primary == 0)))
cat(sprintf("countries with no research-accessible provider: %d\n",
            sum(countries$n_accessible == 0)))
cat(sprintf("median providers: %.0f | IQR %.0f to %.0f | max %d (%s) | min %d (%s)\n",
            median(countries$n_providers),
            quantile(countries$n_providers,.25), quantile(countries$n_providers,.75),
            max(countries$n_providers), countries$iso3[which.max(countries$n_providers)],
            min(countries$n_providers), countries$iso3[which.min(countries$n_providers)]))
cat("\nmean providers by income group:\n")
print(round(tapply(countries$n_providers, countries$income_group, mean), 1))
cat("\nmean primary collectors by conflict exposure (MODEL-DRIVEN, see tab19):\n")
print(round(tapply(countries$n_primary, countries$conflict, mean), 1))
cat("mean OBSERVED providers by conflict exposure:\n")
print(round(tapply(countries$n_observed, countries$conflict, mean), 1))
cat("\nmean primary collectors by research regime:\n")
print(round(tapply(countries$n_primary, countries$restrictive, mean), 1))
cat("mean OBSERVED providers by research regime:\n")
print(round(tapply(countries$n_observed, countries$restrictive, mean), 1))
cat("mean OBSERVED PRIMARY collectors by research regime (like-for-like):\n")
print(round(tapply(countries$n_observed_primary, countries$restrictive, mean), 1))
message("country gap analysis written to output/")
