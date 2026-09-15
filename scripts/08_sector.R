## 08_sector.R -- the for-profit cut.
## `sector` separates commercial firms from nonprofits, universities and state
## bodies. This script reports the register both ways, because several findings
## in docs/coverage_gaps.md rest on a population that is not all commercial.

source("scripts/01_load.R")
library(stargazer)
dir.create("output", showWarnings = FALSE)

emit <- function(obj, name, title) {
  obj <- as.data.frame.matrix(as.matrix(obj))
  for (ty in c("text", "latex")) {
    ext <- if (ty == "text") "txt" else "tex"
    stargazer(obj, type = ty, title = title, summary = FALSE, rownames = TRUE,
              out = file.path("output", paste0(name, ".", ext)))
  }
}

cat(sprintf("operating firms: %d, of which for-profit %d (%.1f%%)\n",
            nrow(companies), sum(companies$sector == "for_profit"),
            100 * mean(companies$sector == "for_profit")))

## ---- 1. Sector by region -----------------------------------------------------
emit(table(companies$hq_region, companies$sector),
     "tab29_sector_region", "Sector by headquarters region, operating organisations")

## ---- 2. Sector by segment ----------------------------------------------------
emit(table(companies$segment_primary, companies$sector),
     "tab30_sector_segment", "Sector by primary segment, operating organisations")

## ---- 3. Disclosure, whole register against for-profits only ------------------
## The access finding in section 1 of coverage_gaps.md is computed over every
## operating organisation. Restricting to commercial firms is the test of whether
## it is a fact about an industry or about a donor-funded research network.
acc <- function(df) sum(df$microdata_access %in% c("open", "researcher_restricted"))
regs <- c("NOAM", "WEU", "SSA", "MENA", "SAS", "SEA", "LAC", "EEU", "OCE", "EAS", "CHN", "RUS")
rows <- lapply(regs, function(rg) {
  a <- companies[companies$hq_region == rg, ]
  b <- a[a$sector == "for_profit", ]
  data.frame(all_n = nrow(a), all_acc = acc(a),
             all_pct = round(100 * acc(a) / max(nrow(a), 1), 1),
             fp_n = nrow(b), fp_acc = acc(b),
             fp_pct = round(100 * acc(b) / max(nrow(b), 1), 1))
})
disc <- do.call(rbind, rows); rownames(disc) <- regs
emit(disc, "tab31_disclosure_forprofit",
     "Microdata disclosure: all operating organisations against for-profits only")

## ---- 4. Exit rate by sector --------------------------------------------------
## Only for-profit organisations can be acquired, so the exit analysis in
## section 14 is really an analysis of the commercial layer.
emit(table(companies_all$sector, companies_all$status),
     "tab32_sector_status", "Status by sector, whole register including exits")

cat("\nfor-profit share by region:\n")
for (rg in regs) {
  a <- companies[companies$hq_region == rg, ]
  if (nrow(a) == 0) next
  cat(sprintf("  %-5s %3d of %3d (%.1f%%)\n", rg,
              sum(a$sector == "for_profit"), nrow(a),
              100 * mean(a$sector == "for_profit")))
}
