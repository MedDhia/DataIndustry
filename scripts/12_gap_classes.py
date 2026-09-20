#!/usr/bin/env python3
"""Separate three things the register had been calling by one name: a gap.

The register exists to find gaps in the data collection industry. Before this
script, a gap was whatever came out of grouping organisations by headquarters and
finding an empty cell. That conflates three different claims:

  presence gap   nobody collects there at all
  depth gap      somebody collects there, thinly
  ownership gap  somebody collects there, and nobody based there does

Only the first is a gap in the industry. The third is a gap in who owns the
capacity to know a place, which is a different and arguably more interesting
finding, and the second is a matter of degree. Reported separately here because
reporting them together produced claims that fell apart on the first test:
140 region-by-segment cells are empty by headquarters and 5 are empty by
coverage at any depth.

Coverage rows are 92% model output at a measured precision near 0.49
(`scripts/11_validate_allocation.py`), so read a presence count of 38 as
"clearly not zero" and never as "38".
"""
import csv, collections, sys

def main():
    rows = {r["company_id"]: r for r in csv.DictReader(open("data/companies.csv"))}
    op = {k for k, r in rows.items() if r["status"] in ("active", "acquired_active")}
    reg_of = {c["iso3"]: c["region_code"] for c in csv.DictReader(open("data/countries.csv"))}
    regions = [r["region_code"] for r in csv.DictReader(open("data/regions.csv"))]
    segs = sorted({rows[k]["segment_primary"] for k in op})

    pres = {t: collections.defaultdict(set) for t in (1, 2, 3)}
    for r in csv.DictReader(open("data/coverage_country.csv")):
        if r["company_id"] not in op:
            continue
        c, reg = int(r["coverage"]), reg_of[r["iso3"]]
        for t in (1, 2, 3):
            if c >= t:
                pres[t][reg].add(rows[r["company_id"]]["segment_primary"])

    print(f"{'region':7s} {'ownership':>10s} {'presence':>9s} {'thin':>6s} {'shallow':>8s}")
    print(f"{'':7s} {'(no HQ)':>10s} {'(cov>=1)':>9s} {'(>=2)':>6s} {'(>=3)':>8s}")
    tot = collections.Counter()
    for reg in regions:
        hq = {rows[k]["segment_primary"] for k in op if rows[k]["hq_region"] == reg}
        row = [len(set(segs) - hq)] + [len(set(segs) - pres[t][reg]) for t in (1, 2, 3)]
        for i, v in enumerate(row):
            tot[i] += v
        print(f"{reg:7s} {row[0]:10d} {row[1]:9d} {row[2]:6d} {row[3]:8d}")
    n = len(regions) * len(segs)
    print(f"{'TOTAL':7s} {tot[0]:10d} {tot[1]:9d} {tot[2]:6d} {tot[3]:8d}   of {n} region-segment cells")
    print(f"\n{tot[0]} apparent gaps by headquarters, {tot[1]} by presence. "
          f"{tot[0] - tot[1]} of them are ownership gaps, not industry gaps.")

    print("\nPRESENCE GAPS, the only ones that claim nobody collects:")
    any_left = False
    for reg in regions:
        m = sorted(set(segs) - pres[1][reg])
        if m:
            any_left = True
            print(f"  {reg}: {', '.join(m)}")
    if not any_left:
        print("  none")
    print("  Each surviving cell needs a falsification attempt before it is cited;"
          "\n  see data/gap_tests.csv for the ones already tried.")

    # The disclosure claim, which is the register's most cited, on both readings.
    disc = {k for k in op if rows[k]["microdata_access"] in ("open", "researcher_restricted")}
    fp = {k for k in op if rows[k]["sector"] == "for_profit"}
    bycov = collections.defaultdict(set)
    for r in csv.DictReader(open("data/coverage_country.csv")):
        if r["company_id"] in op and int(r["coverage"]) >= 1:
            bycov[reg_of[r["iso3"]]].add(r["company_id"])
    print("\nDISCLOSURE, by headquarters and by coverage:")
    print(f"{'region':7s} {'fp HQ':>6s} {'HQ disclosing':>14s} {'fp operating':>13s} {'operating disclosing':>21s}")
    for reg in regions:
        hq = {k for k in fp if rows[k]["hq_region"] == reg}
        print(f"{reg:7s} {len(hq):6d} {len(hq & disc):14d} {len(bycov[reg] & fp):13d} {len(bycov[reg] & fp & disc):21d}")
    return 0

if __name__ == "__main__":
    sys.exit(main())
