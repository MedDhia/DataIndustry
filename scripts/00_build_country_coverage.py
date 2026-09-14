#!/usr/bin/env python3
"""Construct the company-by-country coverage file, typed by data domain and method.

Output: data/coverage_country.csv, one row per company-country pair where the
company has non-zero coverage, carrying the coverage score, the collection
methods usable in that country, and the substantive domains obtainable there.

Rows are produced by three bases, recorded in `basis`:

  manual     from data/coverage_country_manual.csv, hand-coded from published
             country lists or known operating footprints. Each firm there is
             marked `exhaustive` (the list is complete, the model adds nothing)
             or `partial` (these countries are observed, the model fills the
             rest of the firm's stated country budget around them)
  hq_exact   single-country firms, resolved to their headquarters country
  allocated  distributed from the region-level score in coverage_spatial.csv
             across countries, by the documented priority rules below

Only `manual` and `hq_exact` rows are observations. `allocated` rows are a model
of where a firm of that type, size and regional footprint most likely operates.
They are useful in aggregate and should not be cited for an individual firm.

THE ALLOCATION MODEL

A firm's stated country count is treated as a budget. The budget is split across
the regions where it has coverage, weighted by the square of the regional score
times the number of countries in the region, so a flagship region absorbs far
more of the budget than a thin one and a large region absorbs more than a small
one. A firm claiming near-universal reach therefore lands in near-universal
country coverage, which is the correct result for satellite operators and web
crawlers. Within a region, countries are ranked by a priority score and the
budget is spent from the top down, with coverage decaying by rank.

Three priority orderings are used, because different parts of the industry enter
countries for different reasons:

  market   commercial attractiveness: income, population, connectivity.
           Used for firms that sell data about a country's consumers or firms.
  labour   cost and availability of a distributed workforce: large population,
           usable connectivity, low income. Used for annotation and micro-task
           firms, whose country coverage describes where their workers are.
  need     humanitarian and development demand: low income, conflict exposure,
           large population. Used for firms whose clients are donors and agencies.

Each ordering is a falsifiable claim about entry. Change the weights, rerun, and
the gap tables move accordingly.
"""
import csv, collections, math, sys

INCOME_W   = {"HIC": 4, "UMIC": 3, "LMIC": 2, "LIC": 1}
POP_W      = {"XL": 5, "L": 4, "M": 3, "S": 2, "XS": 1}
INTERNET_W = {"high": 2, "medium": 1, "low": 0}

# Methods each segment can deploy, beyond the firm's own modality_primary.
SEGMENT_METHODS = {
 "survey_insights": ["face_to_face", "telephone", "online_panel"],
 "field_agency": ["face_to_face", "telephone"],
 "panel_sample": ["online_panel"],
 "collection_software": ["face_to_face", "online_panel"],
 "crowd_micro": ["crowd_task", "mobile_app"],
 "ai_training_data": ["crowd_task", "expert_elicit"],
 "expert_network": ["expert_elicit"],
 "web_data": ["web_scrape"],
 "consumer_broker": ["admin_records", "api_partner"],
 "location_mobility": ["device_passive"],
 "telecom_data": ["telecom_network"],
 "earth_observation": ["remote_sensing"],
 "iot_telemetry": ["sensor_hardware", "device_passive"],
 "financial_altdata": ["transaction", "web_scrape"],
 "trade_logistics": ["sensor_hardware", "admin_records"],
 "retail_pricing": ["transaction", "web_scrape"],
 "health_rwd": ["clinical_records"],
 "audience_measurement": ["device_passive", "online_panel"],
 "social_osint": ["web_scrape", "api_partner"],
 "b2b_firmographic": ["web_scrape", "admin_records"],
 "climate_risk": ["remote_sensing", "api_partner"],
 "identity_biometric": ["sensor_hardware", "web_scrape"],
 "distributed_sensing": ["crowd_sensor", "sensor_hardware"],
}

# A method is dropped in a country that cannot support it.
def method_feasible(method, c):
    net, inc = c["internet_band"], c["income_group"]
    if method in ("online_panel", "device_passive", "mobile_app", "crowd_task",
                  "expert_elicit", "crowd_sensor"):
        return net in ("high", "medium")   # contributors need connectivity to upload
    if method == "clinical_records":
        return inc in ("HIC", "UMIC")
    if method == "transaction":
        return inc in ("HIC", "UMIC") and net in ("high", "medium")
    return True   # face_to_face, telephone, web_scrape, api_partner, admin_records,
                  # remote_sensing, sensor_hardware, telecom_network, and the three
                  # methods that need no local infrastructure at all:
                  # environmental_sample, acoustic, signals_rf

# A domain is dropped where the infrastructure it is derived from does not exist.
def domain_feasible(domain, c, modality_primary):
    net, inc = c["internet_band"], c["income_group"]
    if domain in ("financial_transactions", "credit_risk"):
        return inc in ("HIC", "UMIC")
    if domain in ("device_telemetry", "mobility_location"):
        return net in ("high", "medium")
    if domain == "health_clinical" and modality_primary in ("clinical_records", "transaction"):
        return inc in ("HIC", "UMIC")   # record-derived health data needs digitised systems
    if domain == "prices_retail" and modality_primary == "transaction":
        return inc in ("HIC", "UMIC")
    return True

# Firms whose country footprint follows need rather than market size.
NEED_FIRMS = {"ipa_research", "jpal", "sixty_decibels", "geopoll", "flowminder",
              "premise_data", "commcare_dimagi", "surveycto", "kobotoolbox", "odk",
              "mwater", "ona", "acled", "bellingcat", "graphika"}

def priority_mode(company):
    if company["company_id"] in NEED_FIRMS:
        return "need"
    if company["segment_primary"] in ("ai_training_data", "crowd_micro"):
        return "labour"
    return "market"

def priority_score(c, mode):
    inc, pop, net = INCOME_W[c["income_group"]], POP_W[c["population_band"]], INTERNET_W[c["internet_band"]]
    conflict = int(c["conflict_affected"])
    if mode == "market":
        return 2 * inc + pop + 2 * net
    if mode == "labour":
        return pop + 2 * net + (5 - inc)
    if mode == "need":
        return pop + 2 * (5 - inc) + 3 * conflict + net
    raise ValueError(mode)

def split_list(x):
    return [] if x in ("NA", "", None) else [v.strip() for v in x.split("|")]

def main():
    companies = list(csv.DictReader(open("data/companies.csv")))
    countries = list(csv.DictReader(open("data/countries.csv")))
    spatial   = {r["company_id"]: r for r in csv.DictReader(open("data/coverage_spatial.csv"))}
    manual = collections.defaultdict(dict)
    man_scope = {}
    for r in csv.DictReader(open("data/coverage_country_manual.csv")):
        manual[r["company_id"]][r["iso3"]] = int(r["coverage"])
        man_scope[r["company_id"]] = r["scope"]

    by_region = collections.defaultdict(list)
    for c in countries:
        by_region[c["region_code"]].append(c)
    cty = {c["iso3"]: c for c in countries}
    regions = [r["region_code"] for r in csv.DictReader(open("data/regions.csv"))]

    out = []
    for co in companies:
        cid = co["company_id"]
        methods_all = sorted(set([co["modality_primary"]] +
                                 SEGMENT_METHODS.get(co["segment_primary"], []) +
                                 SEGMENT_METHODS.get(co["segment_secondary"], [])))
        domains_all = sorted(set(split_list(co["domains_primary"]) +
                                 split_list(co["domains_secondary"])))

        assigned = {}
        if cid in manual:
            assigned = {i: (s, "manual") for i, s in manual[cid].items()}
        if cid in manual and man_scope[cid] == "exhaustive":
            pass
        elif cid not in manual and co["spatial_scope"] == "single_country":
            assigned = {co["hq_country"]: (3, "hq_exact")}
        else:
            mode = priority_mode(co)
            scores = {r: int(spatial[cid][r]) for r in regions}
            live = {r: s for r, s in scores.items() if s > 0}
            # Weight by regional score AND region size, so budget is not spread
            # equally over a 48-country region and a 1-country region.
            wt = {r: (s ** 2) * len(by_region[r]) for r, s in live.items()}
            wsum = sum(wt.values()) or 1
            budget = min(int(co["countries_claimed"]), len(countries)) \
                     if co["countries_claimed"] != "NA" else 20
            budget = max(0, budget - len(assigned))   # hand-coded rows spend the budget first
            for r, s in (live.items() if budget else []):
                pool = sorted(by_region[r], key=lambda c: -priority_score(c, mode))
                n = max(1, min(len(pool), round(budget * wt[r] / wsum)))
                for k, c in enumerate(pool[:n]):
                    score = s if k / n < 0.5 else max(s - 1, 1)
                    assigned.setdefault(c["iso3"], (score, "allocated"))

        for iso, (score, basis) in sorted(assigned.items()):
            c = cty[iso]
            m = [x for x in methods_all if method_feasible(x, c)]
            d = [x for x in domains_all if domain_feasible(x, c, co["modality_primary"])]
            if basis == "allocated":
                if not m or not d:
                    continue  # a firm with no usable method or no obtainable data is not present
            else:
                # A hand-coded footprint is an observation that the firm operates
                # there, so it overrides the feasibility model rather than being
                # deleted by it. Impact-sourcing delivery centres are the clear
                # case: they supply their own connectivity regardless of the
                # national figure. Fall back to the firm's own primary method.
                m = m or [co["modality_primary"]]
                d = d or split_list(co["domains_primary"])[:1]
            out.append(dict(company_id=cid, iso3=iso, region_code=c["region_code"],
                            coverage=score, basis=basis,
                            n_methods=len(m), n_domains=len(d),
                            methods="|".join(m), domains="|".join(d)))

    fields = ["company_id","iso3","region_code","coverage","basis",
              "n_methods","n_domains","methods","domains"]
    with open("data/coverage_country.csv","w",newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields); w.writeheader(); w.writerows(out)

    b = collections.Counter(r["basis"] for r in out)
    print(f"wrote {len(out)} company-country rows covering "
          f"{len({r['iso3'] for r in out})} countries and "
          f"{len({r['company_id'] for r in out})} firms")
    print("  basis:", dict(b))
    return 0

if __name__ == "__main__":
    sys.exit(main())
