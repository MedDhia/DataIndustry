## 10_innovation.R -- the method layer: what was new, and how crowded it was.
##
## The question is whether firms whose entry rested on a genuinely new
## collection method arrived into crowded segments or into empty ones. The
## register can answer a version of that: for each innovator, count the firms
## already in its segment at the moment it first deployed the method.
##
## That count is a property of this register's enumeration as much as of the
## industry. Earth observation and survey work are enumerated deeply here;
## digital olfaction or wifi sensing are not. A prior-occupant count of 60 means
## a segment this file knows well, so the counts compare innovators against each
## other within a segment far better than across segments. Every table below
## prints the segment.

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

innov <- read_di("method_innovations.csv")
cat(sprintf("innovation layer: %d firms, %d novelty types, %d contested\n",
            nrow(innov), length(unique(innov$novelty_type)),
            sum(innov$contested == "yes")))

cmp <- companies_all[, c("company_id", "company_name", "segment_primary", "hq_region",
                         "founded_year", "status", "operating", "sector",
                         "microdata_access", "modality_primary")]
innov <- merge(innov, cmp, by = "company_id", all.x = TRUE)
innov$deploy <- suppressWarnings(as.numeric(innov$first_deployment_year))

## ---- 1. How crowded was the segment when the method arrived? ---------------
## Prior occupants: firms in the same segment with a founding year strictly
## before the innovator's first deployment. Exited firms count, because they
## were competitors at the time even if they are gone now.
founded_n <- suppressWarnings(as.numeric(companies_all$founded_year))
prior <- mapply(function(seg, yr) {
  if (is.na(yr)) return(NA_integer_)
  sum(companies_all$segment_primary == seg & !is.na(founded_n) & founded_n < yr)
}, innov$segment_primary, innov$deploy)
innov$prior_occupants <- as.integer(prior)

cat(sprintf("\nprior occupants at first deployment: median %d, range %d to %d\n",
            median(innov$prior_occupants, na.rm = TRUE),
            min(innov$prior_occupants, na.rm = TRUE),
            max(innov$prior_occupants, na.rm = TRUE)))
cat(sprintf("entered a segment with 20 or more prior occupants: %d of %d\n",
            sum(innov$prior_occupants >= 20, na.rm = TRUE), nrow(innov)))
cat(sprintf("entered a segment with fewer than 5: %d\n",
            sum(innov$prior_occupants < 5, na.rm = TRUE)))

tab <- innov[order(-innov$prior_occupants),
             c("company_name", "segment_primary", "novelty_type",
               "first_deployment_year", "prior_occupants", "contested")]
rownames(tab) <- NULL
emit(tab, "tab40_innovators", "Method innovators, ordered by how crowded the segment already was")
write.csv(tab, "output/method_innovators.csv", row.names = FALSE)

## ---- 2. What kind of novelty, and where ------------------------------------
emit(table(innov$novelty_type, innov$hq_region),
     "tab41_novelty_region", "Type of methodological novelty by region of headquarters")

emit(table(innov$novelty_type, innov$contested),
     "tab42_novelty_contested",
     "Whether the method has drawn litigation, regulatory action or documented accuracy disputes")

## ---- 3. Do innovators disclose more than the firms they competed with? -----
## Restricted twice over: to operating FOR-PROFIT firms, and to the segments the
## innovators are actually in. Without the sector restriction the comparison is
## a trick, because five of the innovators are nonprofits that publish by
## constitution and would carry the whole difference on their own.
inn_ids <- innov$company_id
segs_in <- unique(innov$segment_primary)
fp_op <- companies[companies$sector == "for_profit" &
                     companies$segment_primary %in% segs_in, ]
acc <- function(d) sum(d$microdata_access %in% c("open", "researcher_restricted"))
inn_fp <- fp_op[fp_op$company_id %in% inn_ids, ]
peers  <- fp_op[!(fp_op$company_id %in% inn_ids), ]
cat(sprintf("\ndisclosure, operating for-profit firms in the innovators' segments:\n  innovators %d of %d (%.1f%%)\n  everyone else %d of %d (%.1f%%)\n",
            acc(inn_fp), nrow(inn_fp), 100 * acc(inn_fp) / nrow(inn_fp),
            acc(peers), nrow(peers), 100 * acc(peers) / nrow(peers)))
cat(sprintf("  for comparison, all %d operating innovators including nonprofits: %d disclose (%.1f%%)\n",
            sum(companies$company_id %in% inn_ids),
            acc(companies[companies$company_id %in% inn_ids, ]),
            100 * acc(companies[companies$company_id %in% inn_ids, ]) /
              sum(companies$company_id %in% inn_ids)))
emit(table(ifelse(fp_op$company_id %in% inn_ids, "innovator", "other"),
           fp_op$microdata_access),
     "tab43_innovator_disclosure",
     "Microdata access of operating for-profit firms in the innovators' segments")

## ---- 4. Did the innovators survive? ----------------------------------------
emit(table(innov$novelty_type, innov$status),
     "tab44_innovator_status", "Status of method innovators by type of novelty")
cat(sprintf("\ninnovators no longer independent: %d of %d (%.0f%%); register-wide rate is %.0f%%\n",
            sum(!innov$operating), nrow(innov), 100 * mean(!innov$operating),
            100 * mean(!companies_all$operating)))

## ---- 5. Sector and ownership of innovators ---------------------------------
emit(table(innov$novelty_type, innov$sector),
     "tab45_innovator_sector", "Sector of method innovators by type of novelty")
