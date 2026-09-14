# What the data collection industry covers, and what it does not

All figures come from `scripts/03_coverage_gaps.R` over the 370-firm register.
A firm counts as *present* in a region when its coverage score is 2 or 3.
The grid is 12 regions by 26 substantive domains, so 312 cells.

## 1. The industry is nominally almost universal

Only 12 of 312 region-domain cells (3.8%) have no provider at all. Read on its
own this says the map is filled in. It is not the useful reading.

Provider counts by region:

| Region | Any presence | Substantial | HQ'd there | Direct human contact | Research-accessible |
|---|---|---|---|---|---|
| NOAM | 254 | 239 | 163 | 91 | 48 |
| WEU | 234 | 204 | 74 | 77 | 41 |
| SAS | 228 | 180 | 16 | 75 | 33 |
| MENA | 238 | 160 | 49 | 71 | 34 |
| SEA | 222 | 154 | 11 | 58 | 29 |
| LAC | 218 | 151 | 14 | 53 | 29 |
| EEU | 215 | 141 | 15 | 47 | 32 |
| SSA | 222 | 141 | 43 | 65 | 39 |
| EAS | 208 | 139 | 14 | 40 | 27 |
| OCE | 201 | 132 | 4 | 28 | 26 |
| RUS | 140 | 79 | 7 | 16 | 22 |
| CHN | 152 | 69 | 14 | 12 | 15 |

The spread between the best and worst served region is 3.5 to 1 on presence but
7.6 to 1 on direct human contact. Nominal coverage is far more even than real
collection, because the firms that make coverage look global are the ones that
never touch a person.

## 2. Three different gaps, with different causes

**Existence gaps** are rare and concentrated. The twelve empty cells are almost
all in mainland China and the Russia bloc, plus financial transaction data, which
is absent from six of twelve regions. Consumer transaction panels exist only where
card networks, receipt apps and data aggregators are dense and legally permitted:
North America above all, then Western Europe and parts of East Asia. Everywhere
else, spending is inferred rather than observed.

**Access gaps** are the binding constraint. 62 of 312 cells (19.9%) have at least
one provider but none whose record-level data a researcher can obtain. The
access ratio sits near 0.20 in every region, so roughly four fifths of the
industry's coverage is commercially closed regardless of where you look. The gap
is not that nobody collects. It is that collection and disclosure have come
apart.

The most closed cells are ones where collection is heaviest:

| Region | Domain | Providers | Research-accessible |
|---|---|---|---|
| MENA | Prices and retail | 15 | 0 |
| NOAM | Identity and biometrics | 14 | 0 |
| SEA | Identity and biometrics | 13 | 0 |
| SAS | Identity and biometrics | 12 | 0 |
| WEU | Identity and biometrics | 11 | 0 |
| NOAM | Credit and financial identity | 10 | 0 |
| CHN | Consumer behaviour | 9 | 0 |

Biometric and identity data is the extreme case: collected in all twelve regions,
released to outside researchers in none. Credit data behaves the same way.

**Modality gaps** are invisible in provider counts. Providers by collection method:

| Method | NOAM | WEU | SSA | MENA | RUS | CHN |
|---|---|---|---|---|---|---|
| Remote sensing | 26 | 26 | 26 | 26 | 26 | 26 |
| Web scraping | 34 | 32 | 8 | 20 | 8 | 5 |
| Online panel | 35 | 32 | 7 | 13 | 6 | 3 |
| Face-to-face | 8 | 7 | 24 | 21 | 6 | 2 |
| Telecom network | 0 | 3 | 2 | 1 | 0 | 0 |

Remote sensing is the only method that is genuinely uniform, because satellites
do not need permission from the ground. Every other method is uneven, and the
unevenness runs in opposite directions: online and web methods concentrate in
rich connected markets, while in-person interviewing survives mainly in
Sub-Saharan Africa, MENA and Latin America. A region served only by online panels
has a population coverage problem no provider count will show.

## 3. The substantive skew

Domains ranked by number of providers: consumer behaviour (140) and public
opinion (138) are served by roughly a third of the register each. At the bottom
sit legal and regulatory records (6), infrastructure (8), financial transactions
(10), device telemetry (11) and energy and extractives (12).

Migration and displacement has fifteen providers worldwide and fewer than three in
five regions, including North America and Oceania. For a domain that drives a
large share of contemporary policy argument, the primary collection base is very
thin, and most of it is nonprofit or academic rather than commercial.

Education has twenty-five providers and none at all in mainland China. Labour and
employment has twenty-nine, but most are scraped professional-profile datasets
(Coresignal, People Data Labs, ZoomInfo) whose population is people who maintain
a public professional profile, which is not the labour force.

## 4. Where the firms are

55.9% of the register is headquartered in North America or Western Europe.
Among venture and private-equity backed firms that rises to 80.7%. Of the 46
firms founded in 2019 or later, 23 are North American and 6 Western European,
leaving 17 for the rest of the world: nine in Sub-Saharan Africa, five in MENA,
two in Latin America, one in South Asia. None are in the Russia bloc, mainland
China, East Asia, Southeast Asia or Oceania.

The African entry is concentrated and recent, and it is not in survey research.
It is in AI training data for African languages (Lelapa AI, Masakhane, Digital
Umuganda, Awarri, DataLens Africa), in geospatial and environmental data (Amini,
Charis UAS), and in alternative credit scoring (Indicina). The new African firms
are building the observational layer their countries previously only received
from abroad.

New entry by segment since 2019: AI training data (9), survey insights (6),
climate risk (4), field agencies (4), earth observation (3), web data (3),
location and mobility (2). The growth is in repackaging and in remote sensing,
not in getting closer to populations that are currently poorly measured.

Ownership varies systematically by region. Venture capital backs 66 firms in
North America and 26 in Western Europe, against roughly 20 across MENA, Africa,
South Asia, Southeast Asia, East Asia and mainland China combined. Outside the core, the
register is dominated by owner-managed independents and by nonprofits and
academic centres. Those account for 48 of the 424 firms (11.3%) but for 45.7% of
every firm whose record-level data a researcher can reach at all.

That last point explains an otherwise odd result. The access ratio is slightly
*higher* in Russia and Central Asia (0.27) and Sub-Saharan Africa (0.26) than in
North America (0.20). This is not a sign of openness in those markets. It is
survivorship: where commercial demand is thin, the organisations that persist are
funded to publish (Afrobarometer, Levada, the Caucasus Research Resource Centers,
Central Asia Barometer), so the small amount that exists is more likely to be
open. Thin and open beats dense and closed for a researcher, but it is still thin.

## 5. Systematic blind spots

Reading the three gap types together, the register has five clear blind spots.

1. **Closed regimes.** Mainland China (69 substantial providers, 12 with direct
   human contact) and the Russia bloc (79 and 16). What exists is either state
   linked (VCIOM, FOM, CTR, CSM, Chang Guang) or legally exposed (Levada as a
   designated foreign agent). Independent commercial collection has largely
   withdrawn.
2. **Conflict-affected and low-connectivity areas.** Face-to-face capacity is
   what covers these, and it sits with small single-country firms (IIACSS in
   Iraq, KIIS in Ukraine, AWRAD in Palestine, the Afrobarometer national
   partners). These are the most substitutable-looking and least substitutable
   organisations in the register: no global firm replaces them.
3. **Behavioural traces outside rich markets.** Transaction, telemetry,
   location and credit data barely exist beyond North America, Western Europe and
   parts of East Asia. Measurable AI covering Asian and Middle Eastern receipts
   is a rare exception that proves the rule.
4. **Anything sensitive.** Identity, biometrics and credit are collected
   everywhere and disclosed nowhere. The FTC actions against Kochava and X-Mode,
   the bans on Clearview AI, and the suspension of World in several jurisdictions
   show the pattern: enforcement has restricted *sale* without restricting
   collection, which widens the access gap rather than closing the existence gap.
5. **States themselves.** Legal and regulatory records (6 providers) and
   infrastructure (8) are the thinnest domains in the register. Sayari and
   OpenCorporates aside, what governments do is far less measured by this
   industry than what consumers buy.

## 6. How to read a claimed country count

`countries_claimed` has a mean of 65 and a maximum of 250. It correlates
strongly with substantial regional presence (r = 0.88), so it is not noise. The
problem is what the breadth is made of.

Of the firms claiming 100 or more countries, only about a fifth have any direct
contact with a human subject. Among every other firm in the register, roughly
seven in ten do.
Breadth of claim is bought by method: a web scraping firm claiming 195 countries
is describing where its proxy exit nodes sit, a satellite operator claiming
global coverage is describing orbital mechanics, and neither has asked anyone
anything. The claim is usually true and usually not about people.

Where firms do reach people, the claim behaves better but still flatters depth.
A survey firm claiming 90 markets is describing a subcontracting network, and
the ninetieth market is not the first. The ordinal scores in
`coverage_spatial.csv` exist to separate these, and the honest use of
`countries_claimed` is as a measure of infrastructure reach read alongside
`human_subjects` and `modality_primary`, never as a coverage measure on its own.

---

# Country level, by data type and by method

The region tables above are built from hand-coded and rule-derived regional
scores. This section disaggregates them to 194 countries. Before reading it:
**98% of the 21,344 company-country rows are model output**, allocated by the
rules in `scripts/00_build_country_coverage.py`. Only 435 rows are observed.
Every claim below that survives the observed-only sensitivity check is marked;
every claim that does not is labelled as a property of the model.

## 7. The floor is made of firms that never touch anyone

Every one of the 194 countries has at least one provider, and the *minimum* is
29. Turkmenistan, the least served country on earth by this register, still has
29 organisations collecting data about it.

Not one of them speaks to a Turkmen. All 28 are satellite operators, web
crawlers, trade and vessel trackers, and open-source monitors. Turkmenistan is
the only country in the register with zero primary collectors, but the pattern
generalises: the floor beneath every country is remote sensing and web
scraping, and it is the same floor everywhere.

| | Providers | Primary collectors | Research-accessible |
|---|---|---|---|
| United States | 239 | 92 | 48 |
| United Kingdom | 205 | 79 | 41 |
| France | 200 | 75 | 38 |
| Median country | 70 | — | — |
| Guinea-Bissau | 35 | 8 | 5 |
| Comoros | 34 | 7 | 5 |
| Tajikistan | 34 | 3 | 10 |
| Kyrgyzstan | 32 | 3 | 8 |
| Turkmenistan | 29 | **0** | 7 |

The bottom of the distribution is Central Asia and the small states of the Sahel,
Central Africa and the Pacific. The gap between the United States and
Turkmenistan is 8 to 1 on providers and unbounded on primary collection.

## 8. What predicts whether anyone collects data about a country

Regressing country provider counts on country characteristics (full table in
`output/tab17_country_model.txt`, R² = 0.74). The third column repeats the
estimate on hand-coded rows only, which is the test of whether a result is a
property of the industry or of the allocation model.

| Predictor | Effect on log providers | Full file | Observed rows only |
|---|---|---|---|
| Population over 100m (vs under 1m) | +0.88 | +1.61 | +2.76 |
| Internet over 70% (vs under 30%) | +0.27 | +0.60 | +0.55 |
| Restrictive research regime | −0.19 | −0.29 | −0.30 |
| Conflict-affected | +0.05, n.s. | +0.07, n.s. | +0.08, n.s. |
| High income (vs low) | +0.65 | +0.15, n.s. | −0.28 |

(Columns two and three are Poisson estimates on primary collectors and on
observed providers respectively, so they are compared with each other, not with
the first column.)

**Three results now hold in both columns.** Population and connectivity keep
their sign and significance. Restrictive research regime does too, at −0.29 and
−0.30, which is as close as these two columns come to agreeing about anything.
Conflict exposure is a consistent null. Only income still misbehaves, reversing
from +0.65 to −0.28, and it remains unreportable.

The rank correlation between modelled and observed country provider counts is
now 0.535, against 0.094 one revision ago. The observed sample has become
balanced enough for the check to discriminate.

### Reinstating the restrictive-regime result

The previous revision of this document retracted this finding. That retraction
was correct on the evidence then available: with hand-coding concentrated almost
entirely in MENA and Africa, the coefficient on hand-coded rows was 0.001. With
Western European and Latin American footprints added, it is −0.30 and highly
significant, matching the full-file estimate almost exactly. The finding is
reinstated.

Two things make this convergence worth something rather than nothing. The
allocation model does not use `restrictive_research_regime` as an input at all —
`priority_score` reads income, population, connectivity and conflict, and nothing
else — so the two columns are not mechanically linked through the country
allocation. And the biases that remain in each column push in different
directions: the full column inherits thin Russia and China scores from the
hand-coded region matrix, while the observed column is selected on wherever the
coding effort went. Two differently biased estimates landing on the same number
is weak evidence, but it is evidence.

What it is not is clean identification. A wealthy country that gates independent
research gets measured less than its size and connectivity predict; whether that
is the gating doing the work, or something else those countries share, this
register cannot say.

Conflict exposure does not predict provider counts in either column and never
has, across three revisions and two large changes to the sample. That null is
the most stable result here. What conflict does predict is method narrowness,
in section 10.

## 9. Data types are missing from most of the world

Country availability of each data type, out of 194:

| Data type | Countries with any | Missing | Accessible to researchers | Collected but closed |
|---|---|---|---|---|
| Financial transactions | 28 | 166 | **0** | 28 |
| Device telemetry | 89 | 105 | 46 | 43 |
| Credit and financial identity | 104 | 90 | **0** | 104 |
| Mobility and location | 121 | 73 | 64 | 57 |
| Migration and displacement | 154 | 40 | 106 | 48 |
| Labour and employment | 166 | 28 | 112 | 54 |
| Identity and biometrics | 166 | 28 | 5 | 161 |
| Education | 175 | 19 | 82 | 93 |
| Consumer behaviour | 182 | 12 | 103 | 79 |
| AI labels and human feedback | 176 | 18 | 176 | 0 |

Two distinct shapes appear, and they need different remedies.

Financial transactions, credit and device telemetry are **absent** from most of
the world. Transaction data exists in 28 countries and credit data in 104, because
they are by-products of card networks, credit bureaux and smartphone penetration
that most countries do not have. No amount of market access opens these up; the
underlying infrastructure is not there to observe.

Identity and biometrics, prices, education, consumer behaviour and housing are
**present and closed**. Retail price data reaches 189 countries and is reachable
by an outside researcher in 53. Education data reaches 175 and is reachable in
82. Identity and biometric data is the near-pure case: obtainable in 166
countries and accessible in 5, all of them through Digital Umuganda's open
Kinyarwanda speech corpora rather than through any commercial holder. Here the data exists and the barrier is commercial
and legal, which is a tractable problem in a way the first shape is not.

The data types that stay open are the ones nonprofits, academics and satellite
operators hold: earth observation, environment and climate, conflict and security
(194 of 194 each), public opinion, and AI training labels (176 of 176, because the
firms supplying that domain at country level are open-corpus projects such as
Common Crawl, Roboflow, Masakhane and Digital Umuganda rather than the
commercial annotation houses). Openness in this industry is a function of who owns the collector, not of
what is collected.

## 10. Poor countries are reachable by fewer methods

The number of distinct collection methods available in a country falls sharply
with income:

| Income group | Mean distinct methods available |
|---|---|
| High income | 14.0 |
| Upper middle income | 13.0 |
| Lower middle income | 11.3 |
| Low income | 8.8 |

Conflict-affected countries average 10.6 distinct methods against 12.6 elsewhere
(p < 0.001). That difference holds where the earlier regional claim about
conflict coverage did not: conflict does not reliably reduce the *number* of
collectors, but it does narrow the *repertoire*.

Share of provider-country pairs using each method, in the least served quartile
of countries against the rest:

| Method | Bottom quartile | Rest |
|---|---|---|
| Remote sensing | 26.3% | 14.0% |
| API and partner feeds | 18.0% | 15.4% |
| Web scraping | 16.0% | 16.7% |
| Face-to-face | 8.2% | 10.2% |
| Administrative records | 6.3% | 6.8% |
| Online panel | 6.1% | 10.1% |
| Telephone | 5.7% | 7.0% |
| Sensor hardware | 4.7% | 4.3% |
| Transaction | 3.3% | 3.0% |
| Device telemetry | 1.7% | 3.2% |
| Crowd task | 1.5% | 3.4% |
| Expert elicitation | 1.2% | 3.3% |
| Clinical records | 0.0% | 0.7% |

In the least served quartile, more than a quarter of all coverage is a satellite
looking down, against a seventh elsewhere. Face-to-face and telephone hold
slightly *below* their share elsewhere, which is worth stating plainly: adding
fifty-four MENA and African firms did not show that in-person capacity is
concentrated in poor countries. It showed that in-person capacity exists in poor
countries at roughly the rate it exists anywhere, on a much smaller absolute
base. What disappears at the bottom is everything else: online panels at 6.1%
against 10.1%, crowd tasking and expert elicitation at under a third of their
share elsewhere, device telemetry at half, clinical records at zero.

This is the modality gap at country resolution, and it has a methodological
consequence for anyone doing comparative work. In a low-income country the
available evidence is an overhead image, a household interview, or a phone call.
There is no passive trace layer to triangulate against, so a single badly drawn
sample has nothing to correct it. In a high-income country the same question can
be approached five ways. Treating a variable as equivalently measured across both
assumes away the largest source of error in the data.

Nonprofit and academic organisations supply 16.7% of providers in
conflict-affected countries against 10.9% elsewhere (p < 0.001). Where the
commercial case is weakest, the collection that happens is funded rather than
sold, which is also why it is more likely to be published.

## 11. What this changes about the regional picture

The country layer sharpens three of the earlier findings and qualifies one.

Sharpened: the access gap is worse than the regional tables showed, because
closure concentrates in exactly the domains that are present nearly everywhere.
Retail prices reach 189 countries and are reachable in 53; identity and
biometrics reach 165 and are reachable in 5.

Sharpened: the modality gap is a country-level phenomenon, not a regional one.
MENA as a region looks moderately served; Turkmenistan, Yemen and Libya do not,
and they are averaged in with the Gulf and Morocco.

Sharpened: the industry's floor is uniform and thin. Every country is covered,
because satellites and crawlers cover everything. Nothing about that floor tells
you what people in a country think, earn, or do.

Qualified: the earlier regional claim that conflict-affected settings are
particularly poorly covered is **not established at country level**. Once
allocation is stripped out, conflict exposure has no measurable relationship
with provider counts either way. What the register supports is narrower and
firmer, and both parts clear the significance threshold: conflict-affected
countries are reachable by fewer distinct methods (10.6 against 12.6), and the
organisations that cover them are disproportionately nonprofit or academic
(16.7% against 10.9%).

Reinstated: restrictive research regimes do depress collection net of income,
population and connectivity. This claim was made, retracted when the observed
sample was too skewed to test it, and now holds at −0.29 and −0.30 across both
columns. Section 8 gives the history and the remaining limits.

## 12. How much of this is observed

Hand-coding is concentrated where it was most needed. Share of company-country
rows that are observations rather than model output:

| Region | Observed rows | Total rows | Share |
|---|---|---|---|
| MENA | 366 | 2,353 | 15.6% |
| North America | 58 | 403 | 14.4% |
| Sub-Saharan Africa | 612 | 4,267 | 14.3% |
| Western Europe | 360 | 3,298 | 10.9% |
| Latin America | 252 | 3,645 | 6.9% |
| Russia and Central Asia | 17 | 483 | 3.5% |
| South Asia | 37 | 1,080 | 3.4% |
| Mainland China | 5 | 148 | 3.4% |
| Southeast Asia | 41 | 1,272 | 3.2% |
| Eastern Europe | 49 | 2,463 | 2.0% |
| East Asia | 8 | 803 | 1.0% |
| Oceania | 11 | 1,513 | 0.7% |
| **All** | **1,816** | **21,728** | **8.4%** |

Five regions now sit in a usable band between 7% and 16% observed: MENA, North
America, Sub-Saharan Africa, Western Europe and Latin America. Together they
carry 1,648 of the 1,816 observed rows. The remaining seven regions are between
0.7% and 3.5%, and country-level claims about them rest almost entirely on the
allocation model.

The previous revision reported that the observed-only sensitivity check had
stopped working, because hand-coding was concentrated so heavily in MENA and
Africa that a regression on observed rows recovered the shape of the coding
effort rather than the industry. Adding Western European and Latin American
footprints fixed that. The rank correlation between modelled and observed
provider counts went from 0.094 to 0.535, and three of five predictors now agree
across the two columns where previously only two did.

The lesson generalises past this dataset. A hand-coded sample built by following
your own substantive interest will validate nothing, because its selection is
correlated with everything you want to test. Balance in the observed sample is
not a nicety; it is what makes the sample capable of contradicting the model.

Where the grounding still fails: Eastern Europe (2.0%), Southeast Asia (3.2%),
South Asia (3.4%), mainland China (3.4%), the Russia bloc (3.5%), East Asia
(1.0%) and Oceania (0.7%). Two of those, the Russia bloc and mainland China,
carry a specific risk: they are the regions this register claims are least
covered, and they are among the regions where the claim rests least on
observation. That is the next thing to fix, and it is harder than the last two
rounds, because the firms operating there publish less about where they operate.
