# Codebook

All files are UTF-8 CSV with a header row. `NA` denotes a value that is unknown or
does not apply. Multi-valued fields use `|` as the separator. `company_id` is the
primary key across every file.

## `data/companies.csv` (370 rows, 24 variables)

| Variable | Type | Description |
|---|---|---|
| `company_id` | string | Stable slug. Primary key. |
| `company_name` | string | Trading name as the firm presents itself. |
| `parent_company` | string | Immediate owner where the firm is not independent. |
| `hq_country` | ISO 3166-1 alpha-3 | Country of the operational headquarters, not of incorporation. |
| `hq_region` | factor | One of the twelve codes in `regions.csv`. |
| `founded_year` | integer | Year the collecting operation began, not the year of a later holding company. |
| `maturity_class` | factor | `established`, `scaleup`, `startup`. See below. |
| `ownership_type` | factor | `public_listed`, `private_pe`, `private_vc`, `private_independent`, `subsidiary`, `nonprofit`, `academic`, `state_linked`, `cooperative_jic`. |
| `status` | factor | `active`, `acquired_active`, `wound_down`, `insolvent`. |
| `segment_primary` | factor | Principal segment, from `segments.csv`. |
| `segment_secondary` | factor | Secondary segment or `NA`. |
| `modality_primary` | factor | Principal collection method, from `modalities.csv`. |
| `unit_of_observation` | factor | `individual`, `household`, `device`, `firm`, `place`, `transaction`, `document`, `area`, `patient`, `vehicle`, `housing_unit`. |
| `temporal_granularity` | factor | `real_time`, `daily`, `weekly`, `monthly`, `quarterly`, `annual`, `episodic`. |
| `spatial_scope` | factor | `global`, `multi_region`, `single_region`, `single_country`. |
| `countries_claimed` | integer | Countries the firm claims to reach. A marketing figure, recorded as stated, not verified. |
| `domains_primary` | list | Substantive domains that are core to the business, from `domains.csv`. |
| `domains_secondary` | list | Domains covered but not central. |
| `human_subjects` | factor | `direct` (the firm interacts with people), `indirect` (data about people obtained from a third party or a device), `none`. |
| `consent_model` | factor | `explicit_consent`, `platform_terms`, `contractual_third_party`, `public_record`, `not_applicable`. |
| `access_model` | factor | `project_commission`, `subscription`, `api_license`, `marketplace`, `panel_rental`, `open_free`. |
| `microdata_access` | factor | Who can obtain record-level data: `open`, `researcher_restricted`, `commercial_only`, `none`. |
| `evidence_level` | factor | `A`, `B`, `C`. See below. |
| `notes` | string | Short free text, no commas. |

### `maturity_class`

- `established` — operating more than roughly twenty years, or listed, or held at
  scale by private equity.
- `scaleup` — growth stage, typically founded between 2006 and 2018.
- `startup` — founded 2019 or later, or still at seed or Series A.

Age and stage are recorded separately (`founded_year`, `ownership_type`) so that
users who dislike this cut can build their own.

### `evidence_level`

This variable describes the coding, not the firm. It is the honest limit of the
dataset and should be reported in anything built on it.

- `A` — verified against a regulatory filing or a source retrieved during
  construction, and cited in `docs/sources.md`.
- `B` — consistently reported across multiple independent public sources.
- `C` — analyst judgement from domain knowledge. Directionally reliable for
  segment, region and modality; not reliable for dates or counts.

Current distribution: A 21, B 140, C 209. Treat every `C` figure as an ordinal
placement rather than a measurement.

## `data/coverage_spatial.csv` (370 rows, 14 variables)

`company_id`, `coverage_basis`, then one column per region code.

Coverage is ordinal:

| Score | Meaning |
|---|---|
| 0 | No meaningful coverage. |
| 1 | Thin. A handful of countries, resold supply, or a nominal claim. |
| 2 | Substantial. Own operations or a dense dataset across much of the region. |
| 3 | Deep. Flagship coverage; the firm is a reference source for the region. |

`coverage_basis` records how the row was produced:

- `manual` (108 rows) — hand-coded from specific knowledge of the firm.
- `segment_template` (262 rows) — derived by the documented rule in
  `scripts/00_build_coverage.py` from segment, `spatial_scope` and focus region.
  For the single-country and single-region field agencies that make up most of
  these rows the rule is near-exact. For globally scoped firms it is an
  assumption, and those rows should be hand-checked before load-bearing use.

A score of 2 is the threshold used throughout the analysis to mean "present".

## Derived matrices

`scripts/01_load.R` constructs two matrices used by everything downstream.

- `spatial_mat` — firms by regions, ordinal 0-3.
- `domain_mat` — firms by domains, weight 2 for a primary domain, 1 for a
  secondary domain, 0 otherwise.

`scripts/03_coverage_gaps.R` writes long-format versions to `output/`.

## Lookup tables

- `data/regions.csv` — twelve regions. Mainland China and the Russia/Belarus/
  Central Asia bloc are separated from their neighbours because exclusion from
  them is one of the strongest patterns in the industry.
- `data/segments.csv` — twenty-two segments, each tagged `solicited` (data is
  produced by asking someone) or `observational` (data is captured from traces).
- `data/domains.csv` — twenty-six substantive domains.
- `data/modalities.csv` — fifteen collection methods, each tagged by whether it
  brings the firm into contact with a data subject.

---

# Country layer

The region layer above remains the empirically grounded one. The country layer
disaggregates it, and most of it is model output. Read this section before using
any country-level figure.

## `data/countries.csv` (194 rows, 9 variables)

| Variable | Type | Description |
|---|---|---|
| `iso3` | ISO 3166-1 alpha-3 | Primary key. |
| `country_name` | string | Common English name. |
| `region_code` | factor | One of the twelve codes in `regions.csv`. |
| `subregion` | string | Finer grouping within the region. |
| `income_group` | factor | `LIC`, `LMIC`, `UMIC`, `HIC`, following the World Bank classification. |
| `population_band` | factor | `XS` under 1m, `S` 1-10m, `M` 10-50m, `L` 50-100m, `XL` over 100m. |
| `internet_band` | factor | `low` under 30%, `medium` 30-70%, `high` over 70% of population online. |
| `conflict_affected` | binary | Sustained armed conflict or acute state fragility as of 2026. |
| `restrictive_research_regime` | binary | Independent collection is legally gated: survey or research licensing, foreign agent and NGO law, or hostile treatment of foreign data firms. |

The last two are coded judgements against the stated criteria, not indices
imported from elsewhere. They are blunt, and a user who disagrees with a
specific coding should change it and rerun.

Note that region code `NOAM` is used for North America rather than `NAM`,
because `NAM` is the ISO3 code for Namibia.

## `data/coverage_country_manual.csv` (349 rows)

Hand-coded country footprints for 40 organisations: `company_id`, `iso3`,
`coverage`. Sources are published country lists (the barometer networks) or
known operating footprints. A firm present in this file has its country
coverage taken entirely from here, with no model allocation on top.

## `data/coverage_country.csv` (21,344 rows, 9 variables)

One row per company-country pair with non-zero coverage. Absence is the
anti-join: a pair not present here is a pair with no coverage.

| Variable | Type | Description |
|---|---|---|
| `company_id`, `iso3`, `region_code` | key | |
| `coverage` | 1-3 | Same ordinal scale as the region layer. |
| `basis` | factor | `manual`, `hq_exact`, `allocated`. |
| `n_methods`, `n_domains` | integer | Counts of the two list columns. |
| `methods` | list | Collection methods the firm can actually deploy in this country. |
| `domains` | list | Substantive data types obtainable from this firm in this country. |

### What `basis` means, and why it matters

| Basis | Rows | Status |
|---|---|---|
| `manual` | 349 | Observation. Hand-coded footprint. |
| `hq_exact` | 86 | Observation. Single-country firm resolved to its headquarters country. |
| `allocated` | 20,909 | Model output. |

**98% of rows are model output.** An `allocated` row says where a firm of that
type, regional footprint and stated country count most likely operates. It is
not a claim that the firm operates there. Aggregate country counts are usable;
an individual firm's row is not citable.

`scripts/04_country_gaps.R` reports every country-level regression twice, once
on the full file and once on the 435 observed rows only (`tab19_sensitivity`).
A result that appears only in the full column is a property of the allocation
rule. On the current data, population and internet penetration survive that
test; conflict exposure and restrictive research regime do not.

### The allocation model

Documented in full in the docstring of `scripts/00_build_country_coverage.py`.
In outline: a firm's `countries_claimed` is treated as a budget, split across
regions by the square of the regional coverage score times the number of
countries in the region, then spent from the top of a within-region priority
ordering, with coverage decaying one step below the median-ranked country.

Three priority orderings are used, because different parts of the industry enter
countries for different reasons:

- `market` — income, population, connectivity. Firms selling data about a
  country's consumers or firms.
- `labour` — population, connectivity, low income. Annotation and micro-task
  firms, whose country coverage describes where their *workers* are, not who
  they collect data about.
- `need` — low income, conflict exposure, population. Firms whose clients are
  donors and agencies.

Each ordering is a falsifiable claim about market entry. Change the weights,
rerun, and the gap tables move.

### Method and domain gating

A method is dropped in a country that cannot support it, and a data type is
dropped where the infrastructure it derives from does not exist. These gates are
the substantive content of the "by method and by type" coding:

| Gate | Applies to |
|---|---|
| Requires internet `medium` or `high` | `online_panel`, `device_passive`, `mobile_app`, `crowd_task`, `expert_elicit`; domains `device_telemetry`, `mobility_location` |
| Requires income `UMIC` or `HIC` | `clinical_records`; domains `financial_transactions`, `credit_risk` |
| Requires both | `transaction`; `health_clinical` and `prices_retail` where the firm's primary method is record- or transaction-based |
| Ungated | `face_to_face`, `telephone`, `web_scrape`, `api_partner`, `admin_records`, `remote_sensing`, `sensor_hardware`, `telecom_network` |

A firm left with no usable method, or no obtainable data type, generates no row
for that country.

Method repertoires come from the firm's `modality_primary` plus the methods its
segment can deploy, listed in `SEGMENT_METHODS` in the build script.
