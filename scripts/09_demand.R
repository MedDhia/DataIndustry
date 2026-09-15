## 09_demand.R -- the buyer side, and segment entry as a proxy for demand.
##
## Two separate things are done here and they should not be confused.
##
## (1) Entry cohorts. The register records when for-profit firms were founded,
##     so the share of a segment's firms founded recently is a revealed
##     preference measure: capital and founders went where they expected to be
##     paid. It is a proxy, not a measurement of demand. There is no revenue in
##     this file, and a segment can fill with entrants who all fail. Entry is
##     therefore always printed next to the exit rate.
##
## (2) The demand layer, data/demand.csv. 65 rows keyed on segment and buyer
##     category, each with its own evidence level and source. It is a purposive
##     sample of documented buying, not a census of buyers, so every table below
##     prints its denominator and none of them is weighted.

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

## ---- 1. Entry cohorts by segment ------------------------------------------
fp <- companies_all[companies_all$sector == "for_profit", ]
fp$founded <- suppressWarnings(as.numeric(fp$founded_year))
fp$cohort <- cut(fp$founded, c(-Inf, 1999, 2009, 2014, 2018, Inf),
                 labels = c("pre2000", "y2000_09", "y2010_14", "y2015_18", "y2019plus"))
cat(sprintf("for-profit firms: %d, of which %d carry a founding year\n",
            nrow(fp), sum(!is.na(fp$founded))))

by_seg <- split(fp, fp$segment_primary)
rise <- do.call(rbind, lapply(names(by_seg), function(s) {
  d <- by_seg[[s]]
  k <- d[!is.na(d$cohort), ]
  if (nrow(k) < 6) return(NULL)
  data.frame(segment = s,
             n_dated = nrow(k),
             n_total = nrow(d),
             recent_pct = round(100 * mean(k$cohort %in% c("y2015_18", "y2019plus"))),
             exit_pct = round(100 * mean(!d$operating), 1),
             pre2000 = sum(k$cohort == "pre2000"),
             y2000_09 = sum(k$cohort == "y2000_09"),
             y2010_14 = sum(k$cohort == "y2010_14"),
             y2015_18 = sum(k$cohort == "y2015_18"),
             y2019plus = sum(k$cohort == "y2019plus"),
             stringsAsFactors = FALSE)
}))
rise <- rise[order(-rise$recent_pct), ]
rownames(rise) <- NULL
emit(rise, "tab33_entry_cohorts",
     "For-profit entry cohorts and exit rate by segment (segments with 6 or more dated firms)")
write.csv(rise, "output/entry_cohorts.csv", row.names = FALSE)

## Entry and exit read together. A segment that is filling with entrants AND
## losing incumbents is churning, not growing; the two are not the same signal.
rise$profile <- ifelse(rise$recent_pct >= 45 & rise$exit_pct < 12, "expanding",
                ifelse(rise$recent_pct >= 45, "churning",
                ifelse(rise$exit_pct >= 15, "consolidating", "mature_stable")))
emit(table(rise$profile), "tab34_segment_profile",
     "Segments classified by entry share and exit rate")
cat("\nsegment profiles:\n")
print(rise[order(rise$profile, -rise$recent_pct), c("segment", "recent_pct", "exit_pct", "profile")])

## ---- 2. The demand layer ---------------------------------------------------
demand <- read_di("demand.csv")
cat(sprintf("\ndemand layer: %d rows, %d segments, %d buyer categories\n",
            nrow(demand), length(unique(demand$segment)),
            length(unique(demand$buyer_category))))

demand$family <- segments$segment_family[match(demand$segment, segments$segment_code)]
emit(table(demand$buyer_category, demand$family),
     "tab35_buyer_family", "Buyer category by segment family (rows are demand-layer rows, not buyers)")

emit(table(demand$buyer_category, demand$direction),
     "tab36_buyer_direction", "Direction of demand by buyer category")

## Evidence is not evenly available: public procurement is documented and
## commercial subscription is not, so state buyers are over-represented among
## the A rows. This table is about the record, not about the industry.
emit(table(demand$evidence_level, demand$contract_visibility),
     "tab37_evidence_visibility", "Evidence level by contract visibility in the demand layer")

## ---- 3. Does a state security buyer travel with anything? ------------------
sec <- unique(demand$segment[demand$buyer_category == "government_security"])
fpo <- companies[companies$sector == "for_profit", ]
fpo$sec_buyer <- ifelse(fpo$segment_primary %in% sec, "security buyer", "no security buyer")
emit(table(fpo$sec_buyer, fpo$microdata_access),
     "tab38_security_disclosure",
     "Microdata access of operating for-profit firms by whether their segment has a documented state security buyer")
cat(sprintf("\nsegments with a documented state security buyer: %s\n",
            paste(sort(sec), collapse = ", ")))

## ---- 4. Breadth of documented demand against entry -------------------------
breadth <- as.data.frame(table(demand$segment), stringsAsFactors = FALSE)
names(breadth) <- c("segment", "buyer_rows")
cmb <- merge(rise[, c("segment", "recent_pct", "exit_pct")], breadth, by = "segment")
cat(sprintf("\ncorrelation between documented buyer breadth and recent-entry share: %.2f (n=%d)\n",
            cor(cmb$buyer_rows, cmb$recent_pct), nrow(cmb)))
cat("Buyer rows are a count of what could be evidenced, so this is a property of\n",
    "the research effort as much as of the industry. It is reported, not interpreted.\n", sep = "")

## ---- 5. Price signals that could be attached to a source -------------------
ps <- demand[!is.na(demand$price_signal_usd), c("demand_id", "segment", "buyer_category",
                                                "price_signal_usd", "price_signal_basis",
                                                "signal_year", "evidence_level")]
ps <- ps[order(-ps$price_signal_usd), ]
rownames(ps) <- NULL
emit(ps, "tab39_price_signals", "Documented price signals in the demand layer")
write.csv(ps, "output/demand_price_signals.csv", row.names = FALSE)
