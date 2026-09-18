#!/usr/bin/env python3
"""Screen candidate organisations against the register before adding them.

Written after the same mistake twice. A plain substring test on the name column
misses a firm the register holds under a different spelling: SatVu is in as
"Satellite Vu", SBM Intelligence as "SB Morgen Intelligence". Both were reported
absent and both were already there. The first was caught by an insert assertion,
the second by the same assertion a round later.

    python3 scripts/00_check_new.py "SatVu" "SB Morgen" "Some New Firm"

Reports, for every candidate: exact id hits, substring hits either way, and any
register row sharing a significant word with it. Nothing is flagged as safe to
add; the point is to put the near-misses in front of the coder's eyes.
"""
import csv, re, sys

STOP = {"the", "and", "group", "ltd", "limited", "inc", "llc", "corp", "corporation",
        "company", "co", "technologies", "technology", "tech", "solutions", "systems",
        "international", "global", "labs", "lab", "ai", "data", "research", "institute",
        "africa", "african", "intelligence", "analytics", "digital", "plc", "sa", "gmbh"}

def toks(s):
    return {w for w in re.split(r"[^a-z0-9]+", s.lower()) if len(w) > 2 and w not in STOP}

def main(cands):
    rows = list(csv.DictReader(open("data/companies.csv")))
    if not cands:
        print(__doc__)
        return 1
    worst = 0
    for c in cands:
        ct, cl = toks(c), c.lower()
        hits = []
        for r in rows:
            nid, nm = r["company_id"], r["company_name"]
            if nid == cl.replace(" ", "_") or cl == nm.lower():
                hits.append(("EXACT", nid, nm))
            elif cl in nm.lower() or nm.lower() in cl or cl in nid:
                hits.append(("substring", nid, nm))
            elif ct & toks(nm):
                hits.append(("shared word: " + ",".join(sorted(ct & toks(nm))), nid, nm))
        if hits:
            worst = max(worst, 2 if any(h[0] == "EXACT" for h in hits) else 1)
            print(f"\n{c}")
            # Severity first, then file order. The first version printed in file
            # order and truncated at six, so an EXACT match sitting behind a run
            # of shared-word noise never reached the screen: that is how a second
            # Ifakara Health Institute row was created. Exact and substring hits
            # are now always printed in full.
            rank = {"EXACT": 0}
            hits.sort(key=lambda h: rank.get(h[0], 1 if h[0] == "substring" else 2))
            hard = [h for h in hits if h[0] in ("EXACT", "substring")]
            for kind, nid, nm in hard + [h for h in hits if h not in hard][:4]:
                print(f"    {kind:28s} {nid} / {nm}")
        else:
            print(f"\n{c}\n    no match in {len(rows)} rows")
    return worst

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
