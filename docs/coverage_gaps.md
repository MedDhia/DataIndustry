# What the data collection industry covers, and what it does not

All figures come from `scripts/03_coverage_gaps.R` over the **805 operating
firms** in the register. A further 75 organisations that no longer operate are
recorded but excluded from every coverage table here; section 14 is about them.
A firm counts as *present* in a region when its coverage score is 2 or 3.
The grid is 12 regions by 27 substantive domains, so 324 cells.

## 1. The industry is nominally almost universal

Only 3 of 324 region-domain cells (0.9%) have no provider at all. Read on its
own this says the map is filled in. It is not the useful reading.

Provider counts by region:

| Region | Any presence | Substantial | HQ'd there | Direct human contact | Research-accessible |
|---|---|---|---|---|---|
| SSA | 435 | 317 | 167 | 152 | 125 |
| NOAM | 426 | 411 | 255 | 154 | 92 |
| WEU | 411 | 359 | 156 | 142 | 71 |
| MENA | 395 | 271 | 109 | 106 | 58 |
| SAS | 340 | 251 | 16 | 80 | 46 |
| SEA | 333 | 218 | 11 | 62 | 39 |
| LAC | 323 | 214 | 14 | 57 | 39 |
| EEU | 321 | 203 | 16 | 49 | 42 |
| OCE | 313 | 203 | 6 | 29 | 37 |
| EAS | 310 | 201 | 15 | 41 | 36 |
| CHN | 236 | 120 | 23 | 13 | 19 |
| RUS | 214 | 137 | 17 | 23 | 26 |

The spread between the best and worst served region is 1.8 to 1 on presence but
11.7 to 1 on direct human contact.

**Sub-Saharan Africa is now first on presence and on research-accessible
providers, and first on direct human contact.** That is a complete reversal of
what the first revisions of this document reported, and the honest reading is
that it says more about how the register was built than about the industry. Three
successive African rounds have gone looking specifically for organisations the
earlier construction missed, and no comparable effort has been made for Latin
America, South Asia, Southeast Asia or Eastern Europe. **Read the African row as
the closest thing here to a properly enumerated region, and every row below it as
a lower bound.**

Nominal coverage is far more even than real collection, because the firms that
make coverage look global are the ones that never touch a person.

**Sub-Saharan Africa now has the most research-accessible providers of any region
except North America, and the highest access ratio of any region at all.** That
is an artefact of who does the collecting rather than of how much gets collected:
adding the Afrobarometer national partner network put 34 in-country field agencies
into the register, each of which releases its national microdata openly.

### Most of this table is not commercial, and that changes how to read it

The register now carries a `sector` variable separating for-profit firms from
nonprofits, universities and state bodies. **630 of the 805 operating
organisations are for-profit, 78.3%, but the share varies enormously by region
and it is lowest exactly where the register is best enumerated.**

| Region | Operating | For-profit | Share | Nonprofit | Academic | Governmental |
|---|---|---|---|---|---|---|
| NOAM | 255 | 223 | 87.5% | 19 | 13 | 0 |
| WEU | 156 | 137 | 87.8% | 13 | 6 | 0 |
| SSA | 167 | 86 | 51.5% | 48 | 19 | 14 |
| MENA | 109 | 81 | 74.3% | 10 | 6 | 12 |
| CHN | 23 | 23 | 100% | 0 | 0 | 0 |

**Half of the Sub-Saharan African layer is not a business.** For anyone reading
this register as a map of an industry, the African row in the density table above
is roughly half as large as it looks, and the reason is in what three African
rounds went looking for: Afrobarometer national partners, health and demographic
surveillance sites, university institutes and statistical bodies. Those are real
collectors, and they are not firms.

### The MENA and Africa comparison, both ways

Successive rounds have enumerated both regions to a comparable depth. They look
alike on capacity and nothing alike on disclosure, and the gap survives the
for-profit cut.

| | MENA | Sub-Saharan Africa |
|---|---|---|
| Operating organisations | 109 | 167 |
| Releasing microdata | 23 (21.1%) | 91 (54.5%) |
| **For-profit organisations** | **81** | **86** |
| **For-profit releasing microdata** | **5 (6.2%)** | **22 (25.6%)** |

Restricting to commercial firms cuts both figures by more than half and leaves the
ratio between them intact, slightly wider in fact, 4 to 1 rather than 2.6 to 1. So
the difference is not only that Africa has more nonprofits.

**But the mechanism is the same one either way, and it is a contractual condition
rather than a property of the firms.** Of the 22 African for-profit organisations
releasing microdata, **17 are Afrobarometer national partners**: private
consultancies that publish their national dataset because the network requires it
as a condition of the contract. The other five are Amini, Intron Health, Zindi,
Kartoza and Spatial Collective. Strip the Afrobarometer condition out and
commercial African data disclosure is five organisations in 86, which is 5.8% and
statistically indistinguishable from MENA's 6.2%.

**That is the finding, and it is sharper than the one the previous revision
reported.** Commercial data collectors in MENA and in Sub-Saharan Africa disclose
at almost identical, very low rates. The regional difference in openness is
produced almost entirely by two things Africa has and MENA does not: a distributed
donor-funded survey network that writes publication into its partner contracts,
and a dense layer of nonprofit and academic population cohorts. Neither is a fact
about African firms.

The MENA figure rests on coding 109 organisations, most of them privately held,
and `microdata_access` for a private firm is the least verifiable field in
`companies.csv`. Treat the direction as well supported and the magnitude as
approximate.

### In six regions not one commercial collector discloses

Running the same cut across every region gives `output/tab31_disclosure_forprofit.txt`:

| Region | For-profit firms | Releasing microdata |
|---|---|---|
| SSA | 86 | 25.6% |
| NOAM | 223 | 19.3% |
| EEU | 12 | 16.7% |
| WEU | 137 | 11.7% |
| MENA | 81 | 6.2% |
| CHN | 23 | 4.3% |
| SAS, SEA, LAC, OCE, EAS, RUS | 74 combined | **0%** |

**In six of twelve regions, not one for-profit organisation in this register makes
record-level data available to an outside researcher.** Those six hold 74
commercial collectors between them. The access gap documented in section 2 is at
its most complete in exactly the places the register has enumerated least, so the
figure should be read as a lower bound on openness and an upper bound on
confidence.

## 2. Three different gaps, with different causes

**Existence gaps** are rare and concentrated. The three remaining empty cells are
in mainland China and the Russia bloc. Financial transaction data is the thinnest
domain that exists everywhere: consumer transaction panels are substantial only
where card networks, receipt apps and data aggregators are dense and legally
permitted. That means North America above all, then Western Europe and parts of East Asia.
Everywhere else, spending is inferred rather than observed.

**Access gaps** are the binding constraint. 55 of 324 cells (17.0%) have at least
one provider but none whose record-level data a researcher can obtain, and the
share has barely moved as the register has grown from under 500 organisations to
over 880. The access ratio sits near 0.20 in every region except Sub-Saharan
Africa, where it is 0.39 for the reason given in section 1, so roughly four fifths
of the industry's coverage is commercially closed almost everywhere you look. The
gap is not that nobody collects. It is that collection and disclosure have come
apart.

The most closed cells are ones where collection is heaviest:

| Region | Domain | Providers | Research-accessible |
|---|---|---|---|
| NOAM | Identity and biometrics | 22 | 0 |
| MENA | Prices and retail | 18 | 0 |
| CHN | Consumer behaviour | 17 | 0 |
| NOAM | Credit and financial identity | 16 | 0 |
| NOAM | Financial transactions | 13 | 0 |
| SSA | Prices and retail | 13 | 0 |
| SEA | Identity and biometrics | 13 | 0 |
| WEU | Identity and biometrics | 13 | 0 |

Biometric and identity data is the extreme case: collected in all twelve regions,
released to outside researchers in none. Credit data behaves the same way.

**Modality gaps** are invisible in provider counts. Providers by collection method:

| Method | NOAM | WEU | SSA | MENA | RUS | CHN |
|---|---|---|---|---|---|---|
| Remote sensing | 50 | 50 | 62 | 57 | 50 | 50 |
| Web scraping | 48 | 45 | 15 | 31 | 12 | 5 |
| Online panel | 60 | 61 | 10 | 15 | 10 | 4 |
| Face-to-face | 14 | 15 | 89 | 45 | 10 | 2 |
| Telecom network | 1 | 4 | 2 | 1 | 0 | 0 |

Remote sensing is the only method that is close to uniform, because satellites
do not need permission from the ground; it reads higher in Sub-Saharan Africa and
MENA only because several operators in the register were coded there specifically. Every other method is uneven, and the
unevenness runs in opposite directions, and sharply: online and web methods
concentrate in rich connected markets, while face-to-face interviewing is now
recorded six times more often in Sub-Saharan Africa than in North America or
Western Europe. A region served only by online panels
has a population coverage problem no provider count will show.

## 3. The substantive skew

Domains ranked by number of providers: public opinion (289), consumer behaviour
(195), health and clinical (131) and labour and employment (94). At the bottom sit
biodiversity (5), legal and regulatory records (12), financial transactions (18),
energy and extractives (21) and device telemetry (24).

Migration and displacement has thirty-one providers worldwide and fewer than three in
five regions, including North America and Oceania. It rose from eighteen to
thirty-one only because the African surveillance sites were added: an HDSS records
in-migration and out-migration as a matter of routine, which makes the continent's
population cohorts the largest single source of primary migration data in this
register. For a domain that drives a
large share of contemporary policy argument, the primary collection base is very
thin, and most of it is nonprofit or academic rather than commercial.

Education has forty-nine providers and none at all in mainland China. Labour and
employment has ninety-four, but most are scraped professional-profile datasets
(Coresignal, People Data Labs, ZoomInfo) whose population is people who maintain
a public professional profile, which is not the labour force.

## 4. Where the firms are

51.1% of operating firms are headquartered in North America or Western Europe,
down from 62.7% before MENA, African, Russian and Chinese enumeration was
deepened, and still 72.2% among venture and private-equity backed firms. The
share has moved up and down as successive regions were extended; read it as
roughly half rather than as a trend.

Of the 89 operating firms founded in 2019 or later with a known founding year, 40
are North American, 19 Sub-Saharan African, 14 MENA, 12 Western European and 4
elsewhere. The African count fell by one between revisions because Okra, added as
a 2019 startup, turned out to have shut down in May 2025 and moved to the exit
file. A
third of recent entry in this industry is Middle Eastern or African, which was not
visible in earlier revisions of this register and is not an artifact of looking
harder: these are firms with funding rounds, products and named customers.

What they are building differs sharply by region.

| Segment of firms founded 2019 or later | MENA and Africa | North America and Western Europe |
|---|---|---|
| AI training data | 9 | 11 |
| Survey and insights | 0 | 14 |
| Field data collection | 6 | 2 |
| Earth observation | 6 | 6 |
| Climate risk | 0 | 4 |
| Web data | 2 | 4 |

Not one of the 34 MENA and African startups founded since 2019 is in survey and
insights, and 14 of the 52 Northern ones are. That held when the comparison was 21
against 37 and it still holds now that both counts have grown, which is the main
reason to trust it. The new Northern firms are
overwhelmingly tools for asking questions differently: AI-moderated interviewing
(Listen Labs, Strella, Outset, Conveo, Perspective AI, TheySaid, Versive) and
population simulation (Aaru, Simile). The new Southern firms are building
collection capacity that did not exist: African-language speech corpora (Intron
Health, African Languages Lab, Lelapa AI, Digital Umuganda, Awarri), Arabic
dialect corpora (CNTXT AI, Arabic.AI, Intella, Maqsam, QCRI), field sensing (Aflabox, Tolbi, Amini,
Charis UAS) and clinical record estates (Helium Health).

Of the 52 AI training data firms in the register, 20 are headquartered in MENA or
Sub-Saharan Africa against 22 in North America. This is the one segment where the
periphery has meaningful ownership rather than supplying labour to firms
headquartered elsewhere, and the reason is linguistic: nobody in San Francisco
can assemble a Hausa or Tunisian Arabic corpus.

Ownership varies systematically by region. Venture capital backs 108 firms in
North America and 45 in Western Europe, against 66 across MENA, Africa, South
Asia, Southeast Asia, East Asia and mainland China combined. Outside the core, the
register is dominated by owner-managed independents and by nonprofits and academic
centres: 91 of the 394 operating firms headquartered outside North America and
Western Europe, and they supply a disproportionate share of every firm whose
record-level data a researcher can reach at all.

Three extension rounds have run since, and they did not all push in the same
direction. North America added 75 organisations, mostly venture-backed or
private-equity-held, which widened the gap. Western Europe added 81 of which most
were not venture capital at all: owner-managed national opinion institutes and
academic infrastructure such as GESIS, the German Socio-Economic Panel,
Understanding Society, the UK Data Service, Lifelines and FinnGen. Its
headquartered count nearly doubled, from 80 to 156, and its direct human contact
count rose from 84 to 141, within three of North America.

The African round cut the other way again. It added 63 organisations, of which
the great majority are nonprofits, university centres and owner-managed
consultancies rather than venture-backed firms, and it raised Sub-Saharan
Africa's research-accessible count from 53 to 93 and its access ratio to 0.34,
the highest of any region. What the earlier revisions were measuring was not a
thinner African collection base but a register assembled from English-language
trade coverage, which sees venture-backed firms and does not see national
research institutes.

The MENA round confirmed that reading and then complicated it. Thirty-eight
additions took the region from 68 organisations to 106 and its headquartered
count from 66 to 104, so the same undercount was operating there. But MENA's
access ratio barely moved while Africa's went to 0.34 and then, after the
population cohorts were added, to 0.39. Looking harder found the organisations in
both regions; only in Africa did looking harder also find open data. Section 1
sets out why, and warns about how much of that gap this document's own
construction choices are responsible for.

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
| Median country | 70 | - | - |
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

Columns 1 and 2 both count **primary collectors** - firms that make direct
contact with a person - and differ only in whether the row was hand-coded or
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

75 of the 880 organisations here no longer operate: 58 absorbed into an acquirer,
17 wound down or insolvent. Every coverage and gap table above excludes them and
describes the 805 operating firms. This section is about what they show.

### Consolidation is not evenly distributed

Exit rate by segment, counting absorbed and failed firms against all firms ever
recorded in that segment:

| Segment | Operating | Exited | Exit rate |
|---|---|---|---|
| Mobile location and mobility | 15 | 8 | 34.8% |
| Consumer data brokerage | 18 | 7 | 28.0% |
| Retail scanning and pricing | 15 | 3 | 16.7% |
| Health real-world data | 32 | 6 | 15.8% |
| Vehicle and IoT telemetry | 17 | 3 | 15.0% |
| Media and audience measurement | 24 | 4 | 14.3% |
| Financial alternative data | 18 | 3 | 14.3% |
| Panel and sample supply | 31 | 5 | 13.9% |
| Earth observation | 70 | 6 | 7.9% |
| AI training data | 49 | 4 | 7.5% |
| Full-service survey and insights | 100 | 6 | 5.7% |
| Data collection instrumentation | 22 | 1 | 4.3% |
| **In-country field agencies** | **163** | **6** | **3.6%** |

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

77.3% of exited firms were headquartered in North America or Western Europe,
against 51.1% of operating ones. Of 75 exits, 41 were North American, 17 Western
European, 14 Sub-Saharan African, 2 MENA and 1 South Asian. Median lifespan was
13 years for firms that were absorbed and 9 for firms that failed.

### What survivorship would have hidden

Composition of the register with and without the firms that left:

| | n | HQ in North America or Western Europe | VC or PE backed | Direct human contact | Research-accessible |
|---|---|---|---|---|---|
| Operating only | 805 | 51.1% | 33.0% | 58.0% | 28.4% |
| Including exits | 880 | 53.3% | 31.4% | 56.8% | 26.2% |
| Exited firms only | 75 | 77.3% | 13.3% | 44.0% | **2.7%** |

The last cell is the one that matters, and successive extension rounds have
changed it twice. Earlier revisions said that **not one** exited firm in this
register had record-level data a researcher could obtain. There are now two, so
the claim is stated as a rate: 2 of 75 exits, 2.7%, against 28.4% among operating
firms.

**Every exit in this register but one is a for-profit.** 74 of the 75 exited
organisations are commercial; the exception is the INDEPTH Network. No academic
or governmental organisation in the register has ever closed, and exactly one
nonprofit has. Part of that is real, since a university institute does not get
acquired and a statutory body does not run out of runway. Part of it is a coding
limit worth naming: a nonprofit that quietly stops fieldwork leaves no
announcement, and this register finds exits through acquisition notices and
insolvency reporting. **Section 14 is therefore an analysis of the commercial
layer, and the survivorship correction it supports applies to for-profit firms
only.** Do not read the absence of academic exits as evidence that academic
collection is durable.

**A second cell in this table has moved for a reason worth naming.** The venture
and private-equity share among exits was 8.6% when the exit sample was 70 firms
and is 13.3% now that it is 75. The five exits added since were all venture-backed
African startups: Okra, iProcure, Sendy, WeFarm and, earlier, WhereIsMyTransport.
The gap against operating firms survives, 13.3% against 33.0%, but it was
overstated, and the reason is that the register found Northern acquisitions before
it found Southern failures. Acquisitions are announced by the acquirer and
Southern failures are reported, if at all, in regional trade press. **Any
survivorship correction built from English-language sources will understate
failure in the periphery and should be assumed to be doing so here.**

The two exceptions are instructive in opposite directions. Knowledge Networks
built the first probability-based US internet panel in 1998 and was sold to GfK in
2011; its academic access arrangements survived because the acquirer wanted the
panel as a going concern. The INDEPTH Network ran a shared open repository for
close to fifty African surveillance sites and wound down after 2018 governance
disputes; its data survived because it had already been published and because the
member sites, which own their own data, continued without it. **Neither case
turned on the original consent. One survived because an acquirer found the asset
useful and the other because the data had already left the building.**

When a data company dies, its holdings almost always either transfer to an
acquirer under commercial terms or disappear. The access gap documented in
section 2 is therefore close to a ratchet: collection accumulates, and the routes
to it usually close on acquisition or failure without ever opening. Knowledge
Networks is the instructive exception rather than a counter-example, because the
panel survived as Ipsos KnowledgePanel with its academic access arrangements
intact. What preserved researcher access was that the acquirer wanted the panel
as a going concern, not anything about the original consent.

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
| Radio frequency geolocation | 4 | 194 |
| Remote sensing | 110 | 194 |
| Face-to-face interviewing | 339 | 193 |
| Online panel | 339 | 162 |
| Contributor-operated sensors | 21 | 162 |
| Environmental sampling | 5 | 64 |
| Passive acoustics | 1 | 7 |

Contributor sensing by region, as a share of the countries in each:

| Region | Countries | With a contributor sensor network |
|---|---|---|
| North America | 2 | 100% |
| Western Europe | 20 | 100% |
| Mainland China | 1 | 100% |
| MENA | 21 | 90% |
| South Asia | 8 | 88% |
| Russia and Central Asia | 7 | 86% |
| Oceania | 14 | 71% |
| Sub-Saharan Africa | 48 | 56% |
| East Asia | 7 | 29% |
| Latin America | 33 | 21% |
| Eastern Europe | 22 | 18% |
| Southeast Asia | 11 | 18% |

The split is not between old methods and new ones. It is between methods that
need a participant and methods that do not.

Radio frequency geolocation reaches every country on earth with four firms,
because a satellite listening for radio emitters needs no permission, no
infrastructure and no person. Hivemapper needs someone to buy a dashcam, drive,
and care about a token; WeatherXM needs someone to buy a weather station and keep
it calibrated. Those requirements sort by disposable income and connectivity.

### This finding was overstated and is now weaker

An earlier revision of this section reported contributor-operated sensing
reaching 75 countries with thirteen firms, against 193 countries for face-to-face
interviewing, and concluded that the newest participatory method was
substantially less geographically even than the oldest one, at 38% of
Sub-Saharan Africa against 100% of the core.

Extending the register changed that. Contributor sensing now reaches 162
countries with 21 firms, and Sub-Saharan Africa sits at 56%. Most of the
difference is one organisation: Ookla's Speedtest, which crowdsources network
measurements from user devices in essentially every country with mobile
internet, and which the register had simply been missing. PurpleAir and Safecast
add further reach on the same principle.

**The gradient survives but the gap is much smaller than reported.** Contributor
sensing reaches 162 countries against face-to-face's 193, and it is at 100% of
North America and Western Europe against 56% of Sub-Saharan Africa. The ordering
across the poorer regions no longer supports the original story either: Africa is
now better covered on this method than East Asia, Latin America, Eastern Europe
or Southeast Asia, which reflects donor-funded environmental sensing in Africa
more than any market logic.

The lesson is about the register rather than about the industry. A finding built
on a method with only thirteen recorded firms was resting on a sample small
enough that one omission could carry it. Anything in this document computed over
fewer than about twenty firms should be read the same way.

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

## 16. Africa and MENA match North America on earth observation headcount

An earlier revision of this section said the two regions had **more** earth
observation bodies than North America, on 23 against 21. Extending the register
has made it a tie: 25 in MENA and Sub-Saharan Africa against 25 in North America,
and 40 once Western Europe is included. The claim is restated here as parity
rather than quietly left as it was, because the margin it rested on was two
organisations.

On a headcount the periphery has caught up with the United States and Canada. On
structure it has not.

| Ownership | MENA and Africa | North America and Western Europe |
|---|---|---|
| State-linked | 8 | 0 |
| Venture-backed | 8 | 26 |
| Owner-managed independent | 7 | 1 |
| Publicly listed | 1 | 6 |
| Private equity | 0 | 3 |
| Nonprofit | 1 | 0 |
| Subsidiary | 0 | 4 |

Not one North American or Western European earth observation organisation in this
register is state-linked. Eight of twenty-five in MENA and Africa are: SANSA,
NASRDA, the Egyptian Space Agency, the Kenya Space Agency, ESSTI, MBRSC, TÜBİTAK
UZAY and the Saudi Space Agency. Seven more are owner-managed independents, mostly
small drone survey firms, a category with one Northern equivalent in this segment
against seven here.

Three consequences follow, and they run against the headcount.

**Access is worse, not better.** Five of the eight state agencies release nothing
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

`data/ownership.csv` records founders, controlling owners, investors, acquirers
and funders: 258 rows covering 111 of the 880 organisations. Coverage is partial
and purposive. Rows exist where the relationship could be established from a
source, and effort was concentrated on organisations whose data is openly
accessible, because section 4 found that openness tracks grant funding, and on
MENA and African firms. **Absence of a stakeholder row means not established,
never that an organisation has no owner or funder.** Nothing below is a
population statistic.

### Correction to the previous revision

The previous version of this section stated that the open layer had no
non-Northern funder, on 36 established funding relationships. Extending the file
to 66 relationships across 12 organisations found four, so the categorical claim
was wrong and is withdrawn.

The four are the Qatar National Research Fund, which has funded Arab Barometer;
the South African Institute of International Affairs, which has funded Twaweza;
the Open Society Initiative for West Africa, the Dakar-registered West African arm
of the Open Society Foundations, which funds CDD-Ghana; and the Australian
government behind Digital Earth Africa. Of those, only the Qatari fund and the
South African institute are independently non-Northern in origin as well as
registration.

The quantitative version survives and is the one to use: **64 of 68 established
funding relationships, 94.1%, have a funder headquartered in North America or
Western Europe.** Two of the four exceptions are Northern money routed through a
Southern office or a fellow OECD state.

### Locally founded, externally funded

Setting the founder and funder rows side by side produces the sharper result.

| | MENA and Africa | North America and Western Europe |
|---|---|---|
| Founder rows with nationality established | 101 | 28 |
| Founded by a national of the country | 83% | 89% |

MENA and African data organisations are overwhelmingly founded by people from
the countries they operate in, at close to the same rate as Northern ones.
Baseera by Magued Osman in Cairo, AWRAD by Nader Said in Ramallah, IIACSS by
Munqith Al-Dagher in Baghdad, Sigma Conseil by Hassen Zargouni in Tunis, One to
One by Youssef Meddeb, the Yemen Polling Center by Hafez Albukari, NOIPolls by
Ngozi Okonjo-Iweala, Infotrak by Angela Ambitho, Ask Afrika by Andrea Rademeyer,
Aerobotics by James Paterson and Benji Meltzer, UjuziKilimo by Brian Bosire,
mPharma by Gregory Rockson, Helium Health by Adegoke Olubusi, Tito Ovia and
Dimeji Sofowora.

The seventeen exceptions concentrate in a small number of organisations rather
than being spread across the register. Apollo Agriculture, Busara, eHealth
Africa, Hello Tractor and mSurvey are American-founded Kenyan and Nigerian
operations, and mPharma has two American co-founders beside its Ghanaian chief
executive. Afrobarometer was co-founded by an American and a South African
alongside Ghana's E. Gyimah-Boadi, Lelapa AI has an American among its six
founding members, and Hello Tractor has two American founders rather than one. Two exceptions are regional rather than
Northern: Pula's Dutch co-founder Rose Goslinga built her career in Kenyan
agricultural insurance, and Tarjama's Nour Al Hassan is a Jordanian running a
firm registered in the Emirates.

The share fell from 88% to 83% as verification added co-founders, and it fell
for a specific reason: single-name attributions had recorded the local chief
executive and dropped the American technical co-founders standing behind them.
The corrected figure is the one to use, and the direction of the error is worth
keeping in mind for any dataset built from press coverage of African startups.

So the dependency this section documents is not about who runs these
organisations. It is about who pays for them. **Institutions locally founded,
funding base almost entirely external.** That is a different and more precise
claim than a story about Northern control of African research, and it has
different implications: the expertise, the staff and the decisions are largely
domestic, and the budget line is not.

### How the founder rows were verified

Founder attributions have been checked in three passes: the seventeen coded at
evidence level C, then the sixty-five coded at level B, then an audit of the
level A rows themselves. The file now holds 132 founder rows at level A and one
at level B.

**The level C pass.** Sixteen of seventeen were confirmed and one was wrong. The
error is worth naming because of how it happened. Near East Consulting was
attributed to Jamil Rabah. Searching found no support for that and surfaced a
different organisation entirely: Near East Consulting Group, a Lebanese
recruiting and management consultancy founded by Roger Y. Dib, unrelated to the
Palestinian polling firm in this register. The attribution was a name collision
between two similarly named organisations in the same region. The row has been
removed rather than corrected, because the correct founder was not established,
and `companies.csv` now carries a note distinguishing the two organisations.

That pass added fourteen co-founders that single-name attributions had hidden:
Stears has four founders rather than one, Indicina four, Charis UAS three, and
Masakhane, Mawdoo3, Mozn, Awarri, eHealth Africa and the Makerere AI Lab two
each. It corrected two founding years, eHealth Africa from 2009 to 2010 and the
Makerere lab from 2009 to 2011. And it established that six founders'
nationalities cannot be determined from public sources, so those rows now carry
`NA` rather than an inferred country.

**The level B pass.** Sixty-four of sixty-five attributions were confirmed. One
failed: Bell Ihua was recorded as founder of the Africa Polling Institute, and
neither the institute's own staff page nor any press coverage supports it. He is
its executive director, and that is all that is established; the row has been
removed and the company note records the distinction. One attribution remains at
level B, Mustafa Damar among MetroPOLL's founding shareholders, which rests on a
single Turkish source.

The pass surfaced a second, larger problem: **eleven founding years in
`companies.csv` were wrong**, in a file where the founder attributions around
them were mostly right.

| Organisation | Was | Is | Effect |
|---|---|---|---|
| ACLED | 2014 | 2005 | scaleup to established |
| One to One for Research and Polling | 2004 | 2014 | established to scaleup |
| MetroPOLL | 2007 | 2004 | scaleup to established |
| Somali Public Agenda | 2017 | 2018 | startup to scaleup |
| Plus 94 Research | 1995 | 1998 | none |
| Sigma Conseil | 1996 | 1998 | none |
| Statistics Lebanon | 1996 | 1994 | none |
| Information International | 1992 | 1995 | none |
| Baseera | 2011 | 2012 | none |
| Busara | 2012 | 2013 | none |
| Global InfoAnalytics | 2020 | 2019 | none |

Four of the eleven moved an organisation between maturity classes, so any
analysis cutting the register by `maturity_class` before this revision was
using four misclassified rows. The direction is not systematic; errors run both
ways. Two further organisations, Research World International and
Geocartography, have founders confirmed but founding years that no public source
establishes, and their `notes` now say so rather than carrying an unsupported
number.

Verification also added twenty co-founders and four ownership relationships that
the original coding had missed: Busara has four founders rather than one,
MetroPOLL at least two, Taranis four, mPharma three, CDD-Ghana three, Apollo
Agriculture three, Helium Health three, and 60 Decibels, Mercor, Scale AI, Plus
94, mSurvey and Information International two each. The Arab Advisors Group sold
a 55% stake to the Arab Jordan Investment Bank in 2005, which makes it one of the
few MENA research firms in this register with a documented institutional owner.

**The level A audit.** Five founder rows carried level A from the original
coding and had never been through a pass. Four were confirmed: Tobi Olatunji at
Intron Health, Nour Al Hassan at Tarjama and its Arabic.AI venture, and Cameron
Fink at Aaru. One was wrong in kind rather than in detail: KoboToolbox was
attributed to the Harvard Humanitarian Initiative as an institution, when it was
founded in 2005 by Phuong Pham and Patrick Vinck and hosted at HHI until it
incorporated independently in 2019. That row is now two individual founders plus
a funder row for HHI, and the founding year moves from 2010, which was the year
UNDP adopted the tool, to 2005.

Then a sample of eleven rows the earlier passes had marked verified was checked
again independently, to test whether those passes were reliable. **No attribution
in the sample was wrong. Six were incomplete.** Stears, Indicina, Masakhane,
Awarri, Twaweza, Laterite and the Mass Public Opinion Institute came back exactly
as coded. Mozn has four founders and the file held two; Lelapa AI has six and the
file held one; Clearview AI, Hivemapper, Aaru and 54gene each had a co-founder
missing.

That is the finding worth carrying out of this exercise. **The failure mode in
founder data is not misattribution, it is undercounting.** The earlier passes
searched to confirm the name already in the file, which confirms a true fact and
leaves a false impression of completeness. Searching to enumerate all founders
instead finds the missing ones.

**The enumeration sweep.** Every organisation still carrying a single founder row
was then searched again with the question reversed, asking who founded it rather
than whether the recorded person did. Of 42 organisations, **36 came back genuinely
single-founder and 6 were missing a founder**: Sagaci Research was co-founded with
Joao Terlica, the Institute for Justice and Reconciliation with Fanie du Toit,
Hello Tractor with Van Jones, Intron Health with Olakunle Asekun, Gallup's American
Institute of Public Opinion with the Chicago agent Harold R. Anderson, and the
Levada Center by the VCIOM staff who resigned collectively in 2003, of whom Lev
Gudkov is the one consistently named.

A seventh case is a different kind of gap. Geocartography is run by Avi Degani and
Rina Degani, who owns and chairs it; no source calls her a founder, so she is
recorded as a controlling owner rather than guessed into the founder column.

Six organisations describe their own founder as a "co-founder" or refer to a
founding group while naming nobody else: Baseera, the Jerusalem Media and
Communication Centre, the Syrian Center for Policy Research, One to One,
UjuziKilimo and Digital Umuganda. Those rows now say so in their notes. **The
absent names are a documented gap rather than a claim that these organisations had
one founder.** Three organisations are positively confirmed as single-founder by
sources that address the question directly: Surge AI, where Edwin Chen had no
co-founder and no investors, Sama, and Ipsos, where Jean-Marc Lech joined as
co-president seven years after founding and was not a founder.

The founder layer now holds 139 rows over 76 organisations, 136 at level A.
Treat founder counts in this file as a lower bound.

The domestic-founder figures above are computed only over the 132 rows where
nationality is established.

### The funders

68 funding relationships across 14 organisations, from 53 distinct funders. The
set is more diffuse than expected, but a recognisable core recurs: the Ford
Foundation in four of the fourteen, Sweden's Sida, USAID and the Hewlett
Foundation in three each, and the European Union, Germany's BMZ, Google.org,
Canada's IDRC, the UK's FCDO and the World Bank in two each.

By category, 27 relationships come from private foundations, 21 from bilateral
aid agencies, 10 from multilaterals, 4 from corporates, 3 from state research
bodies, 2 from universities and one from a media group. Forty-one of the 68
fund Sub-Saharan African organisations.

Afrobarometer publishes sixteen funders and CDD-Ghana, one of its regional hubs,
publishes ten more. Arab Barometer has raised over five million dollars from MEPI,
the National Science Foundation, the Qatar National Research Fund, USIP, IDRC,
Carnegie Corporation, the Luce Foundation and the BBC. ACLED runs on the US State
Department, the Dutch and German foreign ministries, IOM, the World Bank, the US
Department of Defense and the European Research Council. PCPSR is funded mostly by
the European Union and the Ford Foundation. Twaweza names a five-donor core
consortium of Sida, FCDO, Hewlett, SNV and Hivos.

### What that implies for the access finding

Section 4 established that academic and nonprofit collectors publish at 90% while
every revenue-funded category sits between 8% and 25%. Section 15 found that what
reaches Africa is grant-funded and therefore published. Both hold. This section
adds the condition.

The openly accessible layer over Africa and MENA exists because Northern
foundations and aid ministries pay for it, and it is contingent on decisions
taken in capitals with no accountability to the populations being measured. The
register already contains one instance of that contingency arriving: former USAID
Africa Bureau officials publicly urging the agency to save Afrobarometer's
funding, which nobody does about a secure income.

Set against section 14, the asymmetry is stark. A commercial data firm that loses
its market is bought, and its holdings continue under a new owner; that is what
happened to every MENA and African field agency that exited. A grant-funded
collector that loses its funder has no acquirer, because there was never a
revenue stream to buy. The open layer is the part of this industry that can
disappear rather than change hands.

### State control

15 collectors have an established state controlling owner: the African and Middle
Eastern space agencies, and the Russian, Chinese, Iranian, Egyptian and Uzbek
bodies. Their access profile is the one section 4 reports, mostly closed. State
control and open access are close to unrelated in this data.

### What is missing

Four fifths of the register has no stakeholder row, and the gap is not random.
The bias here runs opposite to most business datasets. Grant-funded organisations
publish their funders, often on a dedicated page, because donors require
acknowledgement. Privately held firms publish nothing about ownership unless a
transaction is announced. This file therefore documents the open layer well and
the commercial layer poorly, and owner-managed independents, the largest ownership
category in the register at 152 operating firms, are almost entirely absent from
it. Extending this layer means company registry work in jurisdictions where
registries are often not open.

## 18. The demand side, and why it is a different kind of claim

Everything above this section describes supply. `docs/demand.md` takes the buyer side
and keeps it separate on purpose, because the two are not knowable to the same standard.

What can be computed from the register is entry. Among 704 for-profit organisations,
682 carry a founding year, so the share of a segment founded since 2015 can be measured
exactly. It is a revealed preference, not demand: founders went where they expected to
be paid. Printed next to the exit rate it separates four situations, and the pairing
matters, because the two highest-entry segments after the expanding ones are also among
the highest-exit. Mobile location and mobility is 46 percent recent and has lost 8 of
24 firms, the worst exit rate in the register. Financial alternative data is 48 percent
recent and has lost 4 of 23. Neither is growth.

Expanding on both measures: AI training data (67 percent recent, 8.0 percent exit),
web data extraction (64, 0.0), distributed contributor sensing (60, 10.0), climate and
environmental risk (57, 4.8), earth observation (47, 8.8). Consolidating: consumer data
brokerage (4 percent recent, 25.0 percent exit), media and audience measurement (5,
18.2), retail scanning (11, 21.1). The two oldest segments, in-country field agencies
and full-service survey firms, are neither: their entry shares are 16 and 24 percent and
their exit rates, 4.6 and 6.7, are among the lowest in the file.

What cannot be computed is who pays. `data/demand.csv` holds 92 researched rows across
all 23 segments, and the composition of that file says something about the record before
it says anything about the industry. State, donor and party buyers are 33 of 92 rows and
11 of the 17 rows that reach evidence level A, because a government purchase leaves an award
notice and a corporate subscription leaves nothing. Any account of data buying built
from public documents will over-count the state, this one included, and section 2 of
`docs/demand.md` states that rather than presenting the concentration as a finding.

The MENA rows were then extended in a round of their own, because they were the file's
weakest. 17 of the 92 rows now carry MENA, and 11 of those 17 have a state, a donor or a
political party as the buyer against 33 of 92 across the whole file. Part of that is real
and part is the round having gone looking for it, and the two cannot be separated from
inside the file. What the round did establish is a demand structure with no counterpart
elsewhere in the register: in Egypt a CAPMAS permit is needed to survey more than five
people and the agency may alter the questions; in Saudi Arabia GASTAT is the sole
official statistical reference and runs its own fieldwork rather than procuring it. One
state gates who may collect and the other collects in-house, and both outcomes suppress
the commercial field agency market that exists in Kenya or Nigeria. The register's thin
count of Gulf field agencies follows from that, and is not an enumeration gap.

Two of the region's standing public opinion series are paid for by governments that are
not the governments being surveyed: Arab Barometer by the US Middle East Partnership
Initiative, USAID, the NED, the BBC and Carnegie, and the Arab Opinion Index by Qatari
state-backed ACRPS. The largest fieldwork buyer in the region is neither, it is the
humanitarian system in Syria, Yemen, Iraq and Sudan, and that buyer is contracting: the
2025 global appeal was funded at 12bn, the lowest in a decade, with Syrian humanitarian
staffing projected to fall by at least 40 percent. Section 6 of `docs/demand.md` sets out
what commercial demand does exist, which is Gulf consumer goods, advertising measurement
and regulated credit files, and why Israel and Turkiye should be pulled out of any MENA
aggregate computed from this register.

A matching round was then run on Africa. 20 of the 92 rows now carry SSA, 11 of them
with a state, a donor or a political party as the buyer and 9 with a commercial one,
against 11 and 5 for MENA. Africa has proportionally more commercial demand than MENA in
this file, which was not the expected result. Both regions were searched deliberately and
neither share is a measurement, but the comparison holds in the direction it runs: African
lenders buy alternative credit data in a genuine market, where the Gulf equivalent is a
state-linked bureau holding the file by regulation; African media houses buy and publish
election polling; Kantar runs consumer panels in 16 African countries against two in the
Middle East.

What Africa carries that no other region does is the concentration of the aid shock. Seven
of the ten rows in the file coded `declining` are MENA or African and every one of the
seven has a donor or a donor-funded state programme as the buyer. Three are African:
Afrobarometer, whose published funders are entirely foreign states, foundations and
multilaterals and whose core donor since 1999 was USAID; PEPFAR, where 2025 disruptions
cut roughly 30 percent of funding, closed about 1714 treatment sites and were associated
with a 22 percent global fall in HIV testing; and humanitarian assessment, where Sudan
alone needs 2.9bn for 2026 inside the weakest global appeal in a decade. Read with the DHS
termination in section 3, that is one buyer withdrawing from four segments at once, with
no commercial buyer stepping into any of them.

Two African cases sharpen what the register means by demand. Digital Earth Africa is
funded by the Helmsley Charitable Trust and Australian DFAT, hosts over 6 petabytes for
more than 29000 users, and is free at the point of use, so continental earth observation
capacity is a donated good with no African buyer at all. And OpenAI paid Sama about 12.50
dollars an hour per worker for labelling while Kenyan workers received around 2 dollars,
with Meta's 3.9m moderation contract ending and about 200 Nairobi jobs going. Nothing
African was bought in those transactions: the buyer wanted labour, the data belonged to
the buyer throughout, and what stayed was a wage. AI training data is the fastest-filling
segment in the register worldwide. Its African form is a labour contract and its MENA form
is a state procurement, and neither leaves a local firm owning a dataset.

One result there bears directly on section 1 of this document. Six segments have a
documented state security buyer. Operating for-profit firms in those six disclose
record-level data to researchers at 10.0 percent against 15.4 percent elsewhere, 15 of
150 against 74 of 480. The gap is small, the denominators are small, and segment
composition could produce it without any relationship between security demand and
secrecy. It is recorded as an observation to test, not as an effect.
