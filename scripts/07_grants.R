## 07_grants.R -- the recurring funding instruments layer.
## Descriptives only: 15 programmes is too few for anything inferential, and the
## file is a purposive sample rather than a population. Every table below prints
## its denominator for that reason.

source("scripts/01_load.R")
library(stargazer)
dir.create("output", showWarnings = FALSE)

progs <- read.csv("data/grant_programmes.csv", stringsAsFactors = FALSE)
cat(sprintf("loaded %d grant programmes (%d open, %d discontinued)\n",
            nrow(progs), sum(progs$status == "open"),
            sum(progs$status == "discontinued")))

emit <- function(obj, name, title) {
  obj <- as.data.frame.matrix(as.matrix(obj))
  for (ty in c("text", "latex")) {
    ext <- if (ty == "text") "txt" else "tex"
    stargazer(obj, type = ty, title = title, summary = FALSE, rownames = TRUE,
              out = file.path("output", paste0(name, ".", ext)))
  }
}

## ---- 1. Instrument type by how squarely the programme targets data work -----
emit(table(progs$instrument_type, progs$data_specific),
     "tab26_instrument_data", "Grant instrument type by data specificity")

## ---- 2. Who funds, and on what cadence ------------------------------------
emit(table(progs$funder_category, progs$cadence),
     "tab27_funder_cadence", "Funder category by cadence")

## ---- 3. Region eligibility -------------------------------------------------
regs <- unique(unlist(strsplit(progs$eligible_regions, "|", fixed = TRUE)))
elig <- sapply(regs, function(r)
  sum(grepl(r, progs$eligible_regions, fixed = TRUE) & progs$status == "open"))
elig_df <- data.frame(region = names(sort(elig, decreasing = TRUE)),
                      open_programmes = sort(elig, decreasing = TRUE))
emit(elig_df, "tab28_region_eligibility",
     "Open programmes for which each region is eligible")

## ---- 4. Award size ---------------------------------------------------------
size <- data.frame(programme = progs$programme_name,
                   min_usd = progs$award_min_usd,
                   max_usd = progs$award_max_usd,
                   data_specific = progs$data_specific,
                   status = progs$status)
size <- size[order(-size$max_usd), ]
write.csv(size, "output/grant_award_sizes.csv", row.names = FALSE)

## ---- 5. Overlap with the funders already recorded in ownership.csv ---------
## A programme counts as observed in the register when one of its funders already
## appears as a funder of an organisation in companies.csv. This is the only
## empirical link between the two layers and it is deliberately narrow.
own_funders <- unique(ownership$stakeholder_name[ownership$stakeholder_type == "funder"])
hit <- sapply(strsplit(progs$funders, "|", fixed = TRUE),
              function(fs) any(fs %in% own_funders))
cat(sprintf("\nprogrammes whose funder already appears in ownership.csv: %d of %d\n",
            sum(hit), nrow(progs)))
cat(paste0("  ", progs$programme_name[hit], collapse = "\n"), "\n")
