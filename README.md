# The Global Data Collection Industry

A register of 569 organisations that collect data as their business, 513 of them
still operating, coded for
where they collect it and what they collect it about, built to make the gaps
visible rather than the coverage.

The question behind it: for any given place and any given subject, who is
actually gathering the data, and what is nobody gathering?

## What is in here

| File | Rows | What it is |
|---|---|---|
| `data/companies.csv` | 569 | The register. One row per organisation, 25 variables. 513 operating, 56 exited. |
| `data/coverage_spatial.csv` | 569 | Ordinal 0-3 coverage score for each firm across 12 world regions. |
| `data/countries.csv` | 194 | Country reference: region, income group, population band, connectivity, conflict exposure, research-regime restriction. |
| `data/coverage_country_manual.csv` | 2,534 | Hand-coded country footprints for 212 organisations, marked exhaustive or partial. |
| `data/coverage_country.csv` | 26,994 | Company-by-country coverage, each row carrying the methods usable and the data types obtainable in that country. |
| `data/segments.csv` | 23 | Industry segment taxonomy. |
| `data/domains.csv` | 27 | Substantive domain taxonomy. |
| `data/regions.csv` | 12 | Region definitions. |
| `data/modalities.csv` | 19 | Collection method taxonomy. |
| `docs/codebook.md` | | Every variable, every coding rule. |
| `data/ownership.csv` | 212 | Founders, owners, investors and funders for 113 organisations. Partial and purposive; read the codebook before computing anything from it. |
| `docs/coverage_gaps.md` | | The findings. |
| `scripts/05_history.R` | | Exit, absorption and survivorship analysis. |
| `docs/sources.md` | | Sources consulted during construction. |

## Scope

An organisation is in the register if collecting or assembling data is the
business rather than a by-product. That includes commercial firms, and also the
nonprofits, academic centres and industry cooperatives that hold the field in
places where no commercial market exists: excluding them would have produced a
badly distorted picture of Sub-Saharan Africa, the post-Soviet space and conflict
settings.

Deliberately covered together:

- **Solicited collection** — survey firms, panels, field agencies, crowd tasking,
  AI training data, expert networks. Someone is asked something.
- **Observational collection** — brokers, web scraping, location and telemetry,
  earth observation, health records, trade and financial traces. Something is
  captured.

Keeping both in one frame is the point. The industry's apparent global reach
comes almost entirely from the observational side, and that only becomes visible
when the two are measured on the same grid.

Both startups and established firms are included by design, and so are firms that
no longer exist. 56 organisations in the register have exited: 46 absorbed into
an acquirer, 10 wound down or insolvent. Without them this would be a survivor
sample of an industry that has consolidated hard. **Every coverage and gap table
uses the 513 operating firms only**; `scripts/05_history.R` analyses the rest.

128 firms are headquartered in MENA or Sub-Saharan Africa and 20 in the Russia
bloc or mainland China, the areas where enumeration effort has been concentrated.

Pure analytics vendors, consultancies and platforms that only process data
others collected are out of scope, and so are hardware suppliers that build
sensors or satellite payloads without operating them. Government statistical
offices are out of scope as producers, though firms that resell their output are
in. State agencies that operate collection systems, such as national space
agencies, are in and are coded `state_linked`.

## Headline findings

- Only **3.8%** of the 312 region-by-domain cells have no provider at all, but
  **19.9%** have no provider whose record-level data a researcher can obtain.
  The binding constraint is access, not existence.
- Nominal presence varies 3.5 to 1 between the best and worst served region.
  Direct contact with human subjects varies **7.6 to 1**. Global coverage is
  produced by methods that never touch a person.
- Remote sensing is the only collection method with uniform world coverage.
  Online panels are five times denser in North America than in Sub-Saharan
  Africa; face-to-face interviewing runs the other way.
- Countries that legally gate independent research have fewer organisations
  making direct contact with their populations than their size and connectivity
  predict (−0.27 on the full file, −0.23 on hand-coded rows). This result was
  reported, retracted, reinstated and apparently overturned across four
  revisions before a fault in the sensitivity test was found and fixed; section 8
  of `coverage_gaps.md` keeps the whole sequence visible.
- Russia capped foreign ownership of market research firms at 20% with data
  localisation from 1 March 2026. Ipsos sold 80% of Ipsos Comcon that February
  and Nielsen moved to divest. Mediascope, which measures Russian media, is 80%
  owned by the state pollster VCIOM.
- **52.1%** of firms are headquartered in North America or Western Europe, down
  from 62.7% as enumeration deepened. Of 62 firms founded since 2019, 31 are
  North American but **21 are MENA or African** — a third of new entry.
- What the new firms build splits by region. Not one of the 21 MENA and African
  startups is in survey and insights; 12 of the 37 Northern ones are. The North
  is building new ways to ask questions (AI-moderated interviewing, population
  simulation); the South is building collection capacity that did not exist
  (African-language and Arabic-dialect corpora, field sensing, clinical records).
- **The newest participatory method is less geographically even than the oldest
  one.** Contributor-operated sensor networks reach 75 countries, 100% of North
  America and Western Europe against 38% of Sub-Saharan Africa and 33% of MENA.
  Face-to-face interviewing reaches 193 of 194. Radio frequency geolocation
  reaches all 194 with three firms, because listening for radio emitters from
  orbit needs no participant at all. The frontier splits between methods that
  need someone on the ground and methods that do not.
- **Africa and MENA now hold more earth observation organisations than North
  America**, 23 against 21, but seven are state agencies and North America has
  none. Four of the seven release nothing outside government, so the locally
  operated layer is less accessible than the Northern commercial one it sits
  beside. The continental market is worth about $77m.
- **Openness tracks grant funding, not public ownership.** Academic and nonprofit
  collectors publish at 90%. State-linked collectors publish at **11.1%**, below
  venture-backed firms at 19.6% and second-lowest of any ownership type.
- **Locally founded, externally funded.** MENA and African data organisations
  are founded by nationals of the country at 88%, almost the same rate as
  Northern ones at 89%. But **62 of 66 established funding relationships (93.9%)
  have a funder in North America or Western Europe**, and only two of the four
  exceptions are independently non-Northern: the Qatar National Research Fund and
  the South African Institute of International Affairs. The expertise and the
  decisions are largely domestic; the budget line is not.
- **The open layer is the part of this industry that can disappear rather than
  change hands.** A commercial firm that loses its market gets bought and its data
  continues under a new owner; every MENA and African field agency that exited was
  acquired. A grant-funded collector that loses its funder has no acquirer,
  because there was never a revenue stream to buy. Former USAID Africa Bureau
  officials have publicly urged the agency to save Afrobarometer's funding.
- **None of the token-incentivised sensor networks reaches Africa.** Contributor
  sensing there is supplied by a Ugandan university lab publishing openly, a
  South African civic-data nonprofit, a Kenyan soil-sensor firm and two Northern
  organisations. Where the commercial case is thin, what gets built is
  grant-funded, and what is grant-funded is published.
- Wastewater epidemiology, acoustic monitoring and RF geolocation measure
  populations with **no consent mechanism and no identifiable data subject**.
  Seven firms return empty on every consent variable the register records, the
  same blank the synthetic research firms produce from the opposite direction.
- Three firms sit in a solicited segment while contacting nobody. Two are new:
  **Aaru** and **Simile** simulate respondents rather than recruiting them, and
  are capitalised at a scale comparable to the largest panel businesses.
- Consolidation is wildly uneven. **35%** of mobile location firms ever recorded
  here have exited, and **32%** of consumer data brokers, against **4.9%** of
  in-country field agencies. The venture-funded, technologically novel end of the
  industry is the fragile end; the part that persists is an enumerator network
  and a long relationship with a statistical office.
- **Every MENA and African field agency that has exited was bought, not closed.**
  Markinor, Steadman, AMRB, RMS Nigeria, Repucom Africa, Compuscan and Omedia
  were all absorbed by Ipsos, Kantar, Nielsen or Experian, four of them between
  2007 and 2010. Much of what the register records as global-firm coverage of
  Africa and the Gulf was bought, not built. The two Southern firms that did
  close were venture-funded technology startups, not agencies.
- **Not one exited firm had record-level data a researcher could obtain.** The
  access gap is a ratchet: collection accumulates and the routes to it close on
  acquisition or failure without ever opening. 23andMe's 15 million genomes went
  to a bankruptcy auction in 2025 under consent that governed collection, not
  sale.
- Identity, biometric and credit data is collected in all twelve regions and
  released to outside researchers in none. At country level, identity data is
  obtainable in 165 countries and accessible in zero.
- Every one of 194 countries has at least one collector, and the minimum is 28.
  Turkmenistan, the least served, has 29 organisations collecting data about it
  and **not one that speaks to a Turkmen**. The floor beneath every country is
  satellites and web crawlers.
- The number of distinct collection methods available falls from 14.0 in
  high-income countries to 8.8 in low-income ones. Transaction data exists in
  28 countries of 194; credit data in 103.
- Identity and biometric data is obtainable in 165 countries and accessible to
  an outside researcher in 5, all of them through one Rwandan nonprofit's open
  speech corpora.

`docs/coverage_gaps.md` has the full argument.

## Reproducing the analysis

```sh
python3 scripts/00_build_coverage.py          # region coverage matrix
python3 scripts/00_build_country_coverage.py  # country coverage, typed by method and domain
python3 scripts/00_validate.py                # check every file against every vocabulary
Rscript  scripts/02_descriptives.R            # descriptive tables -> output/
Rscript  scripts/03_coverage_gaps.R           # region gap analysis -> output/
Rscript  scripts/04_country_gaps.R            # country gap analysis -> output/
Rscript  scripts/05_history.R                 # exits and survivorship -> output/
Rscript  scripts/06_ownership.R               # founders, owners and funders -> output/
```

Requires R with `stargazer`, and Python 3 for the matrix builder. Tables are
written to `output/` in both plain text and LaTeX. `scripts/01_load.R` builds the
derived matrices and is sourced by the analysis scripts.

## Limitations

Read these before using the data for anything load-bearing.

1. **Coding confidence is uneven and recorded.** The `evidence_level` variable is
   A for 29 records, B for 153 and C for 242. Level C is analyst judgement:
   reliable for segment, region and modality, not reliable for founding dates or
   counts. Filter on it.
2. **Region coverage is partly rule-derived.** 113 of 424 spatial rows are
   hand-coded; the remaining 311 come from the documented segment templates in
   `scripts/00_build_coverage.py`. For single-country and single-region field
   agencies the rule is near-exact. For globally scoped firms it is an
   assumption, and `coverage_basis` marks which is which.
3. **Country coverage is mostly model output.** Of 22,102 company-country rows,
   2,316 are observed (`manual` or `hq_exact`) and 19,786 are allocated by the
   model in `scripts/00_build_country_coverage.py`. Country aggregates are
   usable; an individual firm's country row is not citable. Report nothing from
   the country regressions that does not hold in the first two columns of
   `output/tab19_sensitivity.txt`: population, connectivity and restrictive
   research regime, and not income.
4. **The sensitivity test must hold the outcome constant, and for three
   revisions it did not.** Hand-coded footprints are far easier to establish for
   satellite and open-source firms than for survey firms, so every round of
   hand-coding shifts the observed sample toward firms that never contact a
   person. Comparing a full-file count of primary collectors against an all-firm
   observed count reads that compositional shift as a change in the world. It
   produced one false retraction. The test now compares primary collectors
   against primary collectors; the third column is kept as a warning.
5. **Grounding is uneven across regions.** The Russia bloc (38.1%) and mainland
   China (37.0%) are best grounded, then MENA (18.0%), Sub-Saharan Africa
   (17.5%), North America, Western Europe and Latin America between 7% and 15%. Eastern Europe (2.1%),
   East Asia (1.2%) and Oceania (0.7%) remain thin; Eastern Europe matters most,
   because the register makes claims about wartime Ukraine and the Western
   Balkans on 2.1% observation.
6. **Exits are enumerated worse than survivors, and acquisitions better than
   closures.** An acquirer issues a press release; a firm that winds up quietly
   does not. Every MENA and African exit in this register was established from an
   acquisition announcement, and a direct search for African research agency
   closures returns directories of operating firms and nothing else. The 4.9%
   field agency exit rate is a floor carrying two biases, Northern and
   acquisition-shaped. It is not a hazard rate.
7. **The register is not a census.** Private firms in this industry do not have
   to announce themselves, and the smallest national field agencies are the
   hardest to enumerate. Coverage of MENA, Sub-Saharan Africa and the post-Soviet
   space reflects deliberate effort, but Central Asia, Central America and the
   Pacific are certainly under-enumerated, as are the Gulf states, where most
   collection runs through a small number of licensed intermediaries that do not
   advertise. Under-counting
   small local firms biases the findings toward *understating* how much
   collection happens outside the core, which cuts against this document's own
   argument and should be held in mind.
8. **The ownership layer covers a third of the register and is purposively
   selected.** `data/ownership.csv` records relationships that could be
   established from sources, concentrated on openly accessible collectors and on
   MENA and African firms. Absence of a row means not established. Do not compute
   register-wide shares from it.
9. **Revenue, headcount and valuation are excluded.** Reliable figures exist for
   perhaps a fifth of the register, and a column that is mostly missing invites
   misuse. What could be verified is in the `notes` field with its source in
   `docs/sources.md`.
10. **The snapshot is September 2026.** This industry consolidates fast. Recent
   changes already reflected: Publicis acquiring LiveRamp, Experian acquiring
   AtData, Maxar becoming Vantor, Adobe acquiring Semrush, Meta's stake in
   Scale AI and the subsequent shift of frontier-lab demand to Surge, Mercor and
   Handshake.
7. **Region is a coarse unit.** MENA as one cell hides the difference between
   Tunisia, where several independent firms compete, and the Gulf, where almost
   all collection runs through a small number of licensed intermediaries. Country
   level coding is the obvious extension.

## Extending it

The schema is built for additions. To add a firm, append a row to
`data/companies.csv`, add the `company_id` to `MANUAL` in
`scripts/00_build_coverage.py` if you can code its regions directly, and rerun
both. `scripts/00_validate.py` checks every vocabulary value against the lookup
tables, every coverage score against its range, and the two files against each
other; it exits non-zero and names the offending records if anything fails, so it
works as a pre-commit hook.

The highest-value additions, in order: **hand-coded footprints for Eastern
Europe, East Asia, Southeast Asia and Oceania**, the regions still under 3.5%
observed, with Eastern Europe first because of Ukraine and the Western Balkans;
**more hand-coded footprints for survey and field firms specifically**, since the
observed sample is structurally biased toward satellite and open-source firms
whose coverage is easy to establish; national field agencies in Central Asia,
Central America and the Pacific; a time dimension so entry, exit and acquisition
can be tracked; and verified revenue for the subset where filings exist.

To replace model rows with observations for a firm, add its countries to
`data/coverage_country_manual.csv` and rerun the build. Mark the rows
`exhaustive` if you know the firm's complete footprint, or `partial` if you know
only part of it and want the model to fill the rest. The `basis` counts printed
by the build script tell you how much of the file is still modelled.
