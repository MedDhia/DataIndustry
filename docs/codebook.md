# Codebook

All files are UTF-8 CSV with a header row. `NA` denotes a value that is unknown or
does not apply. Multi-valued fields use `|` as the separator. `company_id` is the
primary key across every file.

## `data/companies.csv` (923 rows, 26 variables)

The register includes 842 operating organisations and 81 that no longer operate.
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
| `ownership_type` | factor | `public_listed`, `private_pe`, `private_vc`, `private_independent`, `subsidiary`, `nonprofit`, `academic`, `state_linked`, `cooperative_jic`. Who holds the equity. |
| `sector` | factor | `for_profit`, `nonprofit`, `academic`, `governmental`. What kind of organisation it is. See below. |
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

### `sector`

Four values, one per organisation, derived by `scripts/00_code_sector.py`.

- `for_profit` - trades commercially and distributes surplus to owners, whoever
  those owners are. **A state-owned joint stock company selling research is
  `for_profit` here**; `ownership_type` records that the state owns it.
- `nonprofit` - legally constituted not-for-profit, independent of government.
- `academic` - a university, a unit of one, or a research institute whose
  primary output is scholarship.
- `governmental` - an organ of the state, a body created by statute or decree
  and controlled by government, or an intergovernmental organisation.

**`sector` and `ownership_type` are not redundant and should both be used.**
`ownership_type` says who holds the equity; `sector` says what kind of
organisation it is. They come apart in fourteen cases, every one of them listed
with its reason in `scripts/00_code_sector.py`: state-owned firms that trade
commercially (VCIOM, Mediascope, SberIndex, CTR, CSM, Chang Guang, Twenty First
Century Aerospace, Elm, M42), a state-tied Russian polling foundation that is
constituted as a foundation rather than an organ of state (FOM), two state-linked
academic bodies (ISPA Iran, CREAD Algeria), a credit bureau created by federal law
(Al Etihad), and 23andMe, which operated as a listed for-profit for its entire
collecting life and was only acquired by a nonprofit out of bankruptcy.

Joint industry committees (BARB, OzTAM, BARC India, Numeris, AGF, Auditel,
Marocmétrie) are coded `nonprofit`. They are owned by broadcasters and
advertisers, sell nothing on the open market, and exist to produce a measurement
currency their members trade on. That is a defensible call rather than an obvious
one, and anyone who disagrees can move all seven with one line.

The derivation is a rule plus an override list rather than hand-entered values,
so it is auditable and reruns cleanly when the register grows. The validator
enforces the vocabulary and two consistency rules: a nonprofit or academic owner
cannot be `for_profit`, and listed, private equity or venture backed firms must be.

### `maturity_class`

- `established` - operating more than roughly twenty years, or listed, or held at
  scale by private equity.
- `scaleup` - growth stage, typically founded between 2006 and 2018.
- `startup` - founded 2019 or later, or still at seed or Series A.

Age and stage are recorded separately (`founded_year`, `ownership_type`) so that
users who dislike this cut can build their own.

### `evidence_level`

This variable describes the coding, not the firm. It is the honest limit of the
dataset and should be reported in anything built on it.

- `A` - verified against a regulatory filing or a source retrieved during
  construction, and cited in `docs/sources.md`.
- `B` - consistently reported across multiple independent public sources.
- `C` - analyst judgement from domain knowledge. Directionally reliable for
  segment, region and modality; not reliable for dates or counts.

Current distribution over operating firms: A 59, B 192, C 262. Treat every `C` figure as an ordinal
placement rather than a measurement.

## `data/coverage_spatial.csv` (923 rows, 14 variables)

`company_id`, `coverage_basis`, then one column per region code.

Coverage is ordinal:

| Score | Meaning |
|---|---|
| 0 | No meaningful coverage. |
| 1 | Thin. A handful of countries, resold supply, or a nominal claim. |
| 2 | Substantial. Own operations or a dense dataset across much of the region. |
| 3 | Deep. Flagship coverage; the firm is a reference source for the region. |

`coverage_basis` records how the row was produced:

- `manual` (113 rows) - hand-coded from specific knowledge of the firm.
- `segment_template` (311 rows) - derived by the documented rule in
  `scripts/00_build_coverage.py` from segment, `spatial_scope` and focus region.
  For the single-country and single-region field agencies that make up most of
  these rows the rule is near-exact. For globally scoped firms it is an
  assumption, and those rows should be hand-checked before load-bearing use.

A score of 2 is the threshold used throughout the analysis to mean "present".

## Derived matrices

`scripts/01_load.R` constructs two matrices used by everything downstream.

- `spatial_mat` - firms by regions, ordinal 0-3.
- `domain_mat` - firms by domains, weight 2 for a primary domain, 1 for a
  secondary domain, 0 otherwise.

`scripts/03_coverage_gaps.R` writes long-format versions to `output/`.

## `data/ownership.csv` (258 rows, 111 organisations)

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

Every founder attribution has been checked against sources, in three passes: the
seventeen coded at level C, the sixty-five coded at level B, and an audit of the
level A rows themselves. Founder rows now carry 132 at level A and one at level
B, the exception being a MetroPOLL co-founder resting on a single Turkish source.

Founder rows now carry 136 at level A and three at level B. Every organisation
in the founder layer has been searched with the question framed as enumeration,
asking who founded it rather than whether the recorded person did, so founder
counts per organisation are usable rather than a lower bound. Two qualifications
hold. Six organisations call their own founder a co-founder or refer to a founding
group while naming nobody else, and their notes say so: Baseera, JMCC, the Syrian
Center for Policy Research, One to One, UjuziKilimo and Digital Umuganda. And 36
organisations are recorded with a single founder because the sources name one,
which for most of them means no source addressed the question directly; only Surge
AI, Sama and Ipsos are positively confirmed as single-founder.

The enumeration framing is what makes the difference, and it is worth stating for
anyone extending this file. A search asking whether X founded Y returns a
confirmation and stops. A search asking who founded Y returns the list. The first
two verification passes used the first framing and produced no false positives and
a systematic undercount; twenty-nine founders were added once the framing changed.

Three attributions failed verification and were changed. Near East Consulting was
attributed to Jamil Rabah through a name collision with an unrelated Lebanese
consultancy. Bell Ihua was recorded as founder of the Africa Polling Institute
when he is its executive director; no source establishes who founded it. Both
company rows carry notes saying so. KoboToolbox was attributed to the Harvard
Humanitarian Initiative as an institution; it was founded in 2005 by Phuong Pham
and Patrick Vinck and hosted at HHI, which now appears as a funder rather than a
founder.

The verification passes also corrected twelve founding years in `companies.csv`,
four of which moved an organisation between `maturity_class` values. Anyone using a
version of this register from before that pass should re-pull `companies.csv`
rather than patch it. Two organisations, Research World International and
Geocartography, have confirmed founders and founding years that no public source
establishes; their `notes` say so and their `founded_year` should not be trusted.

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

- `data/regions.csv` - twelve regions. Mainland China and the Russia/Belarus/
  Central Asia bloc are separated from their neighbours because exclusion from
  them is one of the strongest patterns in the industry.
- `data/segments.csv` - twenty-three segments, each tagged `solicited` (data is
  produced by asking someone) or `observational` (data is captured from traces).
- `data/domains.csv` - twenty-seven substantive domains.
- `data/modalities.csv` - nineteen collection methods, each tagged by whether it
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

- `exhaustive` (1,272 rows) - the list is complete. The firm's country coverage
  comes entirely from here and the model adds nothing.
- `partial` (1,006 rows) - these countries are observed. The model fills the rest
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

## `data/coverage_country.csv` (33,393 rows, 9 variables)

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

- `market` - income, population, connectivity. Firms selling data about a
  country's consumers or firms.
- `labour` - population, connectivity, low income. Annotation and micro-task
  firms, whose country coverage describes where their *workers* are, not who
  they collect data about.
- `need` - low income, conflict exposure, population. Firms whose clients are
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

## `data/grant_programmes.csv` (15 rows, 20 variables)

Recurring open-call funding instruments that a data collection venture could apply to.
One row per programme, not per award and not per organisation. See
`docs/grant_programmes.md` for what the layer shows and what was deliberately left out.

| Variable | Type | Description |
|---|---|---|
| `programme_id` | key | Stable identifier. |
| `programme_name` | string | Programme as the funder names it. |
| `funders` | list | Pipe-delimited. Names match `ownership.csv` spelling where the funder appears in both. |
| `funder_country` | ISO3 | Where the lead funder is based. |
| `funder_category` | factor | `foundation`, `bilateral_donor`, `multilateral`, `state`, `nonprofit`, `corporate`, `university`. |
| `instrument_type` | factor | `grant`, `prize`, `equity_free_investment`, `convertible`, `state_subsidy`, `fellowship`. |
| `cadence` | factor | `annual`, `biennial`, `rolling`, `thematic_rounds`, `one_off`. |
| `geography_scope` | factor | `global`, `multi_region`, `single_region`, `single_country`. |
| `eligible_regions` | list | Pipe-delimited region codes from `regions.csv`. |
| `award_min_usd`, `award_max_usd` | integer | Approximate US dollar equivalents of the published range. Converted at the rate prevailing when the round was announced, so treat as an order of magnitude. |
| `stage_targeted` | factor | `idea`, `seed`, `early`, `growth`, `any`. |
| `data_specific` | factor | `yes` the programme exists to fund data work; `partial` a data venture is eligible within a broader remit; `no` data ventures compete against all sectors. |
| `thematic_focus` | string | Free text, no commas. |
| `status` | factor | `open`, `dormant`, `discontinued`. |
| `first_year`, `ended_year` | integer | `ended_year` is `NA` unless `status` is `discontinued`; the validator enforces both directions. |
| `evidence_level` | factor | `A`, `B`, `C`, as elsewhere. All current rows are `A`. |
| `url` | string | Funder's own page for the programme. |
| `notes` | string | Short free text, no commas. |

**Award figures are approximate and currency-converted.** Several programmes publish in
pounds, euros or Canadian dollars, and some state a total pool rather than a per-award
range. Use the range to sort programmes into bands, not to compare two programmes a
thousand dollars apart.

**A shared funder name is not a grant receipt.** Six programmes have a funder that also
appears in `ownership.csv`. That means the funder is active in this industry, not that
any organisation in `companies.csv` won money through that programme. `07_grants.R`
prints the overlap with that caveat attached.

## `data/demand.csv` (92 rows, 14 variables)

The buyer side. One row per segment and buyer category, not per buyer and not per
contract. It is a purposive record of buying that could be documented, not a census of
demand, and the evidence is unevenly available by construction: public procurement
leaves award notices and commercial subscription leaves nothing. See `docs/demand.md`,
section 2, for what that does to the composition of the file.

| Variable | Type | Description |
|---|---|---|
| `demand_id` | key | Stable identifier. |
| `segment` | factor | Segment code from `segments.csv`. All 23 segments have at least two rows. |
| `buyer_category` | factor | `government_security`, `government_civil`, `multilateral_donor`, `financial_investor`, `financial_lender`, `insurance`, `pharma_health`, `corporate_marketing`, `corporate_operations`, `media_advertising`, `ai_developer`, `retail_cpg`, `academic_research`, `ngo_advocacy`, `research_intermediary`, `political_party`. |
| `buyer_examples` | list | Pipe-delimited named buyers, or `NA` where the category is documented but no buyer is named. |
| `procurement_mode` | factor | `subscription`, `one_off_commission`, `framework_contract`, `marketplace_api`, `licensing_deal`, `membership_levy`, `grant_funded`, `panel_rental`. |
| `contract_visibility` | factor | `public_award`, `disclosed_deal`, `trade_reported`, `opaque`. How the transaction enters the public record, not how good the evidence is. |
| `geography` | factor | Region code from `regions.csv`, or `global`. |
| `direction` | factor | `rising`, `stable`, `declining`, `contested`. A judgement, justified in `notes` on every row. `contested` marks demand that exists and is under legal or regulatory challenge. |
| `price_signal_usd` | integer | A documented figure in US dollars, or `NA`. Present on 13 rows. |
| `price_signal_basis` | factor | What the figure measures: `contract_total`, `contract_annual`, `buyer_annual`, `market_annual`, or `NA`. The validator requires this and `price_signal_usd` to be `NA` together. |
| `signal_year` | integer | Year the figure refers to, or `NA`. |
| `evidence_level` | factor | `A` a named buyer with a public award or a deal the parties disclosed; `B` a buyer category documented in named trade or press reporting; `C` an inference from the segment's structure. 17 A, 54 B, 21 C. |
| `url` | string | Source. |
| `notes` | string | Free text, quoted in the CSV where it contains commas. Carries the justification for `direction` and any caveat on the source. |

**Evidence A is enforced, not asserted.** The validator rejects an `A` row that has no
named buyer or whose `contract_visibility` is not `public_award` or `disclosed_deal`.

**Price signals are not comparable across rows.** A ten-year contract ceiling, one
buyer's annual spend and a whole market's annual size are three different quantities and
all three appear in the column. `price_signal_basis` says which, and nothing should be
summed across bases.

**Direction is the softest variable in the file.** It rests on the source behind the row
and on the entry and exit figures in section 1 of `docs/demand.md`, and it is a reading,
not a measurement. Treat it as a hypothesis to check rather than as data.

## `data/method_innovations.csv` (69 rows, 10 variables)

One row per organisation whose entry rested on a collection method its segment
did not already have. Not a scoring of how good a firm is, and not a ranking. The
test applied to each candidate was narrow: name the method, name the practice it
displaced, and point at a source that establishes the firm uses it. A firm that
does the same thing better, cheaper or at larger scale is not in this file.

| Variable | Type | Description |
|---|---|---|
| `innovation_id` | key | Stable identifier, prefixed `in_`. |
| `company_id` | key | Foreign key to `companies.csv`. One row per company; the validator rejects a second. |
| `novelty_type` | factor | `new_sensor`, `new_substrate`, `new_sampling_frame`, `new_inference`, `new_incentive`, `new_contract`. Defined in `docs/method_innovation.md` section 2. |
| `novel_element` | string | What the method is, in one clause. |
| `displaces` | string | The practice it competes against, which is often not another firm but a statistical office, a ranger patrol or a clinic. |
| `first_deployment_year` | integer | The year THIS firm first deployed the method, or `NA`. Where the method predates the firm, as in a spinout, the earlier history goes in `notes` and this field stays with the firm. The validator rejects a deployment year before the company's founding year. |
| `contested` | factor | `yes` if the method itself has drawn litigation, regulatory action or sustained documented accuracy disputes; `no` otherwise. Commercial disputes and ordinary competition do not count. |
| `evidence_level` | factor | `A`, `B`, `C`, as elsewhere. |
| `url` | string | Establishes WHAT the method is, for which the firm is an acceptable authority. It does not establish that the method works. Performance claims stay in the `companies.csv` notes and are marked there as vendor claims. |
| `notes` | string | Free text, quoted in the CSV where it contains commas. |

**Prior occupants are derived, not stored.** `scripts/10_innovation.R` counts the
organisations already in a firm's segment at its first deployment year. Storing
that number would go stale on the next extension round, and it is a property of
this register's enumeration depth as much as of the industry. Read it within a
segment, not across segments.

**Five modality codes were added across the two method rounds**, taking
`data/modalities.csv` from 19 to 24: `fiber_das`, `web_intercept`, `rf_sensing`,
`device_extraction` and `citizen_report`. Each was added because coding the firm
with an existing modality would have misdescribed what it does. `rf_sensing` is
distinct from `signals_rf`, which is the geolocation of emitters, and from
`sensor_hardware`, which assumes something was installed for the purpose.
`device_extraction` and `citizen_report` sit at opposite ends of one axis: in
both the person is the source, but in the first they are never asked and cannot
refuse, and in the second they decide both whether to report and what counts as
reportable.

**`consent_model` gained `no_consent_basis`** in the MENA and Africa round, for
collection that proceeds without any consent from the subject and without a
public-record or contractual basis. The earlier vocabulary had no code for it,
because it was built by reading firms that all claimed a consent basis of some
kind. `not_applicable` does not cover it: that code means there is no human
subject. Four organisations carry the new value and all four sell access to the
contents of a person's phone.
