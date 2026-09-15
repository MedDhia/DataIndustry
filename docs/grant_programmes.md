# Recurring grant programmes for data collection ventures

`data/grant_programmes.csv` records open-call funding instruments, not organisations
and not one-off awards. A programme qualifies if it runs on a repeating cadence, takes
unsolicited applications, and a data collection venture of the kind in this register
could plausibly be eligible. Fifteen programmes are recorded, fourteen open and one
discontinued.

**This is a purposive sample, not a census.** Programmes were included where the
cadence, award range and eligibility could be established from the funder's own pages
during a single research pass in September 2026. Several plausible candidates were left
out rather than coded from memory, named at the end. Nothing here should be read as a
population statistic, and the file is too small for any inferential use.

## What the layer holds

| Programme | Funder | Award range | Cadence | Data-specific |
|---|---|---|---|---|
| Lacuna Fund | Rockefeller, Google.org, IDRC, GIZ/BMZ | $25k-$250k | thematic rounds | **yes** |
| AI4D Responsible AI, Empowering People | IDRC, FCDO | $100k-$1m | thematic rounds | **yes** |
| GSMA Innovation Fund | GSMA, FCDO | £100k-£250k | annual | partial |
| Gates Foundation Grand Challenges | Gates Foundation | up to $500k | annual | partial |
| Grand Challenges Africa | Science for Africa Foundation | up to $200k | thematic rounds | partial |
| Grand Challenges Canada, Transition to Scale | GCC, Global Affairs Canada | CAD 300k-1.5m | thematic rounds | no |
| The DIV Fund | philanthropic consortium | $25k-$1m | rolling | partial |
| Tony Elumelu Foundation | TEF | $5,000 | annual | no |
| Fuzé by Digital Africa | Proparco, AFD | €20k-€100k | rolling | no |
| Mozilla Democracy x AI | Mozilla Foundation | $50k-$300k | annual | partial |
| Milken-Motsepe Prize | Milken Institute, Motsepe Foundation | $50k-$1m | annual | no |
| Africa Prize for Engineering Innovation | Royal Academy of Engineering | up to £50k | annual | no |
| ACSS Small Grants Program | Arab Council for the Social Sciences, Sida | $3k-$4k | annual | partial |
| Tunisia Startup Act | Tunisian state, Smart Capital | stipend, 1,000-5,000 TND/month | rolling | no |
| USAID Development Innovation Ventures | USAID | $25k-$15m | rolling | **discontinued 2025** |

## Five things the layer shows

**1. Only two programmes are actually designed for data collection.** Lacuna Fund and
AI4D are the only instruments in the file whose purpose is the production of datasets
and data capacity rather than something else that happens to admit data ventures. Seven
more are partial: the applicant can be a data venture provided it frames its work as
health, mobile inclusion, democracy or Arab-region research. The rest are
sector-agnostic startup money. **A founder building a data collection company in Africa
is applying, in most cases, to programmes that were designed for someone else.**

**2. The instrument that most resembled a data-collection funder is the one that
closed.** USAID's Development Innovation Ventures ran on a rolling basis from 2010 with
awards from $25,000 to $15m and a documented record of backing data-driven ventures.
Its FY2025 annual programme statement closed on 27 January 2025 and the programme ended
with the dissolution of USAID. A philanthropic successor, the DIV Fund, raised $20m in
emergency funding to rescue stranded grantees and has $28m committed over four years.
That replaces roughly the grant-making of a single large year, not the instrument.

This is the funding-contingency argument in section 17 of `coverage_gaps.md` happening
at instrument level rather than to an individual collector, and it is the reason this
file records discontinued programmes rather than only live ones.

**3. The FCDO is now the load-bearing public funder.** It co-funds both AI4D, at over
CAD 100m, and the GSMA Innovation Fund. With USAID gone, one bilateral donor and a small
number of American foundations sit behind most of the open-call money that a data
collection venture in a low or middle income country can apply for. Concentration of
this kind is what section 17 documents on the recipient side; the instrument side is at
least as concentrated.

**4. Eligibility is heavily African, and thinner for MENA.** Twelve of the fourteen open
programmes admit Sub-Saharan African applicants, six admit South Asia and Latin America,
five admit MENA, and one each admits North America and Western Europe. The MENA figure
overstates availability: three of the five are global programmes with no regional
presence, and the two MENA-specific instruments are the ACSS Small Grants Program, which
tops out at $4,000 and funds researchers rather than ventures, and the Tunisian Startup
Act, which is confined to one country. **There is no MENA equivalent of Lacuna Fund or
the Tony Elumelu Foundation in this file.**

**5. Award sizes are bimodal and the gap is where data collection sits.** The
distribution splits between stipend-scale awards ($3,000-$5,000: ACSS, TEF, the Tunisian
founder stipend) and institutional-scale awards ($200,000-$1.5m: AI4D, Grand Challenges
Canada, Milken-Motsepe). Building a national survey panel, a sensor network or a
language corpus costs more than the first band and is not an institution-scale research
programme. Lacuna Fund's $25k-$250k range and the GSMA fund are the two instruments that
sit in the gap, which is part of why Lacuna appears as a funder in `ownership.csv` and in
`companies.csv` as an organisation in its own right.

## Link to the rest of the register

Six of the fifteen programmes have a funder that already appears in `ownership.csv` as
having funded an organisation in `companies.csv`: Lacuna Fund, AI4D, the GSMA Innovation
Fund, Gates Grand Challenges, USAID DIV and the ACSS programme. `scripts/07_grants.R`
computes that overlap. It is the only empirical link between the two layers and it is
deliberately narrow: a shared funder name is evidence that the funder is active in this
industry, not evidence that any particular organisation won money through that
particular programme. Do not use it as a grant-receipt indicator.

## Deliberately excluded

Programmes that plausibly belong here but could not be verified to a current cadence and
award range in this pass, and were therefore left out rather than guessed: the Patrick J.
McGovern Foundation's AI grants, MIT Solve's annual challenges, Catalyst Fund, Google.org's
Africa AI funding beyond its Lacuna contribution, the Mastercard Foundation's Young Africa
Works programmes, Villgro Africa, and the national research funds of Qatar, Saudi Arabia
and the United Arab Emirates. The Qatar National Research Fund does appear in
`ownership.csv` as a funder of Arab Barometer, so at least one Gulf instrument is reaching
this industry; its open-call structure was not established here.

Also excluded by definition: accelerators that take equity, venture funds, and one-off
awards. Fuzé is the one borderline case admitted, because it is an open call on a
repeating cadence with a fixed ticket schedule, and it is flagged as
`equity_free_investment` rather than `grant`.

## Fields

See `docs/codebook.md` for the full variable list. `data_specific` is the field that
matters most for use: `yes` means the programme exists to fund data work, `partial` means
a data venture is eligible inside a broader remit, `no` means data ventures compete
against every other sector.
