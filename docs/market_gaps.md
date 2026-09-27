# Market white space

Where a venture could enter, computed from the register. A different question
from `docs/real_gaps.md`, which asks where data is not collected. This asks where
demand is documented and supply is thin.

**What this can and cannot say.** The register has no revenue variable and will
not get one. Nothing here is a market size, a margin or a willingness to pay. A
gap below means few incumbents against documented demand, which is a place to
look. `scripts/14_market_gaps.py` recomputes every table.

---

## 1. Selling on different terms, where no incumbent does

The strongest opportunity in the file, because it does not depend on finding
under-served geography. Eight segments have at most one organisation offering a
researcher any route to record-level data, and five have none at all.

| Segment | Firms | Offering access | Demand direction |
|---|---|---|---|
| Consumer brokerage | 27 | **0** | contested, declining, rising, stable |
| Biometric and identity | 17 | **0** | rising |
| Retail scanning and pricing | 16 | **0** | stable |
| Trade and logistics | 13 | **0** | rising |
| Expert networks | 6 | **0** | stable |
| Media and audience measurement | 26 | 1 | rising, stable |
| Financial alternative data | 22 | 1 | rising |
| Crowdsourced micro-tasking | 9 | 1 | rising |

Credit risk is the sharpest case: **178 of 178 country-domain cells closed, with
no accessible provider anywhere on earth.** The one famous research route, the
Equifax and New York Fed Consumer Credit Panel, is restricted by contract to that
central bank's own staff.

The reason this is an opening rather than a curiosity is on the demand side. Four
of the rising segments in `data/demand.csv` are rising because of a rule:
climate disclosure under ISSB and CSRD, sanctions screening, regulatory
acceptance of real-world evidence, and know-your-customer obligations. A buyer
who must satisfy an auditor needs provenance, lineage and the right to let a
third party check the data. Not one incumbent in the eight segments above sells
that. An entrant whose product is auditability rather than volume competes
against nobody on the axis that the regulated buyer cares about.

---

## 2. Methods proven elsewhere that nobody in the region runs

Each row is a collection method with commercial users in the register and zero
organisations headquartered in the region using it. The proof cases are named, so
the question is transfer rather than invention.

### MENA

| Method | Users worldwide | Proven by | Why the absence is odd |
|---|---|---|---|
| Telecom network data | 8 | Positium (EST), Teralytics (CHE), Orange Flux Vision (FRA) | Gulf operators hold some of the densest mobility data anywhere and none of it is a product |
| Environmental sampling | 6 | Biobot, WastewaterSCAN (USA), NatureMetrics (GBR) | Wastewater epidemiology needs sewer coverage, which the Gulf has and most of the register's African countries do not |
| Radio frequency geolocation | 4 | HawkEye 360 (USA), Unseenlabs (FRA) | Red Sea and Gulf shipping is the most surveilled water on earth and the surveillance is sold from Virginia and Brittany |
| Transaction feeds | 18 | Yodlee (USA) | Saudi open banking licensing began in 2019 and Lean Technologies is the only register firm using it |
| Voluntary citizen reporting | 2 | Ushahidi (KEN) | The method was invented in Africa for exactly the documentation problem MENA conflicts present |
| Passive acoustic | 2 | Rainforest Connection, SoundThinking (USA) | |
| Web interception | 1 | RIWI Corp (CAN) | One firm worldwide holds the whole category |

### Sub-Saharan Africa

| Method | Users worldwide | Proven by |
|---|---|---|
| Radio frequency geolocation | 4 | HawkEye 360 (USA), Unseenlabs (FRA) |
| Passive acoustic | 2 | Rainforest Connection (USA), SoundThinking (USA) |
| Radio propagation sensing | 2 | Origin Wireless (USA), Vayyar (ISR) |
| Web interception | 1 | RIWI Corp (CAN) |
| Device content acquisition | 4 | Cellebrite, NSO Group (ISR) |

Passive acoustic is the one to look at twice. Rainforest Connection's use case is
detecting chainsaws in forest in real time, and the register holds no African
organisation doing it, in the continent with the fastest forest loss and the
thinnest ranger coverage. The hardware is a recycled phone in a box.

---

## 3. Rising demand, almost no domestic supply

From the demand layer, restricted to segments with a demand row coded rising.

| Region | Segment | Domestic for-profit firms | Worldwide |
|---|---|---|---|
| MENA | Crowdsourced micro-tasking | 0 | 9 |
| MENA | Trade and logistics | 1 | 13 |
| MENA | Biometric and identity | 1 | 17 |
| MENA | Climate risk | 1 | 24 |
| MENA | Audience measurement | 1 | 26 |
| SSA | Web data extraction | **0** | 16 |
| SSA | Crowdsourced micro-tasking | 0 | 9 |
| SSA | Audience measurement | 1 | 26 |
| SSA | Climate risk | 1 | 24 |

Audience measurement is the clearest single opening. MENA digital advertising
reached about 8.19bn dollars in 2025 with Saudi Arabia growing 19 percent, and
African digital advertising about 3.8bn heading for 6.5bn by 2029. Between them
those markets support two domestic measurement firms. When the UAE industry body
went looking for a cross-media measurement supplier in 2022 it appointed Ipsos,
a French firm. The buyer structure is a standing committee of broadcasters and
advertisers, which is hard to displace and, once won, close to permanent.

Web data extraction in Africa is the starkest number in the file: zero firms
against 16 worldwide, in a segment with a 0 percent exit rate and 64 percent of
its firms founded since 2015.

---

## 4. The substitution opening created by the donor collapse

The register documents one demand shock more clearly than anything else. USAID
ended the Demographic and Health Surveys in February 2025, removing roughly 47m
dollars a year and surveys in more than 25 countries. PEPFAR disruptions cut
about 30 percent of funding and closed some 1,714 treatment sites. The 2025
humanitarian appeal was the weakest in a decade.

The demand did not go away. Governments, lenders and donors still need the
numbers those surveys produced, and two firms already sell the substitute:
**Atlas AI** infers village-level asset wealth from satellite imagery, and
**Fraym** anchors imagery on existing survey points to produce hyperlocal
estimates. Both are American. Neither MENA nor Africa has a single firm selling
model-based substitutes for the surveys that stopped in MENA and Africa.

There is a catch worth stating, because it is also the moat. Fraym's method
depends on a stock of survey points that donor funding is no longer replenishing,
so the accuracy of the substitute decays as the thing it substitutes for
disappears. An entrant that pairs a thin, cheap, continuing ground-truth panel
with imagery has something neither incumbent has, and the register's African
field agencies are the cheapest such panel in the world to run.

---

## 5. Capital that admits these applicants

14 open programmes in `data/grant_programmes.csv` accept MENA or African
applicants. The data-specific ones:

| Programme | Award | Regions |
|---|---|---|
| Lacuna Fund | 25k-250k | SSA, LAC, SAS |
| AI4D Responsible AI | 100k-1m | SSA |
| GSMA Innovation Fund | 125k-315k | SSA, SAS, SEA, OCE, LAC |
| Gates Grand Challenges | 100k-500k | SSA, SAS, LAC, SEA |
| Fuze by Digital Africa | 22k-110k | SSA, MENA |
| The DIV Fund | 25k-1m | SSA, SAS, LAC, SEA, MENA |

Seed-scale, non-dilutive and aimed at exactly the categories above. Lacuna Fund
in particular exists to pay for labelled datasets in low-resource languages,
which is the AI training data opportunity with its funding already attached.

---

## 6. What the register says not to do

**Do not enter consumer brokerage or retail pricing on the incumbent model.**
Consumer brokerage has lost 20.6 percent of the firms ever recorded here and 12
percent of the survivors were founded since 2015. Retail pricing has lost 20
percent with 10 percent recent entry. Both are consolidating, both sell on closed
terms, and both are in column 1 above. The opening in them is the terms, not the
product.

**Do not assume the absence of a firm means an absence of competition.** 135 of
138 apparent regional gaps in this register are ownership gaps: somebody serves
that market from somewhere else. An entrant in MENA audience measurement is not
entering an empty market, it is competing with Ipsos. What the ownership gap
buys is proximity, language, price and regulatory standing, which is a real
advantage and a different one from first-mover.
