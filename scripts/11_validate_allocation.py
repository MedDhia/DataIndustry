#!/usr/bin/env python3
"""Held-out test of the country allocation rule against observed footprints.

92% of `data/coverage_country.csv` is `allocated`: the rule's guess at where a
firm operates, not an observation. Until now nothing said how good that guess is.

138 firms in `coverage_country_manual.csv` carry a footprint marked `exhaustive`,
meaning the hand-coded country list is complete. That is ground truth. This
script hides each of those footprints in turn, runs the allocation rule on the
firm as if nothing were known about it beyond its region scores and country
budget, and compares the predicted country set with the observed one.

Reported per firm and in aggregate:
  precision  share of predicted countries that the firm really operates in
  recall     share of real countries the rule predicted
  jaccard    overlap over union, which punishes both errors at once

The comparison is generous to the rule in one way and harsh in another. Generous
because the firm's `countries_claimed` budget is itself often taken from the same
source as the manual list, so the rule is told how many countries to pick.
Harsh because an exhaustive manual footprint is most often coded for firms with
unusual footprints, which is exactly where a rule trained on income, population
and connectivity should do worst. Read the number as a bound, not a score.
"""
import csv, collections, sys, importlib.util

spec = importlib.util.spec_from_file_location("bld", "scripts/00_build_country_coverage.py")
bld = importlib.util.module_from_spec(spec); spec.loader.exec_module(bld)

def main():
    companies = {r["company_id"]: r for r in csv.DictReader(open("data/companies.csv"))}
    countries = list(csv.DictReader(open("data/countries.csv")))
    spatial = {r["company_id"]: r for r in csv.DictReader(open("data/coverage_spatial.csv"))}
    regions = [r["region_code"] for r in csv.DictReader(open("data/regions.csv"))]
    by_region = collections.defaultdict(list)
    for c in countries:
        by_region[c["region_code"]].append(c)

    truth, scope = collections.defaultdict(set), {}
    for r in csv.DictReader(open("data/coverage_country_manual.csv")):
        truth[r["company_id"]].add(r["iso3"])
        scope[r["company_id"]] = r["scope"]

    rows, skipped = [], 0
    for cid, obs in truth.items():
        if scope[cid] != "exhaustive" or cid not in companies or cid not in spatial:
            skipped += 1
            continue
        co = companies[cid]
        mode = bld.priority_mode(co)
        scores = {r: int(spatial[cid][r]) for r in regions}
        live = {r: s for r, s in scores.items() if s > 0}
        if not live:
            skipped += 1
            continue
        wt = {r: (s ** 2) * len(by_region[r]) for r, s in live.items()}
        wsum = sum(wt.values()) or 1
        budget = min(int(co["countries_claimed"]), len(countries)) \
                 if co["countries_claimed"] != "NA" else 20
        pred = set()
        for r, s in live.items():
            pool = sorted(by_region[r],
                          key=lambda c: -(bld.priority_score(c, mode) +
                                          (1e6 if c["iso3"] == co["hq_country"] else 0)))
            n = max(1, min(len(pool), round(budget * wt[r] / wsum)))
            pred.update(c["iso3"] for c in pool[:n])
        hit = pred & obs
        rows.append(dict(company_id=cid, segment=co["segment_primary"],
                         n_true=len(obs), n_pred=len(pred), n_hit=len(hit),
                         precision=round(len(hit) / len(pred), 3) if pred else 0.0,
                         recall=round(len(hit) / len(obs), 3),
                         jaccard=round(len(hit) / len(pred | obs), 3)))

    rows.sort(key=lambda r: r["jaccard"])
    tp = sum(r["n_hit"] for r in rows)
    print(f"held-out firms: {len(rows)} (skipped {skipped}: partial footprints or no region score)")
    print(f"cells: {sum(r['n_pred'] for r in rows)} predicted, {sum(r['n_true'] for r in rows)} observed, {tp} correct")
    print(f"micro precision {tp / max(1, sum(r['n_pred'] for r in rows)):.3f}  "
          f"micro recall {tp / max(1, sum(r['n_true'] for r in rows)):.3f}")
    n = len(rows) or 1
    print(f"macro precision {sum(r['precision'] for r in rows) / n:.3f}  "
          f"macro recall {sum(r['recall'] for r in rows) / n:.3f}  "
          f"macro jaccard {sum(r['jaccard'] for r in rows) / n:.3f}")

    print("\nby firm size of true footprint:")
    for lo, hi in ((1, 3), (4, 10), (11, 30), (31, 250)):
        g = [r for r in rows if lo <= r["n_true"] <= hi]
        if g:
            print(f"  {lo:3d}-{hi:3d} countries  n={len(g):3d}  "
                  f"precision {sum(r['precision'] for r in g)/len(g):.3f}  "
                  f"recall {sum(r['recall'] for r in g)/len(g):.3f}")

    print("\nworst ten firms by overlap:")
    for r in rows[:10]:
        print(f"  {r['company_id']:24s} {r['segment'][:18]:20s} true {r['n_true']:3d} pred {r['n_pred']:3d} "
              f"hit {r['n_hit']:3d}  jaccard {r['jaccard']:.2f}")

    with open("output/allocation_validation.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
    print("\nwrote output/allocation_validation.csv")
    return 0

if __name__ == "__main__":
    sys.exit(main())
