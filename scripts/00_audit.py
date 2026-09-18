#!/usr/bin/env python3
"""Cross-field consistency probes over companies.csv. Reports, never edits.

This is not the validator. `00_validate.py` holds rules that are always errors
and exits non-zero on any of them. This file holds probes for combinations that
are *usually* wrong, which means most of what it prints will be legitimate and
the reader has to judge each one.

That distinction was learned the expensive way. The first version of this audit
raised 122 flags over 934 rows and roughly a dozen were real. The rest were the
probe being cruder than the register: a firm can recruit a consented cohort and
also ingest clinical records, so `human_subjects=direct` with a records-based
modality is not a contradiction; a private-equity-owned firm names its owner as
`parent_company` without being a subsidiary; radio frequency geolocation is an
earth observation business without being remote sensing. Those probes are
narrowed here to the cases where no such reading exists.

What the first run did find, and what this file exists to find again: a second
Ifakara Health Institute row under a different identifier, four organisations
whose consent code predated the vocabulary value that describes them, and three
scope fields contradicting their own country counts. Rules that the register now
satisfies completely have been promoted into the validator.

Run it after any extension round:  python3 scripts/00_audit.py
"""
import csv, collections, sys

# Modalities that cannot put the firm in front of the person. Records, feeds and
# sensors are excluded on purpose: a cohort study consents its participants and
# then collects their records, and that is one organisation doing both.
NO_CONTACT_POSSIBLE = {"remote_sensing", "web_scrape", "admin_records", "signals_rf",
                       "fiber_das", "acoustic", "environmental_sample", "telecom_network"}
# Modalities where the person IS the subject, as opposed to the worker. Crowd
# tasking and expert elicitation are excluded: annotators and experts are
# producing the data, not being measured by it.
SUBJECT_FACING = {"face_to_face", "telephone", "online_panel", "web_intercept"}

def main():
    rows = list(csv.DictReader(open("data/companies.csv")))
    n = lambda v: int(v) if v.isdigit() else None
    F = collections.defaultdict(list)

    for r in rows:
        cid, m = r["company_id"], r["modality_primary"]
        fy, cc = n(r["founded_year"]), n(r["countries_claimed"])

        if r["human_subjects"] == "direct" and m in NO_CONTACT_POSSIBLE:
            F["direct contact through an instrument that cannot make it"].append((cid, m))
        if r["human_subjects"] == "none" and m in SUBJECT_FACING:
            F["no human subject, but the instrument asks people questions"].append((cid, m))
        if r["consent_model"] == "explicit_consent" and r["human_subjects"] == "none":
            F["explicit consent obtained from nobody"].append((cid, m))
        # The odd case is a listed company with a parent. PE and VC owners are
        # routinely recorded as the parent and that is not a contradiction.
        if r["parent_company"] != "NA" and r["ownership_type"] == "public_listed":
            F["listed company with a parent recorded"].append((cid, r["parent_company"]))
        if fy and r["maturity_class"] == "established" and fy >= 2018:
            F["established but founded 2018 or later"].append((cid, fy))
        if fy and r["maturity_class"] == "startup" and fy <= 2010:
            F["startup but founded 2010 or earlier"].append((cid, fy))
        if r["spatial_scope"] == "global" and cc is not None and cc < 30:
            F["global scope on fewer than 30 countries"].append((cid, cc))
        if r["spatial_scope"] == "multi_region" and cc is not None and cc < 2:
            F["multi region on fewer than two countries"].append((cid, cc))
        if r["microdata_access"] == "open" and r["access_model"] in ("subscription", "api_license",
                                                                    "marketplace", "panel_rental"):
            F["open microdata behind a paid access model"].append((cid, r["access_model"]))
        if r["access_model"] == "open_free" and r["microdata_access"] == "commercial_only":
            F["free access but commercial-only microdata"].append(cid)
        if r["sector"] == "governmental" and r["ownership_type"] not in ("state_linked", "nonprofit", "academic"):
            F["governmental sector, non-state ownership"].append((cid, r["ownership_type"]))
        if r["segment_primary"] == "field_agency" and m in ("web_scrape", "remote_sensing", "api_partner"):
            F["field agency that does no fieldwork"].append((cid, m))

    # Near-duplicate names: exact duplicates are a validator error, so anything
    # here is a pair that differs by punctuation, a suffix or a word.
    def key(s):
        return "".join(ch for ch in s.lower() if ch.isalnum())
    by = collections.defaultdict(list)
    for r in rows:
        by[key(r["company_name"])].append(r["company_id"])
    for k, ids in by.items():
        if len(ids) > 1:
            F["names identical once punctuation is stripped"].append(tuple(ids))

    total = 0
    for k, v in sorted(F.items(), key=lambda x: -len(x[1])):
        total += len(v)
        print(f"\n{k}: {len(v)}")
        for x in v[:15]:
            print("   ", x)
        if len(v) > 15:
            print(f"    ... and {len(v) - 15} more")
    print(f"\n{total} flags over {len(rows)} rows. Every one needs a human reading;"
          f"\nthis file has no opinion about which are errors.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
