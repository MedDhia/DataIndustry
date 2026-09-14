## 02_descriptives.R -- descriptive tables for the company register.
## Tables are written with stargazer to output/ as plain text and LaTeX.

source("scripts/01_load.R")
library(stargazer)

dir.create("output", showWarnings = FALSE)

emit <- function(obj, name, title, ...) {
  ## stargazer needs a data frame; raw table objects confuse its dimname handling.
  obj <- as.data.frame.matrix(as.matrix(obj))
  for (ty in c("text", "latex")) {
    ext <- if (ty == "text") "txt" else "tex"
    stargazer(obj, type = ty, title = title, summary = FALSE, rownames = TRUE,
              out = file.path("output", paste0(name, ".", ext)), ...)
  }
}

## 1. Numeric summary of the register.
num <- data.frame(
  founded_year = suppressWarnings(as.numeric(companies$founded_year)),
  countries_claimed = suppressWarnings(as.numeric(companies$countries_claimed)),
  firm_age = 2026 - suppressWarnings(as.numeric(companies$founded_year)),
  n_regions_covered = rowSums(spatial_mat > 0),
  n_regions_substantial = rowSums(spatial_mat >= 2),
  n_domains = rowSums(domain_mat > 0))
stargazer(num, type = "text", title = "Company register: numeric summary",
          out = "output/tab01_summary.txt", digits = 1)
stargazer(num, type = "latex", title = "Company register: numeric summary",
          out = "output/tab01_summary.tex", digits = 1, label = "tab:summary")

## 2. Segment by maturity class.
t_seg <- table(companies$segment_primary, companies$maturity_class)
t_seg <- t_seg[, c("established", "scaleup", "startup")]
t_seg <- cbind(t_seg, Total = rowSums(t_seg))
t_seg <- rbind(t_seg, Total = colSums(t_seg))
emit(t_seg, "tab02_segment_maturity", "Primary segment by maturity class")

## 3. Ownership by headquarters region.
t_own <- table(companies$ownership_type, companies$hq_region)[, REGION_CODES]
emit(t_own, "tab03_ownership_hqregion", "Ownership type by headquarters region")

## 4. Access regime: who can actually obtain the microdata.
t_acc <- table(companies$segment_primary, companies$microdata_access)
t_acc <- t_acc[, c("open", "researcher_restricted", "commercial_only", "none")]
emit(t_acc, "tab04_microdata_access", "Microdata access regime by primary segment")

## 5. Consent basis by whether the firm touches human subjects.
t_con <- table(companies$consent_model, companies$human_subjects)
emit(t_con, "tab05_consent", "Consent basis by human subject contact")

## 6. Evidence quality of the coding itself.
t_ev <- t(table(companies$evidence_level, companies$segment_primary))
emit(t_ev, "tab06_evidence", "Evidence level of coded records by segment")

message("descriptive tables written to output/")
