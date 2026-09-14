## 03_coverage_gaps.R -- what the industry covers and what it does not.
##
## Three distinct kinds of gap are computed and kept apart, because they have
## different causes and different remedies:
##   existence gap     no firm collects this kind of data in this place
##   access gap        firms collect it but no one outside the client can obtain it
##   modality gap      the only firms present rely on a method that excludes
##                     parts of the population (e.g. online panels where
##                     connectivity is low)

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

SUBSTANTIAL <- 2L                      # coverage score counted as real presence
S  <- (spatial_mat >= SUBSTANTIAL) * 1L # firms x regions, binary
D  <- (domain_mat  >  0L) * 1L          # firms x domains, binary

## ---- 1. Provider density by region -----------------------------------------
open_ids <- companies$microdata_access %in% c("open", "researcher_restricted")
prim_ids <- companies$human_subjects == "direct"

reg_tab <- cbind(
  any_presence        = colSums(spatial_mat > 0),
  substantial         = colSums(S),
  headquartered       = as.integer(table(factor(companies$hq_region, REGION_CODES))),
  primary_collection  = colSums(S[prim_ids, , drop = FALSE]),
  research_accessible = colSums(S[open_ids, , drop = FALSE]))
reg_tab <- cbind(reg_tab,
  access_ratio = round(reg_tab[, "research_accessible"] / reg_tab[, "substantial"], 2))
emit(reg_tab, "tab07_region_density", "Provider density by region")

## ---- 2. Region by domain: the existence gap --------------------------------
rd <- t(S) %*% D
emit(rd, "tab08_region_domain", "Number of providers by region and substantive domain")

## Same cell counts restricted to providers whose microdata a researcher can reach.
rd_open <- t(S[open_ids, , drop = FALSE]) %*% D[open_ids, , drop = FALSE]
emit(rd_open, "tab09_region_domain_accessible",
     "Research-accessible providers by region and substantive domain")

## ---- 3. Thin cells ---------------------------------------------------------
## A cell is thin when fewer than three providers cover it, and closed when no
## provider covering it releases microdata beyond its paying clients.
thin <- which(rd < 3, arr.ind = TRUE)
thin_df <- data.frame(
  region = REGION_CODES[thin[, 1]],
  domain = DOMAIN_CODES[thin[, 2]],
  n_providers = rd[thin],
  n_accessible = rd_open[thin],
  stringsAsFactors = FALSE)
thin_df <- thin_df[order(thin_df$n_providers, thin_df$region, thin_df$domain), ]
write.csv(thin_df, "output/thin_cells.csv", row.names = FALSE)

closed <- data.frame(
  region = REGION_CODES[which(rd_open == 0 & rd > 0, arr.ind = TRUE)[, 1]],
  domain = DOMAIN_CODES[which(rd_open == 0 & rd > 0, arr.ind = TRUE)[, 2]],
  n_providers = rd[rd_open == 0 & rd > 0],
  stringsAsFactors = FALSE)
closed <- closed[order(-closed$n_providers), ]
write.csv(closed, "output/closed_cells.csv", row.names = FALSE)

## ---- 4. Region by segment --------------------------------------------------
seg_f <- factor(companies$segment_primary, levels = sort(unique(segments$segment_code)))
rs <- t(S) %*% model.matrix(~ seg_f - 1)
colnames(rs) <- sub("^seg_f", "", colnames(rs))
emit(t(rs), "tab10_segment_region", "Providers by primary segment and region")

## ---- 5. Modality dependence ------------------------------------------------
## Which collection methods are available in each region. A region served only
## by online or passive-device methods has a coverage problem that provider
## counts alone will not reveal.
mod_f <- factor(companies$modality_primary, levels = modalities$modality_code)
rm_ <- t(S) %*% model.matrix(~ mod_f - 1)
colnames(rm_) <- sub("^mod_f", "", colnames(rm_))
emit(t(rm_), "tab11_modality_region", "Providers by collection modality and region")

## ---- 6. Headline figures ---------------------------------------------------
tot <- length(rd)
cat("\n--- headline figures ---\n")
cat(sprintf("companies in register: %d\n", nrow(companies)))
cat(sprintf("region-domain cells: %d\n", tot))
cat(sprintf("cells with no provider at all: %d (%.1f%%)\n",
            sum(rd == 0), 100 * sum(rd == 0) / tot))
cat(sprintf("cells with fewer than three providers: %d (%.1f%%)\n",
            sum(rd < 3), 100 * sum(rd < 3) / tot))
cat(sprintf("cells with no research-accessible provider: %d (%.1f%%)\n",
            sum(rd_open == 0), 100 * sum(rd_open == 0) / tot))
cat("\nregions ranked by substantial providers:\n")
print(sort(colSums(S), decreasing = TRUE))
cat("\ndomains ranked by providers:\n")
print(sort(colSums(D), decreasing = TRUE))
cat(sprintf("\nshare of firms headquartered in North America or Western Europe: %.1f%%\n",
            100 * mean(companies$hq_region %in% c("NAM", "WEU"))))
cat(sprintf("share of venture or private-equity backed firms in NAM/WEU: %.1f%%\n",
            100 * mean(companies$hq_region[companies$ownership_type %in%
              c("private_vc", "private_pe")] %in% c("NAM", "WEU"))))

write.csv(spatial_long, "output/coverage_spatial_long.csv", row.names = FALSE)
write.csv(domain_long, "output/coverage_domain_long.csv", row.names = FALSE)
message("gap analysis written to output/")
