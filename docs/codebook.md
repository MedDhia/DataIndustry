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
