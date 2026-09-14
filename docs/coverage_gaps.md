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
| NAM | 251 | 236 | 160 | 91 | 48 |
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
| NAM | Identity and biometrics | 14 | 0 |
| SEA | Identity and biometrics | 13 | 0 |
| SAS | Identity and biometrics | 12 | 0 |
| WEU | Identity and biometrics | 11 | 0 |
| NAM | Credit and financial identity | 10 | 0 |
| CHN | Consumer behaviour | 9 | 0 |

Biometric and identity data is the extreme case: collected in all twelve regions,
released to outside researchers in none. Credit data behaves the same way.

**Modality gaps** are invisible in provider counts. Providers by collection method:

| Method | NAM | WEU | SSA | MENA | RUS | CHN |
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
