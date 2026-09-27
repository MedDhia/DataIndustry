#!/usr/bin/env python3
"""Type-of-data gaps: what buyers ask for versus what the supply base produces.

`14_market_gaps.py` asks which segments and regions are thinly served. This
asks a different question: holding the segment fixed, what *kind* of data is
demanded and not produced. A data type here is the combination of four coded
properties of a supplier's output:

  unit_of_observation   what one row is
  temporal_granularity  how often that row is refreshed
  spatial_scope         how far the same instrument reaches
  microdata_access      whether anyone outside the buyer can see a record

A type gap is a combination of those properties that buyers in data/demand.csv
ask for and few or no organisations produce. That is a stronger claim than a
thin segment, because it survives the observation that somebody already sells
in the segment: they sell a different type.

Limits. The register codes one unit, one granularity and one scope per
organisation, so a firm producing two types is represented by its main one, and
every count below is therefore a lower bound on type diversity. There is no
variable for how far back a series runs, so nothing here speaks to historical
depth. No revenue variable exists, so nothing here is a market size.
"""
import csv, collections, itertools

ACTIVE = ("active", "acquired_active")
ACCESSIBLE = {"open", "researcher_restricted"}
UNITS = ["individual", "household", "patient", "firm", "place", "area",
         "device", "vehicle", "transaction", "document", "housing_unit"]
GRAN = ["real_time", "daily", "weekly", "monthly", "quarterly", "annual", "episodic"]
SCOPE = ["single_country", "single_region", "multi_region", "global"]
FAST = {"real_time", "daily", "weekly"}


def domains(r):
    raw = r["domains_primary"] + "|" + r["domains_secondary"]
    return {d.strip() for d in raw.split("|") if d.strip() and d.strip() != "NA"}


def main():
    rows = [r for r in csv.DictReader(open("data/companies.csv"))
            if r["status"] in ACTIVE]
    dem = list(csv.DictReader(open("data/demand.csv")))
    doms = sorted({d for r in rows for d in domains(r)})

    print("1. UNIT MISMATCH: demanded about an asset, produced about an area")
    print("   Buyers in demand.csv name the unit they need. Underwriters ask for")
    print("   asset level physical risk; disclosure rules ask about a company;")
    print("   due diligence rules ask about a worker. Supply is counted by the")
    print("   unit each organisation actually publishes.\n")
    du = collections.Counter()
    dtot = collections.Counter()
    for r in rows:
        for d in domains(r):
            du[(d, r["unit_of_observation"])] += 1
            dtot[d] += 1
    watch = [("environment_climate", ("firm", "housing_unit", "place"), "area"),
             ("supply_chain", ("individual", "household"), "vehicle"),
             ("agriculture", ("firm", "place"), "area"),
             ("infrastructure", ("individual", "household"), "area"),
             ("energy_extractives", ("individual", "household"), "area"),
             ("biodiversity", ("place",), "area")]
    print(f"   {'domain':24s} {'firms':>5s} {'asked-for unit':>14s} {'supplied at':>12s}")
    for d, want, have in watch:
        w = sum(du[(d, u)] for u in want)
        print(f"   {d:24s} {dtot[d]:5d} {w:14d} {du[(d, have)]:12d}   ({'+'.join(want)} vs {have})")

    print("\n   Empty cells in the full domain by unit matrix: "
          f"{sum(1 for d in doms for u in UNITS if du[(d, u)] == 0)} of {len(doms) * len(UNITS)}.")
    print("   Most are not markets. The six above are, because a demand row names the unit.")

    print("\n2. FREQUENCY MISMATCH: the register's fast data is not about people")
    print("   Share of each unit's suppliers refreshing weekly or faster.\n")
    ut = collections.Counter(r["unit_of_observation"] for r in rows)
    uf = collections.Counter(r["unit_of_observation"] for r in rows
                             if r["temporal_granularity"] in FAST)
    urt = collections.Counter(r["unit_of_observation"] for r in rows
                              if r["temporal_granularity"] == "real_time")
    print(f"   {'unit':14s} {'n':>4s} {'weekly+':>8s} {'real time':>10s}")
    for u in sorted(UNITS, key=lambda x: -(uf[x] / ut[x] if ut[x] else 0)):
        if not ut[u]:
            continue
        print(f"   {u:14s} {ut[u]:4d} {100 * uf[u] / ut[u]:7.0f}% {urt[u]:10d}")
    print("\n   By domain, the slowest supply against a rising or policy driven buyer:\n")
    dg = collections.Counter()
    for r in rows:
        for d in domains(r):
            if r["temporal_granularity"] in FAST:
                dg[d] += 1
    for d in sorted(doms, key=lambda x: dg[x] / dtot[x]):
        if dtot[d] >= 30 and dg[d] / dtot[d] < 0.35:
            print(f"   {d:24s} {dtot[d]:4d} firms, {100 * dg[d] / dtot[d]:3.0f}% weekly or faster")

    print("\n3. TERMS BY TYPE: which units of observation are readable at all")
    print("   Share of each unit's suppliers offering any route to a record.\n")
    ua = collections.Counter(r["unit_of_observation"] for r in rows
                             if r["microdata_access"] in ACCESSIBLE)
    print(f"   {'unit':14s} {'accessible':>10s} {'n':>5s} {'share':>7s}")
    for u in sorted(UNITS, key=lambda x: -(ua[x] / ut[x] if ut[x] else 0)):
        if not ut[u]:
            continue
        print(f"   {u:14s} {ua[u]:10d} {ut[u]:5d} {100 * ua[u] / ut[u]:6.0f}%")

    print("\n4. LINKAGE: types that exist only as two separate files")
    print("   Domain pairs held by no single organisation, where a demand row")
    print("   needs them joined. The join is the product that does not exist.\n")
    pairs = collections.Counter()
    for r in rows:
        for a, b in itertools.combinations(sorted(domains(r)), 2):
            pairs[(a, b)] += 1
    never = [(a, b) for a, b in itertools.combinations(doms, 2) if not pairs[(a, b)]]
    print(f"   {len(never)} of {len(doms) * (len(doms) - 1) // 2} domain pairs never co-occur.")
    named = [("labor_employment", "supply_chain"),
             ("environment_climate", "firmographic"),
             ("health_clinical", "supply_chain"),
             ("migration_displacement", "prices_retail"),
             ("credit_risk", "mobility_location"),
             ("agriculture", "firmographic")]
    print(f"\n   {'pair':50s} {'firms a':>8s} {'firms b':>8s} {'joined':>7s}")
    for a, b in named:
        print(f"   {a + ' x ' + b:50s} {dtot[a]:8d} {dtot[b]:8d} {pairs[(min(a, b), max(a, b))]:7d}")
    lonely = sorted(doms, key=lambda d: sum(1 for x in doms
                                            if x != d and pairs[(min(d, x), max(d, x))]))
    print("\n   Domains linked to the fewest others (of 26 possible partners):")
    for d in lonely[:6]:
        n = sum(1 for x in doms if x != d and pairs[(min(d, x), max(d, x))])
        print(f"   {d:24s} {dtot[d]:4d} firms, linked to {n:2d}")

    print("\n5. BORDER MISMATCH: phenomena that cross borders, instruments that do not")
    print("   Share of each domain's suppliers operating in one country only.\n")
    ds = collections.Counter()
    for r in rows:
        for d in domains(r):
            ds[(d, r["spatial_scope"])] += 1
    print(f"   {'domain':24s} {'n':>4s} {'1 country':>10s} {'global':>7s}")
    for d in sorted(doms, key=lambda x: -(ds[(x, 'single_country')] / dtot[x])):
        if dtot[d] >= 30 and ds[(d, "single_country")] / dtot[d] > 0.33:
            print(f"   {d:24s} {dtot[d]:4d} {100 * ds[(d, 'single_country')] / dtot[d]:9.0f}%"
                  f" {ds[(d, 'global')]:7d}")

    print("\n6. TYPES ALREADY SUPPLIED, so not an opening")
    print("   Demand rows name these types and the supply exists, including in")
    print("   MENA and Africa. Listed so the analysis can be falsified.\n")
    reg = collections.Counter
    checks = [("patient level clinical records",
               lambda r: r["unit_of_observation"] == "patient"),
              ("vessel and vehicle level positioning",
               lambda r: r["unit_of_observation"] == "vehicle"),
              ("document level labelled text",
               lambda r: "ai_labels" in domains(r) and r["unit_of_observation"] == "document"),
              ("transaction level credit history",
               lambda r: "credit_risk" in domains(r))]
    for label, test in checks:
        sub = [r for r in rows if test(r)]
        by = reg(r["hq_region"] for r in sub)
        acc = sum(1 for r in sub if r["microdata_access"] in ACCESSIBLE)
        print(f"   {label:36s} n={len(sub):3d}  accessible={acc:3d}  "
              f"MENA={by['MENA']} SSA={by['SSA']} NOAM={by['NOAM']} WEU={by['WEU']}")


if __name__ == "__main__":
    main()
