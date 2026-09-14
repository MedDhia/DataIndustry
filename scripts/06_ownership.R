## 06_ownership.R -- founders, owners and funders.
##
## Coverage is partial by design: a row exists only where the relationship could
## be established from a source. Absence of a stakeholder row means not
## established, never that the organisation has no owner or funder.

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

cat("\n--- ownership layer ---\n")
cat(sprintf("%d stakeholder rows covering %d of %d organisations (%.0f%%)\n",
            nrow(ownership), length(unique(ownership$company_id)),
            nrow(companies_all),
            100 * length(unique(ownership$company_id)) / nrow(companies_all)))

## ---- 1. Who backs what kind of collector -----------------------------------
t_cat <- table(ownership$stakeholder_category, ownership$stakeholder_type)
emit(t_cat, "tab24_stakeholder_type", "Stakeholder category by relationship type")

## ---- 2. The open layer and its funders -------------------------------------
## Grant funding is what distinguishes the collectors that publish, so the
## question is who supplies it and from where.
fund <- ownership[ownership$stakeholder_type == "funder", ]
cat(sprintf("\nfunder rows: %d across %d organisations\n",
            nrow(fund), length(unique(fund$company_id))))
cat("\nfunders by category:\n"); print(sort(table(fund$stakeholder_category), decreasing = TRUE))
cat("\nfunders by country:\n"); print(sort(table(fund$stakeholder_country), decreasing = TRUE))
cat("\nfunders by region:\n"); print(sort(table(fund$stakeholder_region), decreasing = TRUE))

## Where the funded organisation sits, against where its money comes from.
flow <- table(factor(fund$hq_region, levels = REGION_CODES),
              factor(fund$stakeholder_region, levels = REGION_CODES))
flow <- flow[rowSums(flow) > 0, colSums(flow) > 0, drop = FALSE]
emit(flow, "tab25_funding_flow", "Funding flows: recipient region by funder region")

cat(sprintf("\nshare of funding relationships that are domestic: %.1f%%\n",
            100 * mean(fund$domestic, na.rm = TRUE)))
cat(sprintf("share where the funder is in North America or Western Europe: %.1f%%\n",
            100 * mean(fund$stakeholder_region %in% c("NOAM", "WEU"), na.rm = TRUE)))

## ---- 3. Funder concentration -----------------------------------------------
## How many distinct funders carry the openly accessible collectors, and how
## concentrated is that set?
open_ids <- companies_all$company_id[companies_all$microdata_access %in%
                                       c("open", "researcher_restricted")]
fo <- fund[fund$company_id %in% open_ids, ]
tab <- sort(table(fo$stakeholder_name), decreasing = TRUE)
cat(sprintf("\nopen-layer organisations with funder rows: %d\n", length(unique(fo$company_id))))
cat(sprintf("distinct funders behind them: %d\n", length(tab)))
cat("funders appearing more than once:\n"); print(tab[tab > 1])

## ---- 4. Founders -----------------------------------------------------------
fnd <- ownership[ownership$stakeholder_type == "founder", ]
cat(sprintf("\nfounder rows: %d across %d organisations\n",
            nrow(fnd), length(unique(fnd$company_id))))
cat("founder nationality by organisation headquarters region:\n")
print(table(factor(fnd$hq_region, levels = REGION_CODES),
            ifelse(fnd$domestic, "domestic founder", "founder elsewhere")))

## ---- 5. State ownership ----------------------------------------------------
st <- ownership[ownership$stakeholder_category == "state" &
                  ownership$stakeholder_type == "controlling_owner", ]
cat(sprintf("\nstate-controlled collectors with an owner row: %d\n", nrow(st)))
cat("by region:\n"); print(sort(table(st$hq_region), decreasing = TRUE))
cat("their microdata access:\n"); print(table(st$microdata_access))

write.csv(ownership, "output/ownership_joined.csv", row.names = FALSE)
message("ownership tables written to output/")
