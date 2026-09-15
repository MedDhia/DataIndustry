#!/usr/bin/env python3
"""Validate data/companies.csv against the lookup tables and controlled vocabularies.

Exits non-zero and prints every offending record if anything fails, so this can
be run as a pre-commit check when the register is extended.
"""
import csv, collections, sys

VOCAB = {
 "maturity_class": {"established", "scaleup", "startup"},
 "sector": {"for_profit", "nonprofit", "academic", "governmental"},
 "ownership_type": {"public_listed", "private_pe", "private_vc", "private_independent",
                    "subsidiary", "nonprofit", "academic", "state_linked", "cooperative_jic"},
 "status": {"active", "acquired_active", "absorbed", "wound_down", "insolvent"},
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
        if len(r) != 26 or None in r.values():
            err["wrong field count"].append(cid)
            continue
        # sector and ownership_type are separate variables but not free of each
        # other: a nonprofit or academic owner cannot be a for-profit sector.
        if r["ownership_type"] in ("nonprofit", "academic") and r["sector"] == "for_profit":
            err["sector vs ownership_type"].append((cid, r["ownership_type"], r["sector"]))
        if r["ownership_type"] in ("public_listed", "private_pe", "private_vc") \
           and r["sector"] != "for_profit":
            err["sector vs ownership_type"].append((cid, r["ownership_type"], r["sector"]))
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
        if r["ceased_year"] != "NA":
            if not 1800 <= int(r["ceased_year"]) <= 2026:
                err["ceased_year"].append((cid, r["ceased_year"]))
            elif r["status"] in ("active", "acquired_active"):
                err["ceased_year set on operating firm"].append(cid)
            elif r["founded_year"] != "NA" and int(r["ceased_year"]) < int(r["founded_year"]):
                err["ceased before founded"].append(cid)
        elif r["status"] in ("absorbed", "wound_down", "insolvent"):
            err["exit status without ceased_year"].append(cid)
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

    # Country layer.
    ctys = list(csv.DictReader(open("data/countries.csv")))
    iso = {r["iso3"] for r in ctys}
    if len(iso) != len(ctys):
        err["duplicate iso3"].append("see countries.csv")
    for r in ctys:
        if r["region_code"] not in regs:
            err["country region_code"].append((r["iso3"], r["region_code"]))
        for field, allowed in (("income_group", {"HIC", "UMIC", "LMIC", "LIC"}),
                               ("population_band", {"XS", "S", "M", "L", "XL"}),
                               ("internet_band", {"high", "medium", "low"}),
                               ("conflict_affected", {"0", "1"}),
                               ("restrictive_research_regime", {"0", "1"})):
            if r[field] not in allowed:
                err[f"country {field}"].append((r["iso3"], r[field]))

    for r in csv.DictReader(open("data/coverage_country_manual.csv")):
        if r["company_id"] not in comp_ids:
            err["manual company_id"].append(r["company_id"])
        if r["iso3"] not in iso:
            err["manual iso3"].append(r["iso3"])

    cc = list(csv.DictReader(open("data/coverage_country.csv")))
    for r in cc:
        if r["company_id"] not in comp_ids:
            err["country coverage company_id"].append(r["company_id"])
        if r["iso3"] not in iso:
            err["country coverage iso3"].append(r["iso3"])
        if r["coverage"] not in {"1", "2", "3"}:
            err["country coverage score"].append((r["company_id"], r["iso3"], r["coverage"]))
        if r["basis"] not in {"manual", "hq_exact", "allocated"}:
            err["country coverage basis"].append((r["company_id"], r["basis"]))
        for d in r["domains"].split("|"):
            if d not in doms:
                err["country coverage domain"].append((r["company_id"], d))
        for m in r["methods"].split("|"):
            if m not in mods:
                err["country coverage method"].append((r["company_id"], m))
    if {r["company_id"] for r in cc} != comp_ids:
        err["firms absent from country coverage"].append(
            sorted(comp_ids - {r["company_id"] for r in cc}))

    # Ownership and funding layer.
    own = list(csv.DictReader(open("data/ownership.csv")))
    OWN_TYPE = {"founder", "controlling_owner", "investor", "funder", "acquirer"}
    OWN_CAT = {"individual", "vc", "pe", "sovereign_wealth", "corporate", "foundation",
               "bilateral_donor", "multilateral", "university", "state", "media_group"}
    for r in own:
        if r["company_id"] not in comp_ids:
            err["ownership company_id"].append(r["company_id"])
        if r["stakeholder_type"] not in OWN_TYPE:
            err["stakeholder_type"].append((r["company_id"], r["stakeholder_type"]))
        if r["stakeholder_category"] not in OWN_CAT:
            err["stakeholder_category"].append((r["company_id"], r["stakeholder_category"]))
        if r["stakeholder_country"] not in iso | {"NA"}:
            err["stakeholder_country"].append((r["company_id"], r["stakeholder_country"]))
        if r["evidence_level"] not in {"A", "B", "C"}:
            err["ownership evidence_level"].append((r["company_id"], r["evidence_level"]))

    # ---- grant_programmes.csv: recurring funding instruments, not organisations.
    progs = list(csv.DictReader(open("data/grant_programmes.csv")))
    PROG = {
     "funder_category": {"foundation", "bilateral_donor", "multilateral", "state",
                         "nonprofit", "corporate", "university"},
     "instrument_type": {"grant", "prize", "equity_free_investment", "convertible",
                         "state_subsidy", "fellowship"},
     "cadence": {"annual", "biennial", "rolling", "thematic_rounds", "one_off"},
     "geography_scope": {"global", "multi_region", "single_region", "single_country"},
     "stage_targeted": {"idea", "seed", "early", "growth", "any"},
     "data_specific": {"yes", "partial", "no"},
     "status": {"open", "dormant", "discontinued"},
     "evidence_level": {"A", "B", "C"},
    }
    for pid, n in collections.Counter(r["programme_id"] for r in progs).items():
        if n > 1:
            err["duplicate programme_id"].append(pid)
    for r in progs:
        pid = r["programme_id"]
        if len(r) != 20 or None in r.values():
            err["programme wrong field count"].append(pid)
            continue
        for f, vocab in PROG.items():
            if r[f] not in vocab:
                err[f"programme {f}"].append((pid, r[f]))
        if r["funder_country"] not in iso:
            err["programme funder_country"].append((pid, r["funder_country"]))
        for rg in r["eligible_regions"].split("|"):
            if rg not in regs:
                err["programme eligible_regions"].append((pid, rg))
        for f in ("award_min_usd", "award_max_usd", "first_year"):
            if not r[f].isdigit():
                err[f"programme {f}"].append((pid, r[f]))
        if int(r["award_min_usd"]) > int(r["award_max_usd"]):
            err["programme award range"].append(pid)
        if (r["status"] == "discontinued") != (r["ended_year"] != "NA"):
            err["programme status vs ended_year"].append((pid, r["status"], r["ended_year"]))

    # ---- demand.csv: the buyer side, keyed on segment rather than on firm. ---
    # Rows are buyer categories, not buyers, because almost no segment publishes
    # a customer list. Evidence A is reserved for a named buyer with a public
    # award or a disclosed deal; B is a buyer category documented in named trade
    # or press reporting; C is an inference from the segment's structure.
    DEM = {
     "buyer_category": {"government_security", "government_civil", "multilateral_donor",
                        "financial_investor", "financial_lender", "insurance",
                        "pharma_health", "corporate_marketing", "corporate_operations",
                        "media_advertising", "ai_developer", "retail_cpg",
                        "academic_research", "ngo_advocacy", "research_intermediary",
                        "political_party"},
     "procurement_mode": {"subscription", "one_off_commission", "framework_contract",
                          "marketplace_api", "licensing_deal", "membership_levy",
                          "grant_funded", "panel_rental"},
     "contract_visibility": {"public_award", "disclosed_deal", "trade_reported", "opaque"},
     "direction": {"rising", "stable", "declining", "contested"},
     "price_signal_basis": {"contract_total", "contract_annual", "buyer_annual",
                            "market_annual", "NA"},
     "evidence_level": {"A", "B", "C"},
    }
    dem = list(csv.DictReader(open("data/demand.csv")))
    for did, n in collections.Counter(r["demand_id"] for r in dem).items():
        if n > 1:
            err["duplicate demand_id"].append(did)
    for r in dem:
        did = r["demand_id"]
        if len(r) != 14 or None in r.values():
            err["demand wrong field count"].append(did)
            continue
        for f, vocab in DEM.items():
            if r[f] not in vocab:
                err[f"demand {f}"].append((did, r[f]))
        if r["segment"] not in segs:
            err["demand segment"].append((did, r["segment"]))
        if r["geography"] not in regs | {"global"}:
            err["demand geography"].append((did, r["geography"]))
        if r["price_signal_usd"] != "NA" and not r["price_signal_usd"].isdigit():
            err["demand price_signal_usd"].append((did, r["price_signal_usd"]))
        if (r["price_signal_usd"] == "NA") != (r["price_signal_basis"] == "NA"):
            err["demand price signal vs basis"].append((did, r["price_signal_usd"],
                                                        r["price_signal_basis"]))
        if r["signal_year"] != "NA" and not (r["signal_year"].isdigit()
                                             and 1990 <= int(r["signal_year"]) <= 2026):
            err["demand signal_year"].append((did, r["signal_year"]))
        if not r["url"].startswith("http"):
            err["demand url"].append((did, r["url"]))
        # An A row has to point at something a reader can check: a named buyer
        # and either a public award or a deal the parties themselves disclosed.
        if r["evidence_level"] == "A" and (r["buyer_examples"] == "NA" or
                r["contract_visibility"] not in ("public_award", "disclosed_deal")):
            err["demand evidence A without a checkable buyer"].append(did)

    if err:
        for k, v in err.items():
            print(f"{k}: {len(v)} -> {v[:10]}", file=sys.stderr)
        print(f"\nFAILED with {sum(len(v) for v in err.values())} errors", file=sys.stderr)
        return 1
    print(f"OK: {len(companies)} companies, {len(cov)} region rows, "
          f"{len(ctys)} countries, {len(cc)} company-country rows, "
          f"{len(own)} ownership rows, {len(progs)} grant programmes, "
          f"{len(dem)} demand rows, no errors")
    return 0

if __name__ == "__main__":
    sys.exit(main())
