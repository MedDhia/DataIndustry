# Codebook

All files are UTF-8 CSV with a header row. `NA` denotes a value that is unknown or
does not apply. Multi-valued fields use `|` as the separator. `company_id` is the
primary key across every file.

## `data/companies.csv` (424 rows, 24 variables)

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

Current distribution: A 29, B 153, C 242. Treat every `C` figure as an ordinal
placement rather than a measurement.

## `data/coverage_spatial.csv` (424 rows, 14 variables)

`company_id`, `coverage_basis`, then one column per region code.

Coverage is ordinal:

| Score | Meaning |
|---|---|
| 0 | No meaningful coverage. |
| 1 | Thin. A handful of countries, resold supply, or a nominal claim. |
| 2 | Substantial. Own operations or a dense dataset across much of the region. |
| 3 | Deep. Flagship coverage; the firm is a reference source for the region. |

`coverage_basis` records how the row was produced:

- `manual` (113 rows) — hand-coded from specific knowledge of the firm.
- `segment_template` (311 rows) — derived by the documented rule in
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

## `data/coverage_country_manual.csv` (1,122 rows, 93 organisations)

Hand-coded country footprints: `company_id`, `iso3`, `coverage`, `scope`.
Sources are published country lists (the barometer networks), regional hub
partner lists, and known office and delivery-centre networks.

`scope` governs how the row interacts with the model:

- `exhaustive` (798 rows) — the list is complete. The firm's country coverage
  comes entirely from here and the model adds nothing.
- `partial` (324 rows) — these countries are observed. The model fills the rest
  of the firm's stated country budget around them, and hand-coded rows spend
  that budget first.

`partial` exists so that knowing a global firm's MENA and Africa offices does
not force a claim about its Latin American ones. Without it, partial knowledge
would shrink a footprint rather than improve it.

Coverage is weighted toward MENA and Sub-Saharan Africa by design: 15.4% and
14.2% of their country rows are observed, against 5.6% for the file overall and
0.2% for Western Europe. That skew has now degraded the observed-only sensitivity
check to the point where it no longer validates the model. Section 12 of
`coverage_gaps.md` gives the breakdown and the consequence.

### Observations override the feasibility gate

A hand-coded row survives even when the method and domain gates below would
empty it, falling back to the firm's own primary method. The gate is a model of
where a method can work; a hand-coded footprint is a record that the firm is
there. Impact-sourcing delivery centres are the clear case: Sama's operation in
Uganda supplies its own connectivity regardless of the national figure.

## `data/coverage_country.csv` (21,961 rows, 9 variables)

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
| `manual` | 1,122 | Observation. Hand-coded footprint. |
| `hq_exact` | 107 | Observation. Single-country firm resolved to its headquarters country. |
| `allocated` | 20,732 | Model output. |

**94% of rows are model output**, and 85% in MENA and Sub-Saharan Africa. An `allocated` row says where a firm of that
type, regional footprint and stated country count most likely operates. It is
not a claim that the firm operates there. Aggregate country counts are usable;
an individual firm's row is not citable.

`scripts/04_country_gaps.R` reports every country-level regression twice, once
on the full file and once on the 1,229 observed rows only (`tab19_sensitivity`).
A result that appears only in the full column is a property of the allocation
rule. On the current data **only population and internet penetration survive**,
keeping their sign in both columns. Income reverses sign; restrictive research
regime and conflict exposure go to zero.

The income reversal is a diagnostic, not a finding: because hand-coding is
concentrated in MENA and Africa, the observed subsample is mostly poor countries,
so a regression on it recovers the shape of the coding effort. The observed-only
column can no longer be treated as a validation of the model, only as a signal
that a result is unstable. Report nothing from the country regressions that does
not hold in both columns with the same sign.

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

An `allocated` row with no usable method, or no obtainable data type, is not
written. A `manual` or `hq_exact` row is always written, because the observation
overrides the gate.

Method repertoires come from the firm's `modality_primary` plus the methods its
segment can deploy, listed in `SEGMENT_METHODS` in the build script.
