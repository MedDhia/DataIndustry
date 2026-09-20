#!/usr/bin/env python3
"""The gaps that survive testing, ranked by how much enumeration could move them.

After `12_gap_classes.py` separated ownership from presence and `gap_tests.csv`
recorded the falsification attempts, four candidate gaps remain. They are not
equally solid, and the axis that matters is whether finding more organisations
would shrink them.

  A gap robust to enumeration is a statement about the terms on which the
  industry operates. Adding firms cannot close it, because new firms arrive on
  the same terms.

  A gap bounded by enumeration is a statement about this register. Adding firms
  can close it, so it is a hypothesis with a search attached.

Both are reported. Only the first should be called a finding without a caveat.
"""
import csv, collections, sys

ACCESSIBLE = ("open", "researcher_restricted")

def main():
    rows = {r["company_id"]: r for r in csv.DictReader(open("data/companies.csv"))}
    op = {k for k, r in rows.items() if r["status"] in ("active", "acquired_active")}
    ctys = {c["iso3"]: c for c in csv.DictReader(open("data/countries.csv"))}
    doms = [d["domain_code"] for d in csv.DictReader(open("data/domains.csv"))]

    prov = collections.defaultdict(set); acc = collections.defaultdict(set)
    strong = collections.defaultdict(set); domestic = collections.defaultdict(set)
    for r in csv.DictReader(open("data/coverage_country.csv")):
        cid = r["company_id"]
        if cid not in op or int(r["coverage"]) < 1:
            continue
        co = rows[cid]; iso = r["iso3"]
        if int(r["coverage"]) >= 2:
            strong[iso].add(cid)
            if co["hq_country"] == iso and co["sector"] in ("for_profit", "nonprofit", "academic"):
                domestic[iso].add(cid)
        for d in filter(None, r["domains"].split("|")):
            prov[(iso, d)].add(cid)
            if co["microdata_access"] in ACCESSIBLE:
                acc[(iso, d)].add(cid)

    cells = [k for k in prov if prov[k]]
    noacc = [k for k in cells if not acc[k]]
    print("GAP 1  Terms of access. ROBUST to enumeration.")
    print(f"  {len(noacc)} of {len(cells)} country-domain cells have a provider and none a "
          f"researcher can obtain data from ({len(noacc)/len(cells)*100:.0f}%).")
    by = collections.Counter(d for _, d in noacc)
    for d, n in by.most_common(6):
        tot = sum(1 for k in cells if k[1] == d)
        print(f"    {d:24s} {n:4d} of {tot:4d} cells closed")
    shut = [d for d in doms if sum(1 for k in cells if k[1] == d) and
            not any(acc[k] for k in cells if k[1] == d)]
    print(f"  Domains with no accessible provider anywhere on earth: {shut or 'none'}")
    print("  Adding organisations cannot close this: new firms arrive on the same terms.\n")

    nodom = sorted(i for i in ctys if not domestic[i] and strong[i])
    print("GAP 2  Domestic capacity. BOUNDED by enumeration.")
    print(f"  {len(nodom)} of 194 countries have substantial coverage and no organisation "
          f"based there providing it.")
    reg = collections.Counter(ctys[i]["region_code"] for i in nodom)
    print("   ", dict(reg.most_common()))
    thin = sorted(((len(domestic[i]), len(strong[i]), i) for i in ctys if strong[i]))[:8]
    print("  Thinnest: " + ", ".join(f"{i} {d} domestic of {s}" for d, s, i in thin))
    print("  Four of these were taken to a search and none produced a domestic collector;"
          "\n  see gap_tests.csv. More enumeration can only shrink this number.\n")

    empty = [(i, d) for i in ctys for d in doms if not prov[(i, d)]]
    print("GAP 3  Absence. BOUNDED by enumeration, and mostly already broken.")
    print(f"  {len(empty)} of {len(ctys)*len(doms)} country-domain cells have no provider at all.")
    print("   ", dict(collections.Counter(d for _, d in empty).most_common(5)))
    print("   ", dict(collections.Counter(i for i, _ in empty).most_common(6)))
    print("  Was 297 before the feasibility gate was rebuilt on observation rather than"
          "\n  on income. Read every remaining cell as untested unless gap_tests.csv says otherwise.\n")

    single = [(i, d, next(iter(prov[(i, d)]))) for i in ctys for d in doms
              if len(prov[(i, d)]) == 1]
    print("GAP 4  Single-provider dependency. FRAGILE evidence.")
    print(f"  {len(single)} country-domain cells rest on one organisation.")
    print("   ", dict(collections.Counter(c for _, _, c in single).most_common(5)))
    print("  Coverage rows are 92% modelled at precision near 0.49, so treat a count of one"
          "\n  as a hypothesis about concentration, not as a fact about a country.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
