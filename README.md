# The Global Data Collection Industry

A register of 424 organisations that collect data as their business, coded for
where they collect it and what they collect it about, built to make the gaps
visible rather than the coverage.

The question behind it: for any given place and any given subject, who is
actually gathering the data, and what is nobody gathering?

## What is in here

| File | Rows | What it is |
|---|---|---|
| `data/companies.csv` | 424 | The register. One row per organisation, 24 variables. |
| `data/coverage_spatial.csv` | 424 | Ordinal 0-3 coverage score for each firm across 12 world regions. |
| `data/countries.csv` | 194 | Country reference: region, income group, population band, connectivity, conflict exposure, research-regime restriction. |
| `data/coverage_country_manual.csv` | 1,709 | Hand-coded country footprints for 120 organisations, marked exhaustive or partial. |
| `data/coverage_country.csv` | 21,728 | Company-by-country coverage, each row carrying the methods usable and the data types obtainable in that country. |
| `data/segments.csv` | 22 | Industry segment taxonomy. |
| `data/domains.csv` | 26 | Substantive domain taxonomy. |
| `data/regions.csv` | 12 | Region definitions. |
| `data/modalities.csv` | 15 | Collection method taxonomy. |
| `docs/codebook.md` | | Every variable, every coding rule. |
| `docs/coverage_gaps.md` | | The findings. |
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

Both startups and established firms are included by design: 188 established,
192 scaleups, 44 startups, founded between 1841 and 2024. 92 firms are
headquartered in MENA or Sub-Saharan Africa, which is where enumeration effort
has been concentrated.

Pure analytics vendors, consultancies and platforms that only process data
others collected are out of scope. Government statistical offices are out of
scope as producers, though firms that resell their output are in.

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
- Balancing the hand-coded sample across five regions restored the observed-only
  sensitivity check: the rank correlation between modelled and observed country
  provider counts rose from 0.094 to **0.535**, and a restrictive-research-regime
  result that had to be retracted one revision ago now holds at −0.29 and −0.30
  across both columns.
- **55.9%** of firms are headquartered in North America or Western Europe, rising
  to **80.7%** of venture and private-equity backed firms. Of 46 firms founded
  since 2019, 29 are in those two regions and 9 are in Sub-Saharan Africa, where
  new entry is in African-language AI training data, geospatial and alternative
  credit rather than in survey research.
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
3. **Country coverage is mostly model output.** Of 21,728 company-country rows,
   1,816 are observed (`manual` or `hq_exact`) and 19,912 are allocated by the
   model in `scripts/00_build_country_coverage.py`. Country aggregates are
   usable; an individual firm's country row is not citable. Report nothing from
   the country regressions that does not hold in both columns of
   `output/tab19_sensitivity.txt`: at present that means population,
   connectivity and restrictive research regime, and not income.
4. **Grounding is uneven across regions.** Five regions are between 7% and 16%
   observed (MENA, North America, Sub-Saharan Africa, Western Europe, Latin
   America); the other seven are between 0.7% and 3.5%. The Russia bloc (3.5%)
   and mainland China (3.4%) carry a specific risk, because they are the regions
   this register claims are least covered and among those where the claim rests
   least on observation.
5. **The register is not a census.** Private firms in this industry do not have
   to announce themselves, and the smallest national field agencies are the
   hardest to enumerate. Coverage of MENA, Sub-Saharan Africa and the post-Soviet
   space reflects deliberate effort, but Central Asia, Central America and the
   Pacific are certainly under-enumerated, as are the Gulf states, where most
   collection runs through a small number of licensed intermediaries that do not
   advertise. Under-counting
   small local firms biases the findings toward *understating* how much
   collection happens outside the core, which cuts against this document's own
   argument and should be held in mind.
6. **Revenue, headcount and valuation are excluded.** Reliable figures exist for
   perhaps a fifth of the register, and a column that is mostly missing invites
   misuse. What could be verified is in the `notes` field with its source in
   `docs/sources.md`.
7. **The snapshot is September 2026.** This industry consolidates fast. Recent
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

The highest-value additions, in order: **hand-coded footprints for the Russia
bloc, mainland China, East Asia, Eastern Europe and Oceania**, the five regions
still under 3.5% observed, and the first two especially, since the register's
strongest claims are about them; national field agencies in Central Asia, Central
America and the Pacific, where enumeration is thinnest; a time dimension so
entry, exit and acquisition can be tracked; and verified revenue for the subset
where filings exist.

To replace model rows with observations for a firm, add its countries to
`data/coverage_country_manual.csv` and rerun the build. Mark the rows
`exhaustive` if you know the firm's complete footprint, or `partial` if you know
only part of it and want the model to fill the rest. The `basis` counts printed
by the build script tell you how much of the file is still modelled.
