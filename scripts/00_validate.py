#!/usr/bin/env python3
"""Validate data/companies.csv against the lookup tables and controlled vocabularies.

Exits non-zero and prints every offending record if anything fails, so this can
be run as a pre-commit check when the register is extended.
"""
import csv, collections, sys

VOCAB = {
 "maturity_class": {"established", "scaleup", "startup"},
 "ownership_type": {"public_listed", "private_pe", "private_vc", "private_independent",
                    "subsidiary", "nonprofit", "academic", "state_linked", "cooperative_jic"},
 "status": {"active", "acquired_active", "wound_down", "insolvent"},
 "spatial_scope": {"global", "multi_region", "single_region", "single_country"},
 "human_subjects": {"direct", "indirect", "none"},
 "consent_model": {"explicit_consent", "platform_terms", "contractual_third_party",
                   "public_record", "not_applicable"},
 "access_model": {"project_commission", "subscription", "api_license", "marketplace",
                  "panel_rental", "open_free"},
 "microdata_access": {"open", "researcher_restricted", "commercial_only", "none"},
 "evidence_level": {"A", "B", "C"},
 "temporal_granularity": {"real_time", "daily", "weekly", "monthly", "quarterly",
                          "annual", "episodic"},
 "unit_of_observation": {"individual", "household", "device", "firm", "place",
                         "transaction", "document", "area", "patient", "vehicle",
                         "housing_unit"},
}

def col(path, field):
    return {r[field] for r in csv.DictReader(open(path))}

def main():
    companies = list(csv.DictReader(open("data/companies.csv")))
    segs = col("data/segments.csv", "segment_code")
    doms = col("data/domains.csv", "domain_code")
    regs = col("data/regions.csv", "region_code")
    mods = col("data/modalities.csv", "modality_code")
    err = collections.defaultdict(list)

    for cid, n in collections.Counter(r["company_id"] for r in companies).items():
        if n > 1:
            err["duplicate company_id"].append(cid)

    for r in companies:
        cid = r["company_id"]
        if len(r) != 24 or None in r.values():
            err["wrong field count"].append(cid)
            continue
        if r["segment_primary"] not in segs:
            err["segment_primary"].append((cid, r["segment_primary"]))
        if r["segment_secondary"] not in segs | {"NA"}:
            err["segment_secondary"].append((cid, r["segment_secondary"]))
        if r["hq_region"] not in regs:
            err["hq_region"].append((cid, r["hq_region"]))
        if r["modality_primary"] not in mods:
            err["modality_primary"].append((cid, r["modality_primary"]))
        for f in ("domains_primary", "domains_secondary"):
            if r[f] == "NA":
                continue
            for d in r[f].split("|"):
                if d not in doms:
                    err[f].append((cid, d))
        for field, allowed in VOCAB.items():
            if r[field] not in allowed:
                err[field].append((cid, r[field]))
        if r["founded_year"] != "NA" and not 1800 <= int(r["founded_year"]) <= 2026:
            err["founded_year"].append((cid, r["founded_year"]))
        if r["countries_claimed"] != "NA" and not 1 <= int(r["countries_claimed"]) <= 250:
            err["countries_claimed"].append((cid, r["countries_claimed"]))

    # Every company must have exactly one spatial coverage row.
    cov = list(csv.DictReader(open("data/coverage_spatial.csv")))
    cov_ids = {r["company_id"] for r in cov}
    comp_ids = {r["company_id"] for r in companies}
    for cid in comp_ids - cov_ids:
        err["missing coverage row"].append(cid)
    for cid in cov_ids - comp_ids:
        err["orphan coverage row"].append(cid)
    for r in cov:
        for reg in regs:
            if r[reg] not in {"0", "1", "2", "3"}:
                err["coverage score"].append((r["company_id"], reg, r[reg]))
        if r["coverage_basis"] not in {"manual", "segment_template"}:
            err["coverage_basis"].append((r["company_id"], r["coverage_basis"]))

    if err:
        for k, v in err.items():
            print(f"{k}: {len(v)} -> {v[:10]}", file=sys.stderr)
        print(f"\nFAILED with {sum(len(v) for v in err.values())} errors", file=sys.stderr)
        return 1
    print(f"OK: {len(companies)} companies, {len(cov)} coverage rows, no errors")
    return 0

if __name__ == "__main__":
    sys.exit(main())
