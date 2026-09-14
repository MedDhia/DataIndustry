# What the data collection industry covers, and what it does not

All figures come from `scripts/03_coverage_gaps.R` over the 370-firm register.
A firm counts as *present* in a region when its coverage score is 2 or 3.
The grid is 12 regions by 26 substantive domains, so 312 cells.

## 1. The industry is nominally almost universal

Only 13 of 312 region-domain cells (4.2%) have no provider at all. Read on its
own this says the map is filled in. It is not the useful reading.

Provider counts by region:

| Region | Any presence | Substantial | HQ'd there | Direct human contact | Research-accessible |
|---|---|---|---|---|---|
| NOAM | 251 | 236 | 160 | 91 | 48 |
| WEU | 231 | 201 | 72 | 77 | 41 |
| SAS | 222 | 175 | 16 | 73 | 30 |
| SEA | 216 | 150 | 11 | 57 | 27 |
| LAC | 212 | 148 | 14 | 53 | 28 |
| EEU | 210 | 139 | 15 | 47 | 31 |
| EAS | 205 | 138 | 14 | 40 | 27 |
| MENA | 209 | 132 | 26 | 51 | 28 |
| OCE | 197 | 131 | 4 | 28 | 26 |
| SSA | 191 | 111 | 17 | 45 | 29 |
| RUS | 135 | 77 | 7 | 16 | 21 |
| CHN | 150 | 68 | 14 | 12 | 15 |

The spread between the best and worst served region is 3.5 to 1 on presence but
7.6 to 1 on direct human contact. Nominal coverage is far more even than real
collection, because the firms that make coverage look global are the ones that
never touch a person.

## 2. Three different gaps, with different causes

**Existence gaps** are rare and concentrated. The thirteen empty cells are almost
all in mainland China and the Russia bloc, plus financial transaction data, which
is absent from six of twelve regions. Consumer transaction panels exist only where
card networks, receipt apps and data aggregators are dense and legally permitted:
North America above all, then Western Europe and parts of East Asia. Everywhere
else, spending is inferred rather than observed.

**Access gaps** are the binding constraint. 64 of 312 cells (20.5%) have at least
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

Domains ranked by number of providers: consumer behaviour (121) and public
opinion (111) are served by roughly a third of the register each. At the bottom
sit legal and regulatory records (5), infrastructure (4), financial transactions
(9), device telemetry (11) and energy and extractives (11).

Migration and displacement has twelve providers worldwide and fewer than three in
five regions, including North America and Oceania. For a domain that drives a
large share of contemporary policy argument, the primary collection base is very
thin, and most of it is nonprofit or academic rather than commercial.

Education has seventeen providers and none at all in mainland China. Labour and
employment has twenty-seven, but most are scraped professional-profile datasets
(Coresignal, People Data Labs, ZoomInfo) whose population is people who maintain
a public professional profile, which is not the labour force.

## 4. Where the firms are

62.7% of the register is headquartered in North America or Western Europe.
Among venture and private-equity backed firms that rises to 87.7%. Of the 34
firms founded in 2019 or later, 23 are North American and 6 Western European,
leaving 5 for the rest of the world: two in Latin America, two in MENA, one in
South Asia. None are in Sub-Saharan Africa, the Russia bloc, mainland China,
East Asia, Southeast Asia or Oceania.

New entry by segment since 2019: AI training data (9), survey insights (6),
climate risk (4), field agencies (4), earth observation (3), web data (3),
location and mobility (2). The growth is in repackaging and in remote sensing,
not in getting closer to populations that are currently poorly measured.

Ownership varies systematically by region. Venture capital backs 66 firms in
North America and 26 in Western Europe, against 13 across MENA, South Asia,
Southeast Asia, East Asia and mainland China combined. Outside the core, the
register is dominated by owner-managed independents and by nonprofits and
academic centres. Those account for 36 of the 370 firms (9.7%) but for 39.7% of
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

1. **Closed regimes.** Mainland China (68 substantial providers, 12 with direct
   human contact) and the Russia bloc (77 and 16). What exists is either state
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
5. **States themselves.** Legal and regulatory records (5 providers) and
   infrastructure (4) are the thinnest domains in the register. Sayari and
   OpenCorporates aside, what governments do is far less measured by this
   industry than what consumers buy.

## 6. How to read a claimed country count

`countries_claimed` has a mean of 65 and a maximum of 250. It correlates
strongly with substantial regional presence (r = 0.88), so it is not noise. The
problem is what the breadth is made of.

Of the 107 firms claiming 100 or more countries, only 21 (20%) have any direct
contact with a human subject. Among every other firm in the register, 71% do.
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
28. Turkmenistan, the least served country on earth by this register, still has
28 organisations collecting data about it.

Not one of them speaks to a Turkmen. All 28 are satellite operators, web
crawlers, trade and vessel trackers, and open-source monitors. Turkmenistan is
the only country in the register with zero primary collectors, but the pattern
generalises: the floor beneath every country is remote sensing and web
scraping, and it is the same floor everywhere.

| | Providers | Primary collectors | Research-accessible |
|---|---|---|---|
| United States | 235 | 91 | 49 |
| United Kingdom | 198 | 76 | 40 |
| France | 196 | 74 | 37 |
| India | 174 | 72 | 29 |
| Median country | 65 | — | — |
| Guinea-Bissau | 34 | 8 | 5 |
| Tajikistan | 33 | 3 | 10 |
| Kyrgyzstan | 31 | 3 | 8 |
| Turkmenistan | 28 | 0 | 7 |

The bottom of the distribution is Central Asia and the small states of the Sahel,
Central Africa and the Pacific. The gap between the United States and
Turkmenistan is 8 to 1 on providers and unbounded on primary collection.

## 8. What predicts whether anyone collects data about a country

Regressing country provider counts on country characteristics (full table in
`output/tab17_country_model.txt`, R² = 0.75):

| Predictor | Effect on log providers |
|---|---|
| High income (vs low) | +0.77 |
| Population over 100m (vs under 1m) | +0.83 |
| Internet over 70% (vs under 30%) | +0.27 |
| Conflict-affected | +0.04, not significant |
| Restrictive research regime | −0.19 |

Population and connectivity are the strongest predictors and **both survive the
observed-only check** with larger coefficients: on hand-coded rows alone, XL
population carries +2.96 and high internet +1.08. Size and connectivity really
do determine who gets measured.

The conflict and restrictive-regime coefficients **do not survive**. On observed
rows only they fall to 0.005 and −0.09, neither significant. The
restrictive-regime result in the full model is partly circular: the regional
scores that feed the allocation already encode thin coverage for Russia and
China, and those countries are coded restrictive. Do not cite it.

## 9. Data types are missing from most of the world

Country availability of each data type, out of 194:

| Data type | Countries with any | Missing | Accessible to researchers | Collected but closed |
|---|---|---|---|---|
| Financial transactions | 27 | 167 | 0 | 27 |
| Device telemetry | 92 | 102 | 46 | 46 |
| Credit and financial identity | 99 | 95 | 0 | 99 |
| Mobility and location | 121 | 73 | 64 | 57 |
| Migration and displacement | 153 | 41 | 90 | 63 |
| Labour and employment | 158 | 36 | 96 | 62 |
| Identity and biometrics | 165 | 29 | **0** | 165 |
| Education | 175 | 19 | 68 | 107 |
| Consumer behaviour | 177 | 17 | 97 | 80 |
| Prices and retail | 189 | 5 | 53 | 136 |
| Public opinion | 194 | 0 | 185 | 9 |
| Earth observation | 194 | 0 | 194 | 0 |
| Environment and climate | 194 | 0 | 194 | 0 |
| Conflict and security | 194 | 0 | 194 | 0 |
| Housing and property | 194 | 0 | 99 | 95 |

Two distinct shapes appear, and they need different remedies.

Financial transactions, credit and device telemetry are **absent** from most of
the world. Transaction data exists in 27 countries and credit data in 99, because
they are by-products of card networks, credit bureaux and smartphone penetration
that most countries do not have. No amount of market access opens these up; the
underlying infrastructure is not there to observe.

Identity and biometrics, prices, education, consumer behaviour and housing are
**present and closed**. Retail price data reaches 189 countries and is reachable
by an outside researcher in 53. Education data reaches 175 and is reachable in
68. Identity and biometric data is the pure case: obtainable in 165 countries,
accessible in none of them. Here the data exists and the barrier is commercial
and legal, which is a tractable problem in a way the first shape is not.

The data types that stay open are the ones nonprofits, academics and satellite
operators hold: earth observation, environment and climate, conflict and security
(194 of 194 each), public opinion (185 of 194), social media discourse (184 of
184). Openness in this industry is a function of who owns the collector, not of
what is collected.

## 10. Poor countries are reachable by fewer methods

The number of distinct collection methods available in a country falls sharply
with income:

| Income group | Mean distinct methods available |
|---|---|
| High income | 14.1 |
| Upper middle income | 13.0 |
| Lower middle income | 11.3 |
| Low income | 8.2 |

Conflict-affected countries average 10.3 distinct methods against 12.6 elsewhere
(p < 0.001). That difference holds where the earlier regional claim about
conflict coverage did not: conflict does not reliably reduce the *number* of
collectors, but it does narrow the *repertoire*.

Share of provider-country pairs using each method, in the least served quartile
of countries against the rest:

| Method | Bottom quartile | Rest |
|---|---|---|
| Remote sensing | 26.3% | 13.9% |
| API and partner feeds | 17.3% | 15.2% |
| Web scraping | 16.0% | 17.3% |
| Face-to-face | 9.4% | 9.6% |
| Telephone | 6.8% | 6.3% |
| Administrative records | 6.0% | 7.0% |
| Online panel | 5.4% | 10.2% |
| Sensor hardware | 5.2% | 4.6% |
| Transaction | 3.0% | 3.2% |
| Device telemetry | 1.6% | 3.4% |
| Crowd task | 1.2% | 3.4% |
| Expert elicitation | 0.9% | 3.3% |
| Clinical records | 0% | 0.7% |

In the least served quartile, more than a quarter of all coverage is a satellite
looking down. Face-to-face and telephone hold roughly their share, so in-person
capacity has not collapsed, but it is a constant share of a much smaller
absolute base. What disappears is everything else: online panels at half their
share elsewhere, crowd tasking and expert elicitation at a third, device
telemetry at half, clinical records at zero.

This is the modality gap at country resolution, and it has a methodological
consequence for anyone doing comparative work. In a low-income country the
available evidence is an overhead image, a household interview, or a phone call.
There is no passive trace layer to triangulate against, so a single badly drawn
sample has nothing to correct it. In a high-income country the same question can
be approached five ways. Treating a variable as equivalently measured across both
assumes away the largest source of error in the data.

Nonprofit and academic organisations supply 16.2% of providers in
conflict-affected countries against 10.9% elsewhere (p < 0.001). Where the
commercial case is weakest, the collection that happens is funded rather than
sold, which is also why it is more likely to be published.

## 11. What this changes about the regional picture

The country layer sharpens three of the earlier findings and qualifies one.

Sharpened: the access gap is worse than the regional tables showed, because
closure concentrates in exactly the domains that are present nearly everywhere.
Retail prices reach 189 countries and are reachable in 53; identity and
biometrics reach 165 and are reachable in none.

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
countries are reachable by fewer distinct methods (10.3 against 12.6), and the
organisations that cover them are disproportionately nonprofit or academic
(16.2% against 10.9%).
