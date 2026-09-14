# The Global Data Collection Industry

A register of 370 organisations that collect data as their business, coded for
where they collect it and what they collect it about, built to make the gaps
visible rather than the coverage.

The question behind it: for any given place and any given subject, who is
actually gathering the data, and what is nobody gathering?

## What is in here

| File | Rows | What it is |
|---|---|---|
| `data/companies.csv` | 370 | The register. One row per organisation, 24 variables. |
| `data/coverage_spatial.csv` | 370 | Ordinal 0-3 coverage score for each firm across 12 world regions. |
| `data/countries.csv` | 194 | Country reference: region, income group, population band, connectivity, conflict exposure, research-regime restriction. |
| `data/coverage_country_manual.csv` | 766 | Hand-coded country footprints for 62 organisations, marked exhaustive or partial. |
| `data/coverage_country.csv` | 21,249 | Company-by-country coverage, each row carrying the methods usable and the data types obtainable in that country. |
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

Both startups and established firms are included by design: 171 established,
167 scaleups, 32 startups, founded between 1841 and 2024.

Pure analytics vendors, consultancies and platforms that only process data
others collected are out of scope. Government statistical offices are out of
scope as producers, though firms that resell their output are in.

## Headline findings

- Only **4.2%** of the 312 region-by-domain cells have no provider at all, but
  **20.5%** have no provider whose record-level data a researcher can obtain.
  The binding constraint is access, not existence.
- Nominal presence varies 3.5 to 1 between the best and worst served region.
  Direct contact with human subjects varies **7.6 to 1**. Global coverage is
  produced by methods that never touch a person.
- Remote sensing is the only collection method with uniform world coverage.
  Online panels are five times denser in North America than in Sub-Saharan
  Africa; face-to-face interviewing runs the other way.
- **62.7%** of firms are headquartered in North America or Western Europe, rising
  to **87.7%** of venture and private-equity backed firms. Of 34 firms founded
  since 2019, 29 are in those two regions.
- Identity, biometric and credit data is collected in all twelve regions and
  released to outside researchers in none. At country level, identity data is
  obtainable in 165 countries and accessible in zero.
- Every one of 194 countries has at least one collector, and the minimum is 28.
  Turkmenistan, the least served, has 28 organisations collecting data about it
  and **not one that speaks to a Turkmen**. The floor beneath every country is
  satellites and web crawlers.
- The number of distinct collection methods available falls from 14.1 in
  high-income countries to 8.2 in low-income ones. Transaction data exists in
  27 countries of 194; credit data in 99.

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
   A for 21 records, B for 140 and C for 209. Level C is analyst judgement:
   reliable for segment, region and modality, not reliable for founding dates or
   counts. Filter on it.
2. **Region coverage is partly rule-derived.** 108 of 370 spatial rows are
   hand-coded; the remaining 262 come from the documented segment templates in
   `scripts/00_build_coverage.py`. For single-country and single-region field
   agencies the rule is near-exact. For globally scoped firms it is an
   assumption, and `coverage_basis` marks which is which.
3. **Country coverage is mostly model output, and this is the big one.** Of
   21,249 company-country rows, 852 are observed (`manual` or `hq_exact`) and
   20,397 are allocated by the model in `scripts/00_build_country_coverage.py`.
   Country aggregates are usable; an individual firm's country row is not
   citable. Every country regression is reported twice, once on the full file and
   once on observed rows only (`output/tab19_sensitivity.txt`). Population,
   income, connectivity and restrictive research regime survive that test.
   Conflict exposure does not. The region layer remains the more grounded one.
4. **Grounding is uneven by design.** Hand-coding is concentrated where the
   register is most used: MENA and Sub-Saharan Africa are about 10% observed,
   against 4% for the file overall and 0.2% for Western Europe. Country claims
   about those two regions rest on real footprints; claims about Western Europe,
   Oceania and East Asia are almost entirely model. The same asymmetry means the
   observed-only sensitivity column is a strong check for MENA and Africa and a
   weak one elsewhere.
5. **The register is not a census.** Private firms in this industry do not have
   to announce themselves, and the smallest national field agencies are the
   hardest to enumerate. Coverage of MENA, Sub-Saharan Africa and the post-Soviet
   space reflects deliberate effort, but Central Asia, Francophone West Africa,
   Central America and the Pacific are certainly under-enumerated. Under-counting
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

The highest-value additions, in order: **more hand-coded country footprints**,
which is the single change that would most improve the country layer, since it
replaces model rows with observations; national field agencies in Central Asia,
Francophone Africa and the Pacific, where enumeration is thinnest; a time
dimension so entry, exit and acquisition can be tracked; and verified revenue for
the subset where filings exist.

To replace model rows with observations for a firm, add its countries to
`data/coverage_country_manual.csv` and rerun the build. Mark the rows
`exhaustive` if you know the firm's complete footprint, or `partial` if you know
only part of it and want the model to fill the rest. The `basis` counts printed
by the build script tell you how much of the file is still modelled.
