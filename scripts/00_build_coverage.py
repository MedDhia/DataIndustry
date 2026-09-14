#!/usr/bin/env python3
"""Construct the company-by-region spatial coverage matrix.

Coverage is scored on an ordinal 0-3 scale (see docs/codebook.md):
  0 no meaningful coverage   1 thin or resold   2 substantial   3 deep or flagship

Two bases are used and recorded per row in `coverage_basis`:
  manual            hand-coded from specific knowledge of the firm's operations
  segment_template  derived from the firm's segment, spatial_scope and focus region

The segment templates below are the structural claim of this file: they encode
where a *globally scoped* firm of each type can realistically reach. They are
deliberately conservative and should be overridden wherever direct evidence exists.
"""
import csv, os

REGIONS = ["NOAM","LAC","WEU","EEU","RUS","MENA","SSA","SAS","SEA","EAS","CHN","OCE"]

# Reach of a globally scoped firm in each segment.
TEMPLATES = {
 "survey_insights":   [3,2,3,2,1,2,2,2,2,2,2,2],
 "panel_sample":      [3,2,3,2,0,1,1,2,2,2,1,2],
 "collection_software":[3,3,3,3,2,3,3,3,3,3,1,3],
 "field_agency":      [0,0,0,0,0,0,0,0,0,0,0,0],
 "crowd_micro":       [3,2,3,2,1,1,1,3,2,1,1,1],
 "ai_training_data":  [3,1,2,2,0,1,1,3,2,1,0,1],
 "expert_network":    [3,1,3,1,0,1,0,2,1,2,1,1],
 "web_data":          [3,2,3,2,1,2,1,2,2,2,1,2],
 "consumer_broker":   [3,1,2,1,0,1,0,1,1,1,0,2],
 "location_mobility": [3,1,2,1,0,1,0,1,1,1,0,1],
 "telecom_data":      [1,1,2,1,0,1,1,1,1,1,0,1],
 "earth_observation": [3,3,3,3,3,3,3,3,3,3,3,3],
 "iot_telemetry":     [3,1,3,1,0,1,0,1,1,1,0,2],
 "financial_altdata": [3,1,2,0,0,0,0,1,1,1,1,1],
 "trade_logistics":   [3,3,3,3,3,3,3,3,3,3,3,3],
 "retail_pricing":    [3,2,3,2,1,1,1,2,2,2,2,2],
 "health_rwd":        [3,0,1,0,0,0,0,0,0,1,0,1],
 "audience_measurement":[3,2,3,1,0,1,1,2,2,2,1,2],
 "social_osint":      [3,2,3,2,2,2,2,2,2,2,1,2],
 "b2b_firmographic":  [3,1,3,2,1,1,1,2,1,2,1,2],
 "climate_risk":      [3,2,3,2,2,2,2,2,2,2,2,2],
 "identity_biometric":[3,2,2,2,1,2,1,2,2,2,1,2],
}

# Firms whose operating region is not their headquarters region.
FOCUS = {
 "arab_barometer":"MENA","lapop":"LAC","gamaan":"MENA","ipm_belarus":"RUS",
 "laterite":"SSA","sagaci_research":"SSA","latinobarometro":"LAC",
 "central_asia_barometer":"RUS","serasa_experian":"LAC","uk_biobank":"WEU",
 "iranpoll":"MENA","zogby_research":"MENA",
}

# Hand-coded rows. Order follows REGIONS.
MANUAL = {
 # Global insights incumbents
 "ipsos":[3,3,3,3,1,3,2,3,3,3,2,3],"kantar":[3,3,3,2,1,2,2,3,3,3,3,3],
 "niq":[3,3,3,3,1,2,2,3,3,3,3,3],"circana":[3,1,3,1,0,0,0,0,0,1,0,1],
 "gallup":[3,2,3,2,2,2,2,2,2,2,2,2],"yougov":[3,2,3,2,0,2,1,2,2,2,1,2],
 "pew_research":[3,2,3,2,1,2,2,2,2,2,1,1],"morning_consult":[3,2,3,1,0,1,1,2,2,2,1,2],
 "verian":[2,1,3,2,0,1,1,1,1,1,0,1],"euromonitor":[3,3,3,3,2,3,2,3,3,3,3,3],
 "atlasintel":[3,3,2,1,0,1,0,0,0,0,0,0],
 # Panels and sample
 "cint":[3,2,3,3,1,2,1,2,2,2,1,3],"dynata":[3,2,3,2,0,1,1,2,2,2,1,2],
 "toluna":[3,2,3,2,0,2,1,2,2,2,1,2],"prolific":[3,1,3,1,0,1,0,1,1,1,0,2],
 "mturk":[3,0,1,0,0,0,0,3,0,0,0,0],"cloudresearch":[3,0,1,0,0,0,0,1,0,0,0,0],
 "borderless_access":[2,2,2,1,0,2,2,3,2,1,1,1],"macromill":[0,0,0,0,0,0,0,1,2,3,1,0],
 # Collection software and development research
 "surveycto":[2,3,2,2,1,3,3,3,3,1,0,2],"kobotoolbox":[2,3,2,2,1,3,3,3,3,1,0,2],
 "odk":[2,3,2,2,1,3,3,3,3,1,0,2],"commcare_dimagi":[1,2,1,1,0,2,3,3,2,1,0,1],
 "redcap":[3,2,3,2,1,2,2,2,2,2,1,2],"qualtrics":[3,2,3,2,0,2,1,2,2,2,1,3],
 # Development and impact fieldwork
 "geopoll":[0,0,0,0,0,2,3,2,1,0,0,0],"sixty_decibels":[1,2,0,0,0,1,3,3,2,0,0,0],
 "ipa_research":[1,2,0,0,0,1,3,3,1,0,0,0],"jpal":[2,2,1,0,0,1,3,3,2,0,0,0],
 "busara_center":[0,0,0,0,0,0,3,2,0,0,0,0],"flowminder":[0,1,0,0,0,1,3,2,1,0,0,0],
 "premise_data":[2,2,1,2,1,3,3,3,3,1,0,1],"trax_retail":[2,2,2,1,0,2,1,2,3,2,1,1],
 # AI training data: coverage here means where the working population is drawn from
 "scale_ai":[3,2,2,1,0,1,1,2,2,1,0,1],"surge_ai":[3,1,2,1,0,1,1,2,1,1,0,1],
 "mercor":[3,2,2,2,1,1,1,3,2,2,0,1],"handshake_ai":[3,0,1,0,0,0,0,1,0,0,0,0],
 "micro1":[2,1,1,2,1,1,1,3,1,1,0,1],"turing_com":[2,2,1,2,1,1,1,3,1,1,0,1],
 "appen":[3,2,3,2,1,2,2,3,3,3,2,3],"toloka":[2,2,3,3,2,2,2,3,2,1,1,1],
 "telus_digital_ai":[3,2,3,2,1,2,2,3,3,2,1,2],"sama":[1,0,0,0,0,0,3,0,0,0,0,0],
 "imerit":[1,0,0,0,0,0,1,3,0,0,0,0],"cloudfactory":[1,0,1,0,0,0,2,3,0,0,0,0],
 "speechocean":[2,1,2,1,1,1,1,2,2,2,3,1],"datatang":[1,0,1,0,0,0,0,1,1,1,3,0],
 "magic_data_tech":[1,0,1,0,0,0,0,1,1,1,3,0],
 # Web and open corpora
 "bright_data":[3,3,3,3,2,3,2,3,3,3,2,3],"common_crawl":[3,3,3,3,3,3,2,3,3,3,2,3],
 "gdelt":[3,3,3,3,3,3,2,3,3,3,2,3],"acled":[2,3,2,3,3,3,3,3,3,2,1,2],
 "similarweb":[3,3,3,3,2,3,2,3,3,3,1,3],"sensor_tower":[3,3,3,3,2,3,2,3,3,3,1,3],
 # Consumer brokerage and identity
 "experian":[3,3,3,1,0,1,1,2,2,1,0,2],"equifax":[3,2,2,0,0,0,1,1,0,0,0,2],
 "transunion":[3,2,1,0,0,0,1,2,0,1,0,0],"crif":[1,1,3,3,1,1,0,2,1,1,1,0],
 "dun_bradstreet":[3,2,3,2,1,2,1,2,2,2,2,2],"lexisnexis_risk":[3,2,2,1,0,1,1,1,1,1,0,2],
 "liveramp":[3,1,2,1,0,0,0,0,1,1,0,2],"acxiom":[3,1,2,1,0,0,0,0,1,1,0,2],
 "cotality":[3,0,1,0,0,0,0,0,0,0,0,2],"verisk":[3,1,2,1,0,1,0,1,1,1,0,2],
 # Location and mobility
 "safegraph":[3,1,2,1,0,1,1,1,1,1,0,1],"foursquare":[3,2,2,1,0,1,1,1,2,2,0,2],
 "kochava_collective":[3,2,2,1,0,1,1,2,2,2,0,2],"azira":[3,1,2,1,0,1,0,2,2,2,0,1],
 "geotab":[3,2,3,1,0,1,1,1,1,1,0,2],"here_technologies":[3,2,3,3,1,2,1,2,2,2,1,3],
 "tomtom":[3,2,3,3,1,2,1,2,2,2,1,3],"inrix":[3,1,3,1,0,1,0,1,0,1,0,1],
 # Trade and logistics: vessel tracking is global, customs records are not
 "panjiva":[3,3,1,1,1,1,1,3,2,1,0,1],"importgenius":[3,3,1,1,1,1,1,3,2,1,0,1],
 # Health real-world data
 "iqvia":[3,2,3,2,1,1,1,2,2,2,1,2],"trinetx":[3,1,3,2,1,1,1,1,1,2,0,1],
 "medidata":[3,2,3,2,1,2,1,2,2,3,2,2],"bgi_genomics":[1,1,1,1,1,1,1,1,2,2,3,1],
 # Media measurement
 "nielsen":[3,2,3,1,0,1,1,2,2,2,0,2],"comscore":[3,2,3,1,0,1,0,1,1,1,0,2],
 # Firmographic and corporate records
 "sayari":[3,3,3,3,3,3,2,3,3,3,3,3],"opencorporates":[3,2,3,3,1,1,1,1,2,2,1,2],
 "moodys_bvd":[3,2,3,3,2,2,2,2,2,3,2,3],"zoominfo":[3,1,2,1,0,1,0,1,1,1,0,2],
 "people_data_labs":[3,1,2,1,0,1,0,2,1,1,0,2],"coresignal":[3,1,3,2,1,1,1,2,2,2,1,2],
 # Biometrics and surveillance
 "clearview_ai":[3,2,1,2,1,2,1,2,2,2,1,2],"idemia":[2,2,3,2,1,3,3,2,2,2,0,2],
 "tools_for_humanity":[1,3,2,1,0,1,1,1,2,2,0,1],"hikvision":[1,2,1,2,2,3,3,3,3,2,3,1],
 "sensetime":[0,1,0,1,1,2,2,1,2,1,3,0],"megvii":[0,0,0,0,1,1,1,1,2,1,3,0],
 # Regional survey networks
 "afrobarometer":[0,0,0,0,0,1,3,0,0,0,0,0],"arab_barometer":[0,0,0,0,0,3,1,0,0,0,0,0],
 "latinobarometro":[0,3,0,0,0,0,0,0,0,0,0,0],"lapop":[1,3,0,0,0,0,0,0,0,0,0,0],
 "crrc":[0,0,0,3,1,1,0,0,0,0,0,0],"central_asia_barometer":[0,0,0,0,3,0,0,0,0,0,0,0],
 "m_vector":[0,0,0,1,3,0,0,0,0,0,0,0],"siar_research":[0,0,0,1,3,0,0,0,0,0,0,0],
 "cid_gallup":[0,3,0,0,0,0,0,0,0,0,0,0],"parc_dubai":[0,0,0,0,0,3,0,0,0,0,0,0],
 "awrad":[0,0,0,0,0,3,0,0,0,0,0,0],"nama_strategic":[0,0,0,0,0,3,0,0,0,0,0,0],
 "positium":[1,1,2,2,1,1,1,1,1,1,0,1],"teralytics":[1,1,3,1,0,1,0,1,1,1,0,1],
 "orange_flux_vision":[0,0,3,1,0,2,2,0,0,0,0,0],
 "reach_initiative":[0,1,0,1,1,3,3,2,1,0,0,0],"acaps":[0,2,0,2,2,3,3,3,2,0,0,1],
 "viamo":[0,1,0,0,0,1,3,3,2,0,0,0],"space42":[3,3,3,3,3,3,3,3,3,3,3,3],
 "gro_intelligence":[3,2,2,1,1,2,2,2,2,1,1,1],
 "measurable_ai":[0,1,0,0,0,2,0,2,3,2,1,0],
}

def scope_adjust(vec, scope, hq_idx):
    v = list(vec)
    if scope == "multi_region":
        v = [max(0, x-1) for x in v]
        v[hq_idx] = max(v[hq_idx], 2)
    return v

def main():
    rows = list(csv.DictReader(open("data/companies.csv")))
    out = []
    for r in rows:
        cid, scope = r["company_id"], r["spatial_scope"]
        focus = FOCUS.get(cid, r["hq_region"])
        fi = REGIONS.index(focus)
        if cid in MANUAL:
            vec, basis = MANUAL[cid], "manual"
        elif scope in ("single_country", "single_region"):
            vec = [0]*12; vec[fi] = 3; basis = "segment_template"
        else:
            vec = scope_adjust(TEMPLATES[r["segment_primary"]], scope, fi)
            basis = "segment_template"
        assert len(vec) == 12 and all(0 <= x <= 3 for x in vec), cid
        out.append(dict(company_id=cid, coverage_basis=basis,
                        **{reg: vec[i] for i, reg in enumerate(REGIONS)}))
    with open("data/coverage_spatial.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["company_id","coverage_basis"]+REGIONS)
        w.writeheader(); w.writerows(out)
    man = sum(1 for o in out if o["coverage_basis"] == "manual")
    print(f"wrote {len(out)} rows | manual {man} | template {len(out)-man}")

if __name__ == "__main__":
    main()
