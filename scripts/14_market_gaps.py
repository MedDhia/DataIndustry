#!/usr/bin/env python3
"""Market white space: where documented demand meets thin or absent supply.

A different question from the one `13_real_gaps.py` answers. That script asks
where data is not being collected. This one asks where a venture could enter,
which needs demand on one side and few incumbents on the other.

What the register can support:
  - counts of incumbents by segment, region and headquarters
  - documented demand direction from data/demand.csv
  - entry and exit rates, so a thin segment can be told from a dying one
  - the terms every incumbent sells on, which is where business-model space is
  - methods proven in one place and used by nobody in another
  - open funding programmes a new venture could actually apply to

What it cannot support, and no output here should be read as: market size,
revenue, margin, willingness to pay, or competitive intensity beyond a count of
firms. There is no revenue variable in this register and there will not be one.
A gap here means thin supply against documented demand. It is a place to look,
not a business case.
"""
import csv, collections, sys

EXIT = {"absorbed", "wound_down", "insolvent"}

def main():
    rows = list(csv.DictReader(open("data/companies.csv")))
    op = [r for r in rows if r["status"] in ("active", "acquired_active")]
    dem = list(csv.DictReader(open("data/demand.csv")))
    inn = {r["company_id"] for r in csv.DictReader(open("data/method_innovations.csv"))}
    seg_dir = collections.defaultdict(set)
    for d in dem:
        seg_dir[d["segment"]].add(d["direction"])

    print("1. BUSINESS MODEL WHITE SPACE")
    print("   Segments where no incumbent, or one, offers a researcher any route to")
    print("   record-level data. An entrant selling on different terms has no rival"
          "\n   on that axis, and the regulated buyers in demand.csv need provenance.\n")
    print(f"   {'segment':24s} {'firms':>5s} {'accessible':>11s} {'self':>5s}  demand")
    for seg in sorted({r["segment_primary"] for r in op}):
        g = [r for r in op if r["segment_primary"] == seg]
        a = [r for r in g if r["microdata_access"] in ("open", "researcher_restricted")]
        s = [r for r in g if r["disclosure_route"] == "self"]
        if len(a) <= 1 and len(g) >= 6:
            print(f"   {seg:24s} {len(g):5d} {len(a):11d} {len(s):5d}  {','.join(sorted(seg_dir[seg])) or '-'}")

    print("\n2. METHOD TRANSFER")
    print("   A collection method operating commercially elsewhere that nobody based")
    print("   in the region uses. Named proof cases, so the question is transfer and"
          "\n   not invention.\n")
    for reg in ("MENA", "SSA"):
        have = {r["modality_primary"] for r in op if r["hq_region"] == reg}
        counts = collections.Counter(r["modality_primary"] for r in op)
        print(f"   -- {reg}")
        for m, n in counts.most_common():
            if m in have:
                continue
            users = [r for r in op if r["modality_primary"] == m]
            proof = [u for u in users if u["company_id"] in inn] or users
            names = ", ".join(f"{u['company_name']} ({u['hq_country']})" for u in proof[:3])
            print(f"      {m:20s} {n:3d} worldwide  {names}")

    print("\n3. RISING DEMAND, THIN DOMESTIC SUPPLY")
    print("   Segments with a demand row coded rising, ranked by how few organisations"
          "\n   are based in the region to serve it.\n")
    for reg in ("MENA", "SSA"):
        segs = {d["segment"] for d in dem if d["direction"] == "rising"
                and d["geography"] in (reg, "global")}
        out = []
        for s in segs:
            dom = [r for r in op if r["segment_primary"] == s and r["hq_region"] == reg]
            out.append((len([r for r in dom if r["sector"] == "for_profit"]), len(dom), s,
                        sum(1 for r in op if r["segment_primary"] == s)))
        print(f"   -- {reg}")
        for fp, dom, s, world in sorted(out)[:6]:
            print(f"      {s:24s} domestic for-profit {fp:2d}, any {dom:2d}, worldwide {world:3d}")

    print("\n4. VACATED SEGMENTS")
    print("   High exit, low entry. Read with column 1: the segments incumbents are")
    print("   leaving are largely the same ones that sell on closed terms, which is"
          "\n   an argument for entering differently rather than for entering at all.\n")
    for seg in sorted({r["segment_primary"] for r in rows}):
        g = [r for r in rows if r["segment_primary"] == seg]
        if len(g) < 8:
            continue
        ex = sum(1 for r in g if r["status"] in EXIT)
        dated = [int(r["founded_year"]) for r in g if r["founded_year"].isdigit()]
        recent = sum(1 for y in dated if y >= 2015) / len(dated) if dated else 0
        if ex / len(g) >= 0.14 and recent < 0.35:
            print(f"   {seg:24s} n={len(g):3d} exits {ex:2d} ({ex/len(g)*100:4.1f}%) "
                  f"founded since 2015 {recent*100:3.0f}%  demand={','.join(sorted(seg_dir[seg]))}")

    print("\n5. CAPITAL AVAILABLE FOR THESE REGIONS")
    n = 0
    for p in csv.DictReader(open("data/grant_programmes.csv")):
        if p["status"] == "open" and set(p["eligible_regions"].split("|")) & {"SSA", "MENA"}:
            n += 1
            if p["data_specific"] in ("yes", "partial"):
                print(f"   {p['programme_name'][:36]:38s} {p['award_min_usd']:>7s}-{p['award_max_usd']:<8s} "
                      f"{p['eligible_regions']}")
    print(f"   {n} open programmes admit MENA or African applicants; those printed are data-specific.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
