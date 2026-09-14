# What the data collection industry covers, and what it does not

All figures come from `scripts/03_coverage_gaps.R` over the **467 operating
firms** in the register. A further 51 organisations that no longer operate are
recorded but excluded from every coverage table here; section 14 is about them.
A firm counts as *present* in a region when its coverage score is 2 or 3.
The grid is 12 regions by 26 substantive domains, so 312 cells.

## 1. The industry is nominally almost universal

Only 7 of 312 region-domain cells (2.2%) have no provider at all. Read on its
own this says the map is filled in. It is not the useful reading.

Provider counts by region:

| Region | Any presence | Substantial | HQ'd there | Direct human contact | Research-accessible |
|---|---|---|---|---|---|
| NOAM | 259 | 244 | 171 | 96 | 49 |
| WEU | 239 | 208 | 73 | 81 | 41 |
| SAS | 233 | 182 | 16 | 76 | 34 |
| MENA | 248 | 166 | 54 | 75 | 34 |
| SSA | 240 | 155 | 54 | 70 | 43 |
| SEA | 227 | 155 | 11 | 58 | 29 |
| LAC | 222 | 152 | 14 | 53 | 29 |
| EEU | 221 | 144 | 16 | 48 | 33 |
| EAS | 212 | 141 | 14 | 40 | 27 |
| OCE | 205 | 134 | 4 | 28 | 26 |
| RUS | 151 | 89 | 17 | 23 | 22 |
| CHN | 165 | 80 | 23 | 13 | 15 |

The spread between the best and worst served region is 3.5 to 1 on presence but
7.6 to 1 on direct human contact. Nominal coverage is far more even than real
collection, because the firms that make coverage look global are the ones that
never touch a person.

## 2. Three different gaps, with different causes

**Existence gaps** are rare and concentrated. The seven empty cells are almost
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

52.2% of operating firms are headquartered in North America or Western Europe,
down from 62.7% before MENA, African, Russian and Chinese enumeration was
deepened. Among venture and private-equity backed firms it is still around 73%.

Of the 62 firms founded in 2019 or later, 31 are North American, 13 Sub-Saharan
African, 8 MENA, 6 Western European and 4 elsewhere. A third of new entry in this
industry is now Middle Eastern or African, which was not visible in earlier
revisions of this register and is not an artifact of looking harder: these are
firms with funding rounds, products and named customers.

What they are building differs sharply by region.

| Segment of firms founded 2019 or later | MENA and Africa | North America and Western Europe |
|---|---|---|
| AI training data | 7 | 11 |
| Survey and insights | 0 | 12 |
| Field data collection | 5 | 2 |
| Earth observation | 4 | 2 |
| Climate risk | 0 | 4 |
| Web data | 2 | 1 |

Not one of the 21 MENA and African startups is in survey and insights, and 12 of
the 37 North American and Western European ones are. The new Northern firms are
overwhelmingly tools for asking questions differently: AI-moderated interviewing
(Listen Labs, Strella, Outset, Conveo, Perspective AI, TheySaid, Versive) and
population simulation (Aaru, Simile). The new Southern firms are building
collection capacity that did not exist: African-language speech corpora (Intron
Health, African Languages Lab, Lelapa AI, Digital Umuganda, Awarri), Arabic
dialect corpora (CNTXT AI, Arabic.AI), field sensing (Aflabox, Tolbi, Amini,
Charis UAS) and clinical record estates (Helium Health).

Of the 44 AI training data firms in the register, 13 are headquartered in MENA or
Sub-Saharan Africa against 21 in North America. This is the one segment where the
periphery has meaningful ownership rather than supplying labour to firms
headquartered elsewhere, and the reason is linguistic: nobody in San Francisco
can assemble a Hausa or Tunisian Arabic corpus.

Ownership varies systematically by region. Venture capital backs 66 firms in
North America and 26 in Western Europe, against roughly 20 across MENA, Africa,
South Asia, Southeast Asia, East Asia and mainland China combined. Outside the core, the
register is dominated by owner-managed independents and by nonprofits and
academic centres. Those account for 57 of the 513 operating firms (11.1%) but for a little under
half of every firm whose record-level data a researcher can reach at all.

### Which owners publish, precisely

Earlier revisions of this document said openness is a function of who owns the
collector. That is right but too loose, and the addition of state space agencies
this revision makes the precise version available. Share of firms whose
record-level data is open or reachable by a researcher, by ownership type:

| Ownership | Firms | Open or researcher-accessible |
|---|---|---|
| Academic | 10 | 90.0% |
| Nonprofit | 49 | 89.8% |
| Industry cooperative | 4 | 25.0% |
| Venture-backed | 163 | 19.6% |
| Subsidiary | 43 | 14.0% |
| Publicly listed | 40 | 12.5% |
| **State-linked** | **18** | **11.1%** |
| Private equity | 34 | 8.8% |
| Owner-managed independent | 152 | 7.9% |

The split is not public against private. It is **grant-funded against
revenue-funded**. Academic and nonprofit collectors publish at nine in ten. Every
other category, state ownership included, sits between 8% and 25%.

State-linked collectors are the least open category bar one. Eleven of the
eighteen release nothing at all. This covers VCIOM and FOM in Russia, CTR and
CSM in China, Ijtimoiy Fikr in Uzbekistan and ISPA in Iran, but also the African
and Middle Eastern space agencies added this revision: NASRDA, the Egyptian Space
Agency, the Kenya Space Agency and ESSTI are all coded `none`. Public ownership
of a collector predicts nothing about public access to what it collects.

That last point explains an otherwise odd result. The access ratio is slightly
*higher* in Russia and Central Asia (0.27) and Sub-Saharan Africa (0.26) than in
North America (0.20). This is not a sign of openness in those markets. It is
survivorship: where commercial demand is thin, the organisations that persist are
funded to publish (Afrobarometer, Levada, the Caucasus Research Resource Centers,
Central Asia Barometer), so the small amount that exists is more likely to be
open. Thin and open beats dense and closed for a researcher, but it is still thin.

## 5. Systematic blind spots

Reading the three gap types together, the register has five clear blind spots.

1. **Closed regimes.** Mainland China (78 substantial providers, 13 with direct
   human contact) and the Russia bloc (89 and 23). Adding twenty domestic firms
   raised the provider count in both and barely moved primary collection, which
   is the shape of the problem: these markets have plenty of collectors and very
   few that talk to anyone. What exists is either state
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
24. Turkmenistan, still the only country in the register with no primary
collector at all, has 30 organisations collecting data about it.

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
| Turkmenistan | 30 | **0** | 6 |
| Kyrgyzstan | 39 | 7 | 9 |
| Eritrea | 24 | 8 | 4 |
| Guinea-Bissau | 24 | 8 | 4 |

The bottom of the distribution is the small states of the Sahel, the Horn, the
Pacific and Central Asia. The gap between the United States and Turkmenistan is
8 to 1 on providers and unbounded on primary collection: 92 organisations in the
United States conduct some form of direct contact with a person, and zero do in
Turkmenistan.

## 8. What predicts whether anyone collects data about a country

Regressing country provider counts on country characteristics
(`output/tab17_country_model.txt`, R² = 0.74), then repeating the estimate on
hand-coded rows only to test whether a result belongs to the industry or to the
allocation model.

| Predictor | Full file | Observed rows, like-for-like | Observed rows, all firms |
|---|---|---|---|
| Population over 100m (vs under 1m) | +1.65 | +2.61 | +2.86 |
| Internet over 70% (vs under 30%) | +0.58 | +0.53 | +0.41 |
| Restrictive research regime | −0.26 | −0.21 | +0.03, n.s. |
| Conflict-affected | +0.06, n.s. | +0.08, n.s. | −0.03, n.s. |
| High income (vs low) | +0.16, n.s. | −0.46 | −0.001, n.s. |

Population, connectivity and restrictive research regime hold their sign and
significance between the first two columns. Conflict is a consistent null.
Income reverses and remains unreportable.

The rank correlation between the full and like-for-like observed counts is 0.797.

### The third column, and a fault in this test

Read the last two columns against each other. They disagree completely on the
restrictive-regime coefficient, −0.21 against +0.03. The difference is not in
the data, it is in what is being counted.

Columns 1 and 2 both count **primary collectors** — firms that make direct
contact with a person — and differ only in whether the row was hand-coded or
allocated. Column 3 counts **all providers** on observed rows. Until this
revision, the sensitivity check in this repository compared columns 1 and 3,
which mixes the basis restriction together with a change of outcome. That is not
a sensitivity test, and it produced a false alarm.

The mechanism is specific and worth stating, because it will affect anyone who
builds a register this way. Hand-coded footprints are far easier to establish for
satellite operators, web crawlers and open-source monitors than for survey firms:
a satellite constellation's country coverage is a matter of orbital mechanics,
while a survey firm's is a matter of contracts nobody publishes. So any burst of
hand-coding shifts the observed sample toward firms that never touch anyone.
Hand-coding Russia and China added 228 rows, most of them exactly those firms,
and the all-firm observed count in restrictive-regime countries duly rose. The
coefficient went to zero not because collection there is unrestricted but
because the observed sample had been reloaded with satellites.

Column 2 fixes this by holding the outcome constant. `n_observed_primary` counts
direct-contact firms on observed rows, so it differs from column 1 in basis and
nothing else.

### History of the restrictive-regime result

This finding has now been reported, retracted, reinstated, and apparently
overturned again before the test was corrected. The sequence is worth keeping
visible because each step was a reasonable reading of what the data then showed.

| Revision | Observed-only estimate | Reported as |
|---|---|---|
| MENA and Africa footprints added | 0.001 | retracted |
| Western Europe and Latin America added | −0.30 | reinstated |
| Russia and China added, old test | +0.04 | apparently overturned |
| Russia and China added, corrected test | −0.23 | holds |
| Startup round added | −0.21 | holds |

The first three rows all used the mismatched comparison. On the corrected test
the result holds across two further rounds, and the full-file estimate has sat
between −0.19 and −0.29 throughout, never moving much. It was the test that was unstable, not the
finding.

### What the finding is still worth

Less than the arithmetic suggests. The like-for-like test rules out one specific
artifact: that the coefficient is manufactured by the country allocation rule.
It cannot rule out the deeper problem, which is that both columns encode the
same analyst judgement. The region-level scores that drive the full column were
hand-coded by me on the view that solicited collection is thin in Russia and
China, and the country footprints that drive the observed column were hand-coded
by me on the same view. A test cannot launder a prior by applying it twice.

What the register can support: a country that legally gates independent research
has fewer organisations making direct contact with its population than its size
and connectivity predict, and this is not an artifact of how coverage was
allocated across countries. What it cannot support: that the gating causes this,
or an effect size anyone should quote.

The regulatory facts behind the coding are at least concrete. Russia capped
foreign ownership of market research firms at 20% with a domestic data
localisation requirement, effective 1 March 2026; Ipsos sold 80% of Ipsos Comcon
in February 2026 and Nielsen moved to divest its Russian division. China's
foreign investment negative list continues to restrict social science research,
social surveys and aerial and marine surveying. These are not proxies for regime
type, they are rules about who may collect.

Conflict exposure does not predict provider counts in any column and has not
across five revisions. That null is the most stable result in this document.

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

Holds, with the test corrected: countries that legally gate independent research
have fewer organisations making direct contact with their populations than their
size and connectivity predict (−0.27 full, −0.23 like-for-like). Section 8 gives
the reporting history, the fault in the earlier test, and why the finding is
worth less than the arithmetic suggests.

## 12. How much of this is observed

Hand-coding is concentrated where it was most needed. Share of company-country
rows that are observations rather than model output:

| Region | Observed rows | Total rows | Share |
|---|---|---|---|
| Russia and Central Asia | 200 | 525 | 38.1% |
| Mainland China | 61 | 165 | 37.0% |
| MENA | 437 | 2,426 | 18.0% |
| Sub-Saharan Africa | 778 | 4,440 | 17.5% |
| North America | 58 | 409 | 14.2% |
| Western Europe | 360 | 3,328 | 10.8% |
| Latin America | 257 | 3,656 | 7.0% |
| South Asia | 45 | 1,090 | 4.1% |
| Southeast Asia | 47 | 1,283 | 3.7% |
| Eastern Europe | 52 | 2,462 | 2.1% |
| East Asia | 10 | 810 | 1.2% |
| Oceania | 11 | 1,508 | 0.7% |
| **All** | **2,316** | **22,102** | **10.5%** |

The Russia bloc and mainland China are the best-grounded regions in the file at
roughly 37 to 38% observed, which is what they should be: they are the regions this
register makes its strongest claims about. Seven regions sit between 7% and 16%.
Three remain thin: Eastern Europe (2.1%), East Asia (1.2%) and Oceania (0.7%),
with South and Southeast Asia just above them at 3.4% and 3.2%.

Four rounds of hand-coding have taught two things about this kind of register,
both of which cost a retraction to learn.

**A sample built by following your own interest validates nothing.** The first
round put almost all hand-coding into MENA and Africa, and a regression on the
observed rows then recovered the shape of the coding effort rather than the
industry. Balancing across regions fixed that. The rank correlation between
modelled and observed primary-collector counts is now 0.797.

**Hand-coding is not neutral across firm types, and that biases the check
itself.** A satellite operator's country coverage is knowable from orbital
mechanics; a survey firm's is a matter of unpublished contracts. So every round
of hand-coding pulls the observed sample toward firms that never contact a
person. A sensitivity test whose outcome variable is not held constant will read
that compositional shift as a change in the world. This is what produced the
false collapse of the restrictive-regime result described in section 8, and it
is why the test now compares primary collectors against primary collectors.

Where grounding still fails: Eastern Europe, East Asia, Oceania, and South and
Southeast Asia. Of these, Eastern Europe matters most, because it contains
Ukraine, Belarus's neighbours and the Western Balkans, where the register makes
claims about wartime and post-authoritarian data collection on 2.1% observation.

## 13. Survey firms that interview nobody

Three firms in the register sit in a solicited segment while having no contact
with a human subject at all. One is Statista, which models and resells rather
than collects. The other two are new, and they are not an oddity.

Aaru, founded March 2024, generates populations of agents and predicts how
demographic or geographic groups will respond. It raised a Series A in December
2025 at a one billion dollar headline valuation, counts Accenture, EY and
Interpublic among its partners, and reported calling a New York Democratic
primary to within 371 votes. Simile raised a hundred million dollar Series A led
by Index Ventures on the same premise.

Both are classified here as `survey_insights` with `human_subjects = none` and
`consent_model = not_applicable`, because every variable the register measures
about how data reaches a firm returns empty for them. There is no sampling frame,
no field period, no response rate, no consent, and no respondent.

This matters for the register in a specific way. Every gap measured in this
document rests on distinguishing firms that reach a population from firms that
model one. The provider counts in section 1, the primary-collection column, the
modality tables in section 10, and the sensitivity test in section 8 all depend
on that line holding. Synthetic research is the first segment that makes the line
contested rather than obvious, because its output is shaped exactly like survey
output and is sold into the same procurement.

The substantive risk is worth naming plainly, since it runs in the direction
opposite to most technology optimism. Simulated respondents are trained on the
data that already exists. Where collection is dense, simulation has something to
learn from. Where it is thin, which is most of section 12's bottom half, it has
the register's own gaps as its training distribution. A synthetic panel for
Turkmenistan can only reproduce what is already known about Turkmenistan, which
this register puts at zero organisations making direct contact with anyone there.
If simulation substitutes for collection at the margin, it will do so most easily
in exactly the places where the underlying evidence is weakest, and it will
return confident answers there.

The register takes no position on whether these methods work. It records that
they exist, that they are capitalised at a scale comparable to the largest
traditional panel businesses, and that they are counted separately from anyone
who speaks to a person.

## 14. What the register can only see because it includes the dead

55 of the 522 organisations here no longer operate: 45 absorbed into an acquirer,
10 wound down or insolvent. Every coverage and gap table above excludes them and
describes the 467 operating firms. This section is about what they show.

### Consolidation is not evenly distributed

Exit rate by segment, counting absorbed and failed firms against all firms ever
recorded in that segment:

| Segment | Operating | Exited | Exit rate |
|---|---|---|---|
| Mobile location and mobility | 13 | 7 | 35.0% |
| Consumer data brokerage | 15 | 7 | 31.8% |
| Health real-world data | 17 | 5 | 22.7% |
| Retail scanning and pricing | 12 | 3 | 20.0% |
| Media and audience measurement | 18 | 4 | 18.2% |
| Vehicle and IoT telemetry | 10 | 2 | 16.7% |
| Financial alternative data | 12 | 2 | 14.3% |
| Full-service survey and insights | 42 | 6 | 12.5% |
| Earth observation | 30 | 4 | 11.8% |
| Panel and sample supply | 26 | 3 | 10.3% |
| AI training data | 44 | 4 | 8.3% |
| **In-country field agencies** | **116** | **6** | **4.9%** |
| Data collection instrumentation | 17 | 0 | 0% |

The observational segments consolidate and fail. The solicited ones, and
especially the small national field agencies, persist. One in three location data
firms in this register is gone; one in twenty field agencies is. Wejo and Otonomo
were together valued at over two billion dollars in 2021 and produced fifteen
million dollars of combined revenue in 2022 against operating expenses above two
hundred and fifty million. Meanwhile the Palestinian Center for Policy and Survey
Research has been running quarterly since 1993.

This inverts the usual story about incumbency and disruption in data. The
capital-intensive, venture-funded, technologically novel end of the industry is
the fragile end. The part that persists is a few people with an enumerator
network and a thirty-year relationship with a national statistical office.

### Exits are overwhelmingly Northern

80% of exited firms were headquartered in North America or Western Europe,
against 52.2% of operating ones. Of 55 exits, 34 were North American, 10 Western
European, 8 Sub-Saharan African, 2 MENA and 1 South Asian. Median lifespan was
19 years for firms that were absorbed and 10 years for firms that failed.

### What survivorship would have hidden

Composition of the register with and without the firms that left:

| | n | HQ in North America or Western Europe | VC or PE backed | Direct human contact | Research-accessible |
|---|---|---|---|---|---|
| Operating only | 467 | 52.2% | 36.8% | 57.6% | 21.0% |
| Including exits | 522 | 55.4% | 34.1% | 55.9% | 18.8% |
| Exited firms only | 55 | 80.0% | 9.1% | 41.8% | **0%** |

The last cell is the one that matters. **Not one exited firm in this register had
record-level data a researcher could obtain.** When a data company dies, its
holdings either transfer to an acquirer under commercial terms or disappear. The
access gap documented in section 2 is therefore not a stable feature of the
industry but a ratchet: collection accumulates, and the routes to it close on
acquisition or failure without ever opening.

23andMe is the clean case. Fifteen million genomes, collected under individual
consent, went onto a bankruptcy auction block in 2025 before a nonprofit acquired
them. The consent that governed collection was not the consent that governed the
sale. uBiome's microbiome samples went the same way in 2019, and Cambridge
Analytica's files were moved to Emerdata as insolvency proceedings began.

### Every MENA and African field agency in this register was bought, not closed

Ten organisations headquartered in MENA or Sub-Saharan Africa have exited. Eight
were absorbed by a larger group and two wound down, and the split is not random.

| Firm | Country | Founded | Exit | Acquirer |
|---|---|---|---|---|
| Markinor | South Africa | 1975 | 2007 | Ipsos |
| Steadman Group | Kenya | 1998 | 2008 | Synovate, thence Ipsos |
| AMRB | United Arab Emirates | 1985 | 2008 | Kantar |
| Research and Marketing Services | Nigeria | 1980 | 2010 | Kantar |
| Repucom Africa | South Africa | 2004 | 2017 | Nielsen |
| Compuscan | South Africa | 1994 | 2018 | Experian |
| Omedia | Senegal | 1998 | 2023 | Ipsos |
| Gro Intelligence | Kenya | 2014 | 2024 | wound down |
| 54gene | Nigeria | 2019 | 2024 | wound down |

**Every field agency and bureau on that list was acquired. Neither firm that
closed was one.** Gro Intelligence and 54gene were venture-funded technology
companies founded in 2014 and 2019; they failed the way Northern startups fail.
The agencies with enumerator networks and thirty-year client relationships did
not fail. They were bought.

The acquisitions cluster in two waves. Four fall between 2007 and 2010, when
Ipsos, Synovate, Kantar and TNS were assembling African and Gulf networks by
purchase: Markinor gave Ipsos South Africa, Steadman gave Synovate Kenya Uganda
Tanzania Zambia Ghana and Mozambique, RMS gave TNS Nigeria Senegal Cameroon Ivory
Coast and Ghana, AMRB gave Kantar the Gulf and North Africa. Three fall between
2017 and 2023. Ipsos ends up holding three of the seven directly or through
Synovate.

This is the mechanism behind a figure in section 1. MENA and Sub-Saharan Africa
show 54 headquartered firms each, and the large global firms show deep coverage
of both. Much of that coverage is not something Ipsos or Kantar built. It is
something they bought between 2007 and 2010 from firms founded in 1975, 1980,
1985 and 1998, which no longer appear in any current register of the industry.

Read against section 4, which found that a third of new entry is now Middle
Eastern or African, the question becomes concrete rather than rhetorical. The
last generation of MENA and African data firms was acquired within twenty to
thirty years of founding, at a median age of 19 years for absorbed firms across
the whole register. The current generation is mostly under five years old. The
`ceased_year` field exists so that whoever maintains this register can answer
whether the pattern repeats rather than guess.

### What this section cannot tell you, and a bias it introduces

Exits are far harder to enumerate than survivors, and the difficulty is not
uniform across kinds of exit. **Acquisitions are announced and closures are not.**
An acquirer issues a press release, the trade press writes it up, and the deal
stays findable fifteen years later; that is how every row in the table above was
established. A Nairobi or Tunis agency that wound up quietly in 2014 generates no
announcement from anyone, because nobody has an interest in publicising it.

So the finding that every MENA and African field agency in this register was
bought rather than closed is partly real and partly an artifact of who publishes.
The real part is that the named acquisitions did happen and reshaped who owns
African and Gulf coverage. The artifact is the denominator: closures are missing
from the record, not from the world, and searching directly for African research
agency liquidations returns directories of operating firms and nothing else.

The 4.9% field agency exit rate is therefore a floor, and the composition of
exits is biased toward absorption in a way that flatters the sector's stability.
Read the segment table as a lower bound with two known biases, Northern and
acquisition-shaped, rather than as a hazard rate. The only systematic record that
would fix this is national market research association membership lists over
time, which are not public for most of the countries that matter here.

## 15. The frontier splits in two

This revision added the collection methods that did not fit the original
taxonomy: contributor-owned sensor networks paid per reading, environmental
sampling of wastewater and DNA, passive acoustic monitoring, and radio frequency
geolocation from orbit. Four new modality codes, one new segment, one new domain.

Put on the same grid as the established methods, they do not behave as one thing.

| Method | Firms | Countries reached |
|---|---|---|
| Radio frequency geolocation | 3 | 194 |
| Remote sensing | 79 | 194 |
| Face-to-face interviewing | 220 | 193 |
| Online panel | 231 | 162 |
| Contributor-operated sensors | 13 | 75 |
| Environmental sampling | 4 | 64 |
| Passive acoustics | 1 | 7 |

Contributor sensing by region, as a share of the countries in each:

| Region | Countries | With a contributor sensor network |
|---|---|---|
| North America | 2 | 100% |
| Western Europe | 20 | 100% |
| Mainland China | 1 | 100% |
| Oceania | 14 | 50% |
| Sub-Saharan Africa | 48 | 38% |
| South Asia | 8 | 38% |
| MENA | 21 | 33% |
| Russia and Central Asia | 7 | 29% |
| East Asia | 7 | 29% |
| Latin America | 33 | 21% |
| Eastern Europe | 22 | 18% |
| Southeast Asia | 11 | 18% |

The split is not between old methods and new ones. It is between methods that
need a participant and methods that do not.

Radio frequency geolocation reaches every country on earth with three firms,
because a satellite listening for radio emitters needs no permission, no
infrastructure and no person. Hivemapper needs someone to buy a dashcam, drive,
and care about a token; WeatherXM needs someone to buy a weather station and keep
it calibrated. Those requirements sort by disposable income and connectivity, so
thirteen firms reach 75 countries and the map they produce is closer to the
rich-world map than to the world.

The comparison that matters is contributor sensing against face-to-face
interviewing. Face-to-face is the oldest method in the register and the one
section 10 found concentrated in poor countries; it reaches 193 of 194 countries
with 220 firms. Contributor-operated sensing, the newest, reaches 75 with 13.
**The newest participatory method remains substantially less geographically even
than the oldest one**, at 100% of North America and Western Europe against 38% of
Sub-Saharan Africa and 33% of MENA. Token incentives were supposed to make sensing
cheap enough to be universal. They have made it cheap enough to be universal in
places where sensing was already cheap.

### Who actually supplies contributor sensing in Africa

An earlier revision of this section put African contributor sensing at 19% of
countries, on a sample of firms that were all North American or European. Adding
the African and MENA operators doubled it, which is the right correction to make
and changes what the number means.

The five firms supplying contributor-operated sensing in Sub-Saharan Africa:

| Firm | Headquarters | Ownership | Microdata access |
|---|---|---|---|
| AirQo | Uganda | Academic, Makerere University | Open |
| Code for Africa | South Africa | Nonprofit | Open |
| Clarity Movement | United States | Venture-backed | Researcher-restricted |
| UjuziKilimo | Kenya | Venture-backed | None |
| EarthRanger | United States | Nonprofit | Researcher-restricted |

**Not one of the token-incentivised networks appears.** Hivemapper, WeatherXM,
DIMO and Nova Labs, which between them define the model and carry its valuations,
reach North America, Western Europe and almost nowhere else. What reaches Africa
instead is a university lab building 150-dollar sensors and publishing the
readings openly, a civic-data nonprofit running a citizen air and water network,
and two Northern organisations selling or licensing access.

That is the same pattern section 4 found in ownership and section 2 found in
access, arriving through a third door. Where the commercial case is thin, what
gets built is grant-funded, and what is grant-funded is published. Three of the
five African suppliers release their data openly or to researchers; none of the
four token networks does. The distributed-sensing frontier in Africa is not a
crypto story. It is a university and civic-tech story that happens to use the same
hardware.

MENA is thinner still. The 33% comes almost entirely from the same Northern and
pan-African operators plus RoboCare in Tunisia; a direct search for
MENA-headquartered environmental sensing startups returns international vendors
serving the region and essentially no local firms. That absence is recorded here
rather than filled in.

### Collection with no data subject

The frontier segments also break the register's consent variables. Of the twelve
firms using contributor sensing, environmental sampling, acoustics or RF, seven
are coded `human_subjects = none` and `consent_model = not_applicable`, and the
coding is not a shrug.

Wastewater epidemiology measures a population's infections, drug use and diet
from sewage. Four firms do it, reaching 64 countries, and combined testing
captures around 41% of the United States population. Nobody consents, because
nobody is identifiable: the unit of observation is a sewershed. The same is true
of a forest microphone that records a chainsaw, and of a satellite that
geolocates a ship's transmitter.

This is a category the privacy frameworks in section 9 mostly do not reach, and
it is growing. Identity and biometric data is collected everywhere and released
nowhere, which is an access problem with a known shape. Population-level
environmental measurement has no access problem of that kind, because there is no
individual record to withhold, and no consent problem of that kind either. What
it has instead is that a community can be measured continuously without any
member of it being asked, told, or able to object. Biobot's loss of the US
national contract to Verily in 2023, and Massachusetts ending its Biobot contract
in 2026, were procurement decisions; no sewershed was consulted in either.

The register takes no position on whether that is a problem. It records that the
methods exist, that they are a real and growing share of how populations get
measured, and that `human_subjects` and `consent_model` return empty for them in
the same way they return empty for the synthetic research firms in section 13.
Two different frontiers, arriving at the same blank.

## 16. Africa and MENA now have more earth observation bodies than North America

Adding the state space agencies and the Israeli and Gulf operators puts 23 earth
observation organisations in MENA and Sub-Saharan Africa against 21 in North
America. On a headcount the periphery has caught up. On structure it has not.

| Ownership | MENA and Africa | North America and Western Europe |
|---|---|---|
| State-linked | 7 | 0 |
| Venture-backed | 8 | 18 |
| Owner-managed independent | 6 | 0 |
| Publicly listed | 1 | 5 |
| Private equity | 0 | 3 |
| Nonprofit | 1 | 0 |
| Subsidiary | 0 | 2 |

Not one North American or Western European earth observation organisation in this
register is state-linked. Seven of twenty-three in MENA and Africa are: SANSA,
NASRDA, the Egyptian Space Agency, the Kenya Space Agency, ESSTI, MBRSC and
TÜBİTAK UZAY. Six more are owner-managed independents, mostly small drone survey
firms, a category with no Northern equivalent in this segment at all.

Three consequences follow, and they run against the headcount.

**Access is worse, not better.** Four of the seven state agencies release nothing
outside government. The Northern venture-backed operators at least sell. What is
openly available across Africa comes from one nonprofit, Digital Earth Africa,
which makes Landsat and Sentinel archives analysis-ready for 54 countries and is
the single largest open earth observation resource on the continent, built on
satellites nobody in Africa owns.

**The satellites are mostly not African.** Nigeria's NigeriaSat series and
Ethiopia's ETRSS were built abroad; Digital Earth Africa processes American and
European public imagery. South Africa has a real space manufacturing base, and
CubeSpace, NewSpace Systems, Simera Sense and Dragonfly Aerospace between them
supplied over 280 products to a single SpaceX rideshare in July 2026. They are
excluded from this register on the same rule that excludes analytics vendors:
they do not collect. The continent builds cameras and payloads and processes
other people's imagery, with few commercial operators of its own in between.

**The market is tiny.** African satellite earth observation is valued at roughly
77 million dollars in 2025, projected to reach 112 million by 2030. That is the
whole continental market across 54 countries, against the tens of billions moving
through the consumer data brokerage and AI training segments. Twenty-three
organisations is not a sign of depth; it is a sign of how little revenue each
needs to exist.

What this does not support is a story about African earth observation catching
up. It supports a narrower and more useful one: the collection layer over Africa
and MENA is now substantially locally operated, disproportionately by states,
mostly on foreign hardware, and less accessible to outside researchers than the
Northern commercial layer it sits alongside.

## 17. Who owns and funds the collectors

This revision adds a stakeholder layer: `data/ownership.csv`, 115 rows naming
founders, controlling owners, investors, acquirers and funders for 66 of the 569
organisations. Coverage is deliberately partial and purposive. Rows exist where
the relationship could be established from a source, and effort was concentrated
on two groups: the organisations whose data is openly accessible, because
section 4 found that openness tracks grant funding, and MENA and African firms.
**Absence of a stakeholder row means not established, never that an organisation
has no owner or funder.** Nothing below is a population statistic.

### The open layer has no non-Northern funder

Of 36 funding relationships established, for 8 organisations, **35 have a funder
headquartered in North America or Western Europe**. The single exception is the
Australian Government, through Geoscience Australia, behind Digital Earth Africa.

Sub-Saharan African organisations account for 21 of the 36 funding relationships,
and every one of those 21 is funded from outside the continent.

Afrobarometer alone illustrates the shape. Its published funders are Sweden's
Sida, Norway's Norad, the Mo Ibrahim Foundation, Open Society Foundations Africa,
Luminate, the Ford Foundation, the Hewlett Foundation, the Mastercard Foundation,
the Packard Foundation, the Obama Foundation, the European Commission, the World
Bank, Canada's IDRC, the Netherlands embassy in Uganda, Germany's BMZ through GIZ,
and USAID. Sixteen funders, none headquartered in Africa. The closest is the Mo
Ibrahim Foundation, founded by a Sudanese-British telecoms entrepreneur and
registered in London.

ACLED is funded by the US State Department, the Dutch and German foreign
ministries, the Tableau Foundation, IOM, the World Bank, the US Department of
Defense and the European Research Council. AirQo, built at Makerere University in
Kampala, runs on two Google.org grants. Digital Earth Africa runs on the Helmsley
Charitable Trust and the Australian government with Amazon and Esri hosting.

### What that implies for the access finding

Section 4 established that academic and nonprofit collectors publish at 90% while
every revenue-funded category sits between 8% and 25%, and section 15 found that
what reaches Africa is grant-funded and therefore published. Both are still true.
This section adds the condition attached to them.

The openly accessible layer of the global data industry, and almost the entirety
of the openly accessible layer over Africa, exists because Northern foundations
and Northern aid ministries pay for it. That is not a hidden arrangement; every
organisation above publishes its funders. But it means the open layer is
contingent on decisions taken in Washington, London, Stockholm, Berlin, Ottawa
and Palo Alto, by bodies with no accountability to the populations being
measured and no obligation to continue.

The register already contains one instance of that contingency arriving. Former
USAID Africa Bureau officials publicly urged the agency to save Afrobarometer's
funding, which is not something anyone does about a funding stream that is
secure. The comparison worth holding is with section 14: when a commercial data
firm loses its market it is bought, and its data continues under a new owner.
When a grant-funded collector loses its funder there is no acquirer, because
there was never a revenue stream to buy.

### Founders

33 founder relationships across 29 organisations. Where the founder's nationality
could be established, most organisations were founded domestically: 7 of 10
Sub-Saharan African organisations, 3 of 4 MENA ones, 12 of 14 North American.

The exceptions are informative rather than numerous. African Languages Lab's
founder works from the United States; Sama was founded in the United States to
employ East African workers; GAMAAN polls Iran from the Netherlands. Each is a
case of a collector positioned outside the population it measures, which is a
different arrangement from a domestic firm and is visible in the data only
because founders are now recorded.

### State control

15 collectors have an established state controlling owner. Seven are the African
and Middle Eastern space agencies added last revision, and the rest are the
Russian, Chinese, Iranian, Egyptian and Uzbek bodies already in the register.
Their access profile is the one section 4 reports: mostly closed. State control
and open access are close to unrelated in this data.

### What is missing

Two thirds of the register has no stakeholder row at all, and the gap is not
random. Privately held firms disclose least, and owner-managed independents, the
largest single ownership category at 152 operating firms, disclose almost
nothing. National field agencies in MENA and Africa, the organisations this
register has worked hardest to enumerate, are also the ones whose ownership is
least documented anywhere public. Anyone extending this layer should expect to
need company registries rather than the web, and in several of the relevant
jurisdictions those registries are not open.
