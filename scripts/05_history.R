## 05_history.R -- exits, absorption and consolidation.
##
## The register deliberately includes firms that no longer operate. Without them
## it would be a survivor sample, and an industry that has consolidated as hard
## as this one cannot be read from its survivors alone.

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

## ---- 1. How firms leave ----------------------------------------------------
t_exit <- table(exited$status, exited$segment_primary)
t_exit <- t_exit[, colSums(t_exit) > 0, drop = FALSE]
emit(t(t_exit), "tab20_exit_mode", "Exit mode by primary segment")

## ---- 2. When ---------------------------------------------------------------
brk <- c(-Inf, 2013, 2016, 2019, 2021, 2023, Inf)
lab <- c("to 2013", "2014-2016", "2017-2019", "2020-2021", "2022-2023", "2024-2026")
t_when <- table(cut(exited$ceased_year_n, brk, labels = lab), exited$status)
emit(t_when, "tab21_exit_period", "Exits by period and mode")

## ---- 3. Lifespan -----------------------------------------------------------
life <- data.frame(
  founded = exited$founded_year_n,
  ceased = exited$ceased_year_n,
  lifespan_years = exited$lifespan)
stargazer(life, type = "text", title = "Lifespan of exited firms",
          out = "output/tab22_lifespan.txt", digits = 1)
stargazer(life, type = "latex", title = "Lifespan of exited firms",
          out = "output/tab22_lifespan.tex", digits = 1, label = "tab:lifespan")

## Absorbed firms versus firms that simply failed.
cat("\n--- exits ---\n")
cat(sprintf("firms in register: %d (%d operating, %d exited)\n",
            nrow(companies_all), nrow(companies), nrow(exited)))
cat(sprintf("absorbed into an acquirer: %d | wound down or insolvent: %d\n",
            sum(exited$status == "absorbed"),
            sum(exited$status %in% c("wound_down", "insolvent"))))
cat(sprintf("median lifespan, absorbed: %.0f years | failed: %.0f years\n",
            median(exited$lifespan[exited$status == "absorbed"], na.rm = TRUE),
            median(exited$lifespan[exited$status %in% c("wound_down","insolvent")], na.rm = TRUE)))

## ---- 4. Where the exits came from -----------------------------------------
cat("\nexits by headquarters region:\n")
print(sort(table(exited$hq_region), decreasing = TRUE))
cat("\nexits by segment:\n")
print(sort(table(exited$segment_primary), decreasing = TRUE))

## ---- 5. Survivorship: what the register would say without them -------------
## Recompute headline shares on the survivor-only sample and on the full one, to
## show the direction and size of the bias that omitting exits would introduce.
share <- function(df) c(
  n = nrow(df),
  pct_NOAM_WEU = round(100 * mean(df$hq_region %in% c("NOAM", "WEU")), 1),
  pct_vc_pe = round(100 * mean(df$ownership_type %in% c("private_vc", "private_pe")), 1),
  pct_direct_contact = round(100 * mean(df$human_subjects == "direct"), 1),
  pct_accessible = round(100 * mean(df$microdata_access %in%
                                      c("open", "researcher_restricted")), 1))
cmp <- rbind(`operating only` = share(companies),
             `including exits` = share(companies_all),
             `exited firms` = share(exited))
emit(cmp, "tab23_survivorship", "Survivorship: register composition with and without exited firms")
cat("\nsurvivorship comparison:\n"); print(cmp)

## ---- 6. Acquirers ----------------------------------------------------------
acq <- sort(table(exited$parent_company[exited$status == "absorbed"]), decreasing = TRUE)
cat("\nacquirers absorbing more than one firm in the register:\n")
print(acq[acq > 1])

message("history tables written to output/")
