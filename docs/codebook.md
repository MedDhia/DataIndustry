# Codebook

All files are UTF-8 CSV with a header row. `NA` denotes a value that is unknown or
does not apply. Multi-valued fields use `|` as the separator. `company_id` is the
primary key across every file.

## `data/companies.csv` (569 rows, 25 variables)

The register includes 513 operating organisations and 56 that no longer operate.
**Every coverage and gap table in this repository uses operating firms only.**
`scripts/01_load.R` applies that filter and exposes the full set as
`companies_all` for the historical analysis in `scripts/05_history.R`. Omitting
the exited firms would make this a survivor sample of an industry that has
consolidated hard, and section 14 of `coverage_gaps.md` quantifies what that
would hide.

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
| `status` | factor | `active` (independent and operating), `acquired_active` (operating under a new parent, brand retained), `absorbed` (acquired and no longer operating as a distinct entity), `wound_down` (ceased trading), `insolvent` (failed through bankruptcy or administration). The last three are exits and are excluded from coverage tables. |
| `ceased_year` | integer | Year the firm stopped operating as a distinct entity. Required for `absorbed`, `wound_down` and `insolvent`; must be `NA` for operating firms. The validator enforces both directions. |
| `segment_primary` | factor | Principal segment, from `segments.csv`. |
| `segment_secondary` | factor | Secondary segment or `NA`. |
| `modality_primary` | factor | Principal collection method, from `modalities.csv`. |
| `unit_of_observation` | factor | `individual`, `household`, `device`, `firm`, `place`, `transaction`, `document`, `area`, `patient`, `vehicle`, `housing_unit`. |
| `temporal_granularity` | factor | `real_time`, `daily`, `weekly`, `monthly`, `quarterly`, `annual`, `episodic`. |
| `spatial_scope` | factor | `global`, `multi_region`, `single_region`, `single_country`. |
| `countries_claimed` | integer | Countries the firm claims to reach. A marketing figure, recorded as stated, not verified. |
| `domains_primary` | list | Substantive domains that are core to the business, from `domains.csv`. |
| `domains_secondary` | list | Domains covered but not central. |
| `human_subjects` | factor | `direct` (the firm interacts with people), `indirect` (data about people obtained from a third party or a device), `none`. A solicited-segment firm coded `none` is either a desk-research reseller or a synthetic research firm that simulates respondents rather than recruiting them; see section 13 of `coverage_gaps.md`. |
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

Current distribution over operating firms: A 59, B 192, C 262. Treat every `C` figure as an ordinal
placement rather than a measurement.

## `data/coverage_spatial.csv` (569 rows, 14 variables)

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

## `data/ownership.csv` (212 rows, 113 organisations)

Founders, owners, investors, acquirers and funders. One row per organisation-
stakeholder pair.

| Variable | Type | Description |
|---|---|---|
| `company_id` | key | Foreign key to `companies.csv`. |
| `stakeholder_name` | string | Person or organisation. |
| `stakeholder_type` | factor | `founder`, `controlling_owner`, `investor`, `funder`, `acquirer`. |
| `stakeholder_country` | ISO3 | Where the stakeholder is based, not necessarily their nationality. |
| `stakeholder_category` | factor | `individual`, `vc`, `pe`, `sovereign_wealth`, `corporate`, `foundation`, `bilateral_donor`, `multilateral`, `university`, `state`, `media_group`. |
| `evidence_level` | factor | `A`, `B`, `C`, as in `companies.csv`. |
| `notes` | string | Short free text, no commas. |

**Coverage is partial and purposive, and this matters more here than anywhere
else in the repository.** A row exists only where the relationship could be
established from a source. Effort went to the organisations whose data is openly
accessible, because section 4 of `coverage_gaps.md` found that openness tracks
grant funding, and to MENA and African firms. Four fifths of the register has no
stakeholder row, and the missing four fifths is not a random sample: owner-managed
independents, the largest ownership category in the register, disclose almost
nothing publicly.

The bias runs opposite to most business datasets. Grant-funded organisations
publish their funders because donors require acknowledgement; privately held
firms publish nothing absent a transaction. Findings about funding are therefore
much better supported than anything this file says about private ownership.

### Verification status of founder rows

Founder rows carry 35 at level A and 65 at level B; there are no level-C founder
rows. Level A means the attribution was checked against a source during a
verification pass. Level B means it comes from domain knowledge and has not been
individually checked. One attribution found during verification was wrong, and
the failure mode is worth knowing: it was a name collision between two similarly
named organisations in the same region, not a misremembered person. Level B
founder rows should be treated as claims to check, and checking them is the
cheapest available improvement to this file.

Six founders carry `NA` for `stakeholder_country` because nationality could not
be established. Any statistic using `domestic` must be computed over the rows
where it is known, as `06_ownership.R` does.

**Absence of a row means not established, never that an organisation has no owner
or funder.** Do not compute shares over the register from this file. Shares
computed over the rows that exist, as `scripts/06_ownership.R` does, describe the
established relationships and nothing wider; the script prints the denominators
alongside every figure for that reason.

`scripts/01_load.R` joins the organisation's region and access regime onto each
row and derives `stakeholder_region` and `domestic`, a flag for whether the
stakeholder sits in the same country as the organisation it backs.

## Lookup tables

- `data/regions.csv` — twelve regions. Mainland China and the Russia/Belarus/
  Central Asia bloc are separated from their neighbours because exclusion from
  them is one of the strongest patterns in the industry.
- `data/segments.csv` — twenty-three segments, each tagged `solicited` (data is
  produced by asking someone) or `observational` (data is captured from traces).
- `data/domains.csv` — twenty-seven substantive domains.
- `data/modalities.csv` — nineteen collection methods, each tagged by whether it
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

## `data/coverage_country_manual.csv` (2,534 rows, 212 organisations)

Hand-coded country footprints: `company_id`, `iso3`, `coverage`, `scope`.
Sources are published country lists (the barometer networks), regional hub
partner lists, and known office and delivery-centre networks.

`scope` governs how the row interacts with the model:

- `exhaustive` (1,272 rows) — the list is complete. The firm's country coverage
  comes entirely from here and the model adds nothing.
- `partial` (1,006 rows) — these countries are observed. The model fills the rest
  of the firm's stated country budget around them, and hand-coded rows spend
  that budget first.

`partial` exists so that knowing a global firm's MENA and Africa offices does
not force a claim about its Latin American ones. Without it, partial knowledge
would shrink a footprint rather than improve it.

Grounding is uneven and the unevenness matters. The Russia bloc (38.1%) and
mainland China (37.0%) are best grounded, followed by MENA (18.0%), Sub-Saharan
Africa (17.5%), North America (14.2%), Western Europe (10.8%) and Latin America
(7.0%), against 10.5% for the file overall. Eastern Europe (2.1%), East Asia
(1.2%) and Oceania (0.7%) remain thin. Section 12 of `coverage_gaps.md` gives the
breakdown and what four rounds of hand-coding taught about building one.

### Observations override the feasibility gate

A hand-coded row survives even when the method and domain gates below would
empty it, falling back to the firm's own primary method. The gate is a model of
where a method can work; a hand-coded footprint is a record that the firm is
there. Impact-sourcing delivery centres are the clear case: Sama's operation in
Uganda supplies its own connectivity regardless of the national figure.

## `data/coverage_country.csv` (26,994 rows, 9 variables)

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
| `manual` | 2,534 | Observation. Hand-coded footprint. |
| `hq_exact` | 135 | Observation. Single-country firm resolved to its headquarters country. |
| `allocated` | 24,325 | Model output. |

Rows are written for exited firms too, recording the footprint they had, and are
filtered out of the current-coverage tables by `01_load.R`.

**90% of rows are model output**, falling to about 62% for the Russia bloc and
mainland China, which are the best-grounded regions in the file. An `allocated` row says where a firm of that
type, regional footprint and stated country count most likely operates. It is
not a claim that the firm operates there. Aggregate country counts are usable;
an individual firm's row is not citable.

`scripts/04_country_gaps.R` reports every country-level regression twice, once
on the full file and once on the 2,316 observed rows only (`tab19_sensitivity`).
A result that appears only in the full column is a property of the allocation
rule.

**The comparison must hold the outcome variable constant.** Column 1 of
`tab19_sensitivity` counts primary collectors over the whole file and column 2
counts them over observed rows only, differing in basis and nothing else. Column
3 counts all providers on observed rows and is shown only as a warning: it is not
like-for-like, because hand-coded footprints are far easier to establish for
satellite and open-source firms than for survey firms, so every round of
hand-coding shifts the all-firm observed sample toward firms that never contact a
person. Comparing columns 1 and 3 produced a false collapse of the
restrictive-regime result, described in section 8 of `coverage_gaps.md`.

On the corrected test, **population, connectivity and restrictive research regime
survive**, conflict exposure is a consistent null, and income reverses sign and
remains unreportable. The rank correlation between full and observed
primary-collector counts is 0.797.

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
| Requires internet `medium` or `high` | `online_panel`, `device_passive`, `mobile_app`, `crowd_task`, `expert_elicit`, `crowd_sensor`; domains `device_telemetry`, `mobility_location` |
| Requires income `UMIC` or `HIC` | `clinical_records`; domains `financial_transactions`, `credit_risk` |
| Requires both | `transaction`; `health_clinical` and `prices_retail` where the firm's primary method is record- or transaction-based |
| Ungated | `face_to_face`, `telephone`, `web_scrape`, `api_partner`, `admin_records`, `remote_sensing`, `sensor_hardware`, `telecom_network`, `environmental_sample`, `acoustic`, `signals_rf` |

`crowd_sensor` is gated because a contributor-owned sensor network needs someone
on the ground who can buy the hardware and upload from it. The three ungated new
methods need nobody on the ground at all, which is why they reach every country
and `crowd_sensor` reaches 61. Section 15 of `coverage_gaps.md` treats that split
as the main finding about the collection frontier.

An `allocated` row with no usable method, or no obtainable data type, is not
written. A `manual` or `hq_exact` row is always written, because the observation
overrides the gate.

Method repertoires come from the firm's `modality_primary` plus the methods its
segment can deploy, listed in `SEGMENT_METHODS` in the build script.
