#!/usr/bin/env python3
"""Derive the `sector` variable in data/companies.csv.

`sector` answers one question: whose money is this and who does it answer to.
Four values, and every organisation gets exactly one.

  for_profit    trades commercially and distributes surplus to owners, whoever
                those owners are. A state-owned joint stock company selling
                research is for_profit here; `ownership_type` records that the
                state owns it.
  nonprofit     legally constituted not-for-profit, independent of government.
  academic      a university, a unit of one, or a research institute whose
                primary output is scholarship.
  governmental  an organ of the state, a body created by statute or decree and
                controlled by government, or an intergovernmental organisation.

`sector` and `ownership_type` are deliberately not redundant. `ownership_type`
says who holds the equity; `sector` says what kind of organisation it is. The
two come apart for state-owned commercial firms (VCIOM, Elm, Chang Guang) and
for joint industry committees.

Derivation is a rule on `ownership_type` plus an explicit override list, so the
judgement calls are visible and rerunnable rather than hand-entered.
"""
import csv, sys, collections

# Default mapping. Applies unless the company_id appears in OVERRIDE.
BY_OWNERSHIP = {
    "public_listed":       "for_profit",
    "private_pe":          "for_profit",
    "private_vc":          "for_profit",
    "private_independent": "for_profit",
    "subsidiary":          "for_profit",
    "nonprofit":           "nonprofit",
    "academic":            "academic",
    "state_linked":        "governmental",
    # Joint industry committees are broadcaster- and advertiser-owned bodies
    # constituted not to distribute profit. They sell nothing on the open market
    # and exist to produce a currency their members trade on.
    "cooperative_jic":     "nonprofit",
}

# Cases where ownership does not determine sector. Each carries its reason.
OVERRIDE = {
    # State-owned but commercially trading: they sell research or imagery on the
    # open market and are run as businesses.
    "vciom":         ("for_profit",   "state-owned joint stock company selling research commercially"),
    "mediascope":    ("for_profit",   "commercial audience measurement monopolist, majority held by VCIOM"),
    "sberindex":     ("for_profit",   "analytics product of a listed commercial bank"),
    "ctr_china":     ("for_profit",   "joint venture between CCTV and Kantar, trading commercially"),
    "csm_media":     ("for_profit",   "joint venture of CTR and Kantar Media, trading commercially"),
    "changguang":    ("for_profit",   "commercial satellite operator, state-backed but selling imagery"),
    "twentyone_at":  ("for_profit",   "commercial satellite imagery operator"),
    "elm_saudi":     ("for_profit",   "joint stock company listed on the Saudi exchange, PIF-owned"),
    "m42":           ("for_profit",   "commercial health group under G42 and Mubadala"),
    # State-tied but constituted as an independent foundation.
    "fom_russia":    ("nonprofit",    "registered foundation, politically tied but not an organ of state"),
    # State-linked academic bodies.
    "ispa_iran":     ("academic",     "run under the Academic Center for Education Culture and Research"),
    "cread_algeria": ("academic",     "public research centre, scholarly output"),
    # Nonprofit and academic bodies coded state_linked because of their founder
    # or funder, but which are organs of government in substance.
    "aecb":          ("governmental", "federal credit bureau established by UAE law"),
    # A company whose acquirer is a nonprofit, but which operated as a listed
    # for-profit for its entire collecting life.
    "twentythreeandme": ("for_profit", "operated as a listed for-profit; the nonprofit acquirer came after bankruptcy"),
}


def main():
    path = "data/companies.csv"
    rows = list(csv.DictReader(open(path)))
    fields = list(rows[0].keys())
    if "sector" not in fields:
        fields.insert(fields.index("ownership_type") + 1, "sector")

    reasons = {}
    for r in rows:
        cid = r["company_id"]
        if cid in OVERRIDE:
            r["sector"], why = OVERRIDE[cid]
            reasons[cid] = why
        else:
            r["sector"] = BY_OWNERSHIP[r["ownership_type"]]

    with open(path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)

    counts = collections.Counter(r["sector"] for r in rows)
    print(f"coded {len(rows)} organisations")
    for k, v in counts.most_common():
        print(f"  {k:<14} {v:>4}  ({100*v/len(rows):.1f}%)")
    print(f"  {len(OVERRIDE)} overrides applied, listed in this script with reasons")

    # Cross-tabulate so the non-redundancy is visible.
    print("\nsector by ownership_type:")
    ct = collections.Counter((r["ownership_type"], r["sector"]) for r in rows)
    for (own, sec), n in sorted(ct.items()):
        print(f"  {own:<22} {sec:<14} {n:>4}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
