# The demand side: who buys, and which segments are filling up

Two questions, two different kinds of answer. Entry into a segment can be
measured from the register, because every for-profit firm carries a founding
year. Who pays cannot be, because the register was built from the supply side
and no firm in it publishes a customer list. The first half of this document is
computed. The second half is a new file, `data/demand.csv`, built the same way
as `data/grant_programmes.csv`: one row per segment and buyer category, each
carrying its own evidence level and source, and no row asserted without one.

Everything here concerns the 704 for-profit organisations in the register.
682 carry a founding year.

## 1. Entry is the only demand proxy this register can produce

There is no revenue in this file and there will not be. What can be counted is
where founders and capital went, which is a revealed preference: people started
firms where they expected to be paid. Reported as the share of a segment's dated
firms founded in 2015 or later, printed next to the exit rate, because a segment
can fill with entrants who all fail.

Full table in `output/tab33_entry_cohorts.txt`. Segments with at least six dated
firms, ordered by recent share:

| segment | recent % | n | exit % |
|---|---|---|---|
| AI training data | 67 | 50 | 8.0 |
| Web data extraction | 64 | 14 | 0.0 |
| Distributed contributor sensing | 60 | 10 | 10.0 |
| Climate and environmental risk | 57 | 21 | 4.8 |
| Financial alternative data | 48 | 23 | 17.4 |
| Earth observation | 47 | 68 | 8.8 |
| Mobile location and mobility | 46 | 24 | 33.3 |
| Health real-world data | 44 | 34 | 17.6 |
| Biometric and identity | 42 | 19 | 10.5 |
| B2B firmographic | 38 | 24 | 8.3 |
| Trade and logistics | 36 | 14 | 7.1 |
| Crowdsourced micro-tasking | 33 | 9 | 11.1 |
| Social listening and OSINT | 33 | 21 | 0.0 |
| Expert networks | 29 | 7 | 28.6 |
| Vehicle IoT and telemetry | 29 | 21 | 14.3 |
| Panel and sample supply | 24 | 34 | 14.7 |
| Full-service survey and insights | 24 | 90 | 6.7 |
| Data collection instrumentation | 17 | 18 | 5.6 |
| In-country field agency | 16 | 130 | 4.6 |
| Retail scanning and pricing | 11 | 19 | 21.1 |
| Media and audience measurement | 5 | 22 | 18.2 |
| Consumer data brokerage | 4 | 28 | 25.0 |

Reading the two columns together separates four situations
(`output/tab34_segment_profile.txt`):

- **Expanding**, high entry and low exit: AI training data, web data extraction,
  distributed sensing, climate risk, earth observation.
- **Churning**, high entry and high exit: financial alternative data, mobile
  location and mobility. Mobile location has the highest exit rate in the
  register at 8 of 24 firms and is still taking entrants.
- **Consolidating**, low entry and high exit: consumer data brokerage, media and
  audience measurement, retail scanning, expert networks, health real-world data.
- **Mature and stable**, low entry and low exit: in-country field agencies,
  full-service survey firms, data collection instrumentation.

The two oldest segments in the register are the two that the discipline of
survey research grew out of. 52 of 109 dated field agencies and 39 of 90 dated
survey firms were founded before 2000. Neither is dying: their exit rates, 4.6
and 6.7 percent, are among the lowest in the file. They are simply not where
new firms are being started.

## 2. The buyers that can be documented are mostly states

`data/demand.csv` holds 92 rows across all 23 segments and 16 buyer categories.
The largest categories by row count are corporate marketing (9), financial
investors (7), civil government (7), corporate operations (6) and state security
agencies (6).

State, donor and party buyers are 33 of 92 rows. They are 11 of the 17 rows that reach
evidence level A. That asymmetry is a fact about the record, not about the
industry: a government purchase leaves an award notice, a contract value and
sometimes a court case, while a corporate subscription leaves nothing at all.
Any account of who buys data that relies on public documents will over-count
the state. The demand layer records this in `output/tab37_evidence_visibility.txt`,
where 9 of 17 A rows are public awards and 38 of 54 B rows are trade reporting.

The documented state purchases are large and concrete:

- The US National Reconnaissance Office's Electro-Optical Commercial Layer
  awards, up to 3.24bn over ten years to Maxar and up to 1.02bn to BlackSky,
  with a third undisclosed award to Planet. One buyer underwrites three of the
  largest firms in the earth observation segment.
- Location data sold to DHS, ICE, the FBI, the IRS and the Department of
  Defense through Venntel, and to the Secret Service, CBP, the DEA and US
  Special Operations Command through Babel Street. The purchase substitutes for
  a legal process the agency would otherwise have to go through, which is why
  this row is coded as contested rather than rising.
- LexisNexis Risk Solutions to ICE, reported at 16.8m, with Thomson Reuters
  CLEAR reported in use by over 3,400 law enforcement agencies.
- The Intelligence Community OSINT Strategy for 2024 to 2026, which commits US
  agencies to buying open source material as a standing discipline.

Six segments have a documented state security buyer: consumer brokerage, earth
observation, biometric and identity, mobile location, social listening and
OSINT, trade and logistics. Operating for-profit firms in those six disclose
microdata to researchers less often than the rest: 15 of 150 against 74 of 480,
10.0 against 15.4 percent. The gap is small and the number of firms behind it is
small, and segment composition could produce it on its own, so it is reported
here as an observation and is not offered as an effect.

## 3. Two demand shocks in opposite directions, landing in different places

The register's period contains one documented collapse and one documented boom,
and they do not fall on the same firms.

USAID ended support for the Demographic and Health Surveys programme in
February 2025. That removed roughly 47m a year and surveys in more than 25
countries, and it terminated named African partners including the African
Institute for Development Policy in Malawi and the Institut de Formation et de
Recherche Demographiques in Cameroon. Donor money is the load-bearing buyer for
African field agencies, which is the register's largest segment by firm count
and one of its two oldest.

Over the same period, AI developers bought training data at prices no buyer in
this industry had paid before: News Corp to OpenAI reported at over 250m across
five years, Amazon to the New York Times at 20m to 25m a year, Reddit
disclosing 203m in aggregate licensing contract value in its IPO filing, and
Meta paying 14.3bn for 49 percent of Scale AI, which is a buyer taking equity in
its own supplier.

Both shocks hit segments in this register. They hit different regions. The
collapse lands on African and Asian fieldwork; the money lands on North American
and Western European platform holders and annotation firms.

## 4. Four of the rising segments are rising because of a rule

Climate risk sells because ISSB and CSRD reporting obliges banks, insurers and
asset managers to produce hazard and transition figures. Trade and logistics
compliance sells because sanctions regimes expanded. Health real-world data
sells because regulators accept it in submissions. Biometric identity sells in
Africa because know your customer rules oblige banks to verify, on registries
built with World Bank loans.

Demand created this way moves with rule-making rather than with any underlying
appetite, and suppliers understand that. The RWE Alliance, formed by Aetion,
Flatiron Health, IQVIA, Syapse and Tempus, exists to lobby the FDA and Congress
on the regulatory acceptability of the product its members sell. That is
suppliers acting to enlarge a buyer's willingness to buy, and it is the clearest
case in the file of the demand side being manufactured rather than found.

## 5. Where the buyer is a committee of the sellers' customers

Media and audience measurement has the lowest entry share in the register after
consumer brokerage, 1 of 22 dated firms founded since 2015, and it has a
distinctive buyer structure. Barb in the United Kingdom is funded jointly by the
BBC, ITV, Sky, Channel 4, Channel 5 and the advertising industry through the
IPA, with advertisers represented through ISBA, and it contracts measurement out
to Kantar Media, Ipsos and RSMB. The buyer is a standing committee of the parties
being measured. Entry is closed by design, not by economics, which is why five
US media owners had to form a joint venture to certify alternative measurement
rather than simply buying from a new supplier.

## 6. MENA: who actually pays, and why so little of it is commercial

17 of the 92 rows in `data/demand.csv` carry MENA as their geography, after a
round of research aimed at this region alone. 11 of the 17 have a state, a
donor or a political party as the buyer. Across the whole file the equivalent
share is 33 of 92. The regional figure is higher partly because MENA was
searched harder and partly because it is true, and the two cannot be separated
from inside this file.

Start with the size of the commercial market, because it bounds everything else.
ESOMAR puts the Middle East and Africa together at about 3 percent of global
insights activity, roughly 4.4bn in 2022, the smallest region in the world.
Growth was second highest globally in nominal terms at 9.2 percent and negative
at -1.2 percent once inflation is removed. A region can look like it is growing
and be shrinking in what its buyers actually purchase.

### The state buys, and it also licenses

This is the structural fact that has no counterpart in any other region of the
register. In Egypt a permit from CAPMAS is required to survey more than five
people; the agency can alter questions or refuse outright, and an institutional
ethics approval does not substitute for it. In Saudi Arabia, GASTAT is the sole
official reference for statistical work in the Kingdom, and it runs its own
field, telephone and self-reporting surveys across economic, social,
environmental and spatial domains in every region of the country.

Those are two different mechanisms with the same result. Egypt gates who may
collect. Saudi Arabia collects in-house instead of procuring. Either way the
commercial field agency market that exists in Kenya or Nigeria does not form,
and the register's thin count of Gulf field agencies is a consequence of that
rather than a gap in enumeration.

Since September 2023, SDAIA has also been the authority enforcing the Saudi
Personal Data Protection Law, with cross-border transfer conditions and fines up
to 5m riyals per breach. The same body sets data policy, enforces the privacy
law, and, through HUMAIN, builds the national AI model. Buyer, regulator and
producer are one institution.

### The largest standing buyer of MENA public opinion data is a foreign state

Arab Barometer publishes its funders wave by wave. Waves VII and VIII were paid
for by the US Middle East Partnership Initiative, USAID, the National Endowment
for Democracy, the BBC, Carnegie Corporation and three US universities. The
Arab Opinion Index, the region's other standing series, is produced by ACRPS in
Doha, which is Qatari state backed.

Neither is a commercial purchase, and between them they cover most of what is
published about Arab public opinion. USAID's dismantling in 2025 removed one of
the named funders of the first of them, which is the same shock that ended the
DHS programme and for the same reason.

### Humanitarian assessment is the region's largest fieldwork buyer, and it is contracting

Syria, Yemen, Iraq and Sudan generate more paid data collection than the Gulf
does, through the humanitarian system rather than through any market. REACH,
the joint initiative of IMPACT Initiatives, ACTED and UNOSAT, co-chairs the Iraq
Assessment Working Group with OCHA and runs about 400 assessment and data staff
across more than 20 countries. The buyer and the collector sit inside the same
aid system, so this is an internal allocation and not a market.

That allocation is shrinking. The 2025 global humanitarian appeal was funded at
12bn, the lowest in a decade, with 25 million fewer people reached than in 2024.
Aid cuts are projected to remove at least 40 percent of humanitarian staffing in
Syria. Yemen's 2025 plan received under a quarter of what it asked for.
Assessment work is an early casualty of a shortfall, because it is not itself
lifesaving and is the easiest line to defer.

### What commercial demand does exist, and where

Five of the 17 MENA rows have a commercial buyer, and they cluster tightly:

- **Gulf consumer goods.** NielsenIQ retail measurement covers more than 90,000
  outlets in Saudi Arabia and 30,000 in the UAE. Kantar runs consumer panels in
  Saudi Arabia and the UAE, against 16 in Africa. This is the clearest genuinely
  commercial data purchase in the region.
- **Advertising and measurement.** MENA digital advertising reached about 8.19bn
  in 2025, Saudi Arabia taking roughly 46 percent of it and growing 18.9 percent.
  In 2022 the Advertising Business Group appointed Ipsos to run UAE cross-media
  measurement, which is the same buyer structure as Barb in the United Kingdom:
  an industry committee of the measured parties buying jointly. The predecessor
  panel, tview, ran trials from 2011 and stalled on funding.
- **Credit files.** SIMAH draws on roughly 330 credit data sources under Saudi
  Central Bank supervision; Al Etihad Credit Bureau takes data from banks,
  telecoms, utilities, rental firms and insurers, with Tabby and Tamara now
  reporting into both. Supply is compulsory by regulation and the bureau is a
  state or state-linked monopoly, so no brokerage market of the North American
  kind forms around it.

### The newest MENA buyer is a sovereign AI programme

ALLaM was built by SDAIA with more than 400 experts and 160 government bodies
and is now run by HUMAIN. Falcon comes from TII in Abu Dhabi, Fanar from QCRI in
Doha, Jais from G42's Inception and MBZUAI. Each needs Arabic corpora and
dialect annotation, and in every case the buyer is a state body or a state fund.
AI training data is the fastest-filling segment in the register worldwide, and
the MENA version of that demand is state demand.

### Two countries inside the region that do not behave like it

Israel and Turkiye are both inside this register's MENA definition and both
invert the regional pattern, in opposite directions. Reporting since 2023
describes Palantir supplying AI data analytics to Israel and Unit 8200 holding
about 8,000 TB on Microsoft Azure: a domestic state security buyer with budgets
that resemble North American ones. Turkiye has the region's densest political
polling market, with twenty published voting intention polls in 2026 against a
general election not due until 2028, commissioned by parties and media outlets
that are usually not named.

Any MENA aggregate computed from this register mixes those two countries with
Gulf states that produce in-house, with conflict economies where the buyer is
the humanitarian system, and with North African states that license who may
ask questions at all. The regional code is an administrative convenience here,
not a market.

### What is still missing

Four things were searched for in this round and not found: published contract
values for Gulf government purchases of data or research services; any
decomposition of the ESOMAR Middle East and Africa figure into domestic
corporate buyers against foreign agencies and donors; energy sector purchases
of earth observation by Aramco or ADNOC; and terms for any telecom operator
data sale in the region. Two MENA rows remain evidence C for that reason. The
absence of Gulf procurement records is itself a finding about those states and
is treated as one, not as a hole to be filled with plausible numbers.

## 7. Africa: more commercial demand than MENA, and a harder donor shock

20 of the 92 rows carry SSA, after a round aimed at this region alone. 11 of the
20 have a state, a donor or a political party as the buyer and 9 have a
commercial one. The MENA equivalents are 11 and 5. Africa has proportionally
more commercial demand than MENA in this file, which was not the expected
result, and it is stated with the same caveat as everything else here: both
regions were searched deliberately and neither share is a measurement.

### The aid shock lands harder here than anywhere else in the register

Seven of the ten rows in the whole file coded `declining` are MENA or African,
and every one of those seven has a donor or a donor-funded state programme as
the buyer. Three of them are African:

- **Afrobarometer.** Its funders are published and they are all foreign states,
  foundations and multilaterals: SIDA, USAID through USIP, the Mo Ibrahim
  Foundation, Open Society, Gates, Hewlett, the EU, the NED, the Mastercard
  Foundation, the World Bank and GIZ. USAID has been a core donor since the
  network started in 1999, and in 2025 former US Africa Bureau officials
  publicly called for it to be rescued. The continent's flagship public opinion
  series has never had a domestic commercial buyer.
- **PEPFAR.** Disruptions through 2025 cut roughly 30 percent of funding, closed
  about 1,714 treatment sites and were associated with a 22 percent global fall
  in HIV testing. US money had built national health information systems.
  African health data is largely a by-product of donor-funded service delivery,
  so it contracts exactly when the service does, and the contraction is not
  visible as a data story.
- **Humanitarian assessment.** Sudan alone requires 2.9bn for 2026 with 33.7
  million people assessed as needing assistance, a 10 percent rise, inside a
  global appeal funded at its lowest level in a decade.

Put beside the DHS termination in section 3, this is one buyer withdrawing from
four different segments at once. No commercial buyer is stepping into any of
them, and nothing in this file suggests one will.

### Even the census depends on a lender

The DRC census is costed at 192m, with 100m from the World Bank and 80m from the
African Development Bank, and a financing gap still open. Nigeria's census
remains delayed for want of funding. The state is the commissioning party on
paper and the lender decides whether the count happens. The same pattern runs
through the identity layer already in the file: the Nigeria digital ID project
was approved at 430m, co-financed by the World Bank, the French development
agency and the European Investment Bank.

Digital Earth Africa is the purest version of this. It is funded by the Helmsley
Charitable Trust at 10m dollars and Australian DFAT at 9m Australian dollars,
with AWS support, and it hosts over 6 petabytes for more than 29,000 users. The
data is free at the point of use, so continental earth observation capacity is a
donated good with no African buyer at all.

### Demand can also arrive as outsourced labour rather than as a purchase

OpenAI paid Sama about 12.50 dollars an hour per worker to label toxic content
while the Kenyan workers received around 2 dollars. Meta's 3.9m content
moderation contract with Sama was not renewed, about 200 Nairobi jobs went, and
the dispute reached the Kenyan courts.

Nothing African was bought in those transactions. The buyer wanted labour, the
data being produced belonged to the buyer throughout, and the value that stayed
in Kenya was a wage. AI training data is the fastest-filling segment in the
register worldwide; its African form is a labour contract and its MENA form is a
state procurement, and neither produces an African or Arab firm that owns a
dataset.

### What commercial demand exists, and it is more than the Gulf has

Nine of the 20 African rows have a commercial buyer, and they are less
concentrated than MENA's:

- **Alternative credit data.** Lenders buy mobile money history, airtime
  patterns, handset and utility payment records to score borrowers with no
  credit file. This is the clearest case on the continent of firms paying for
  data about people, and it contrasts sharply with the Gulf, where a
  state-linked bureau holds the file by regulation and no brokerage market
  forms around it.
- **Mobile survey work for multinationals.** GeoPoll sells to global brands,
  media agencies and TV networks alongside development organisations, with
  Diageo in Nigeria among the named cases. African commercial demand is mostly
  multinational demand executed locally, not domestic firms buying research.
- **Election polling bought by media.** Kenyan media houses commission and
  publish presidential race polling, which is why those numbers reach the
  public at all. Parties also commission privately, TIFA lists them as clients,
  and those commissions are almost entirely undocumented.
- **Index insurance.** Pula works with African Risk Capacity and with regional
  insurers and reinsurers, and ARC has paid out to the governments of Senegal,
  Niger, Mauritania, Malawi and Cote d'Ivoire. Premiums are bundled with input
  credit or subsidised, so the party that ultimately pays for the yield and
  weather data is usually a government or a donor.
- **Consumer goods panels.** Kantar runs panels in 16 African countries against
  two in the Middle East. Measurement is harder here because most grocery trade
  is informal and outside scanner coverage, so panels substitute for point of
  sale data and the product sold is thinner.

African digital advertising was about 3.8bn in 2025, forecast at 6.5bn by 2029.
Fifty-four countries generate less than half of MENA's digital advertising
spend, and that bounds how much commercial audience measurement the continent
can support regardless of how many firms enter.

### What is still missing

Operator data sales were searched for and not found. MTN's ADAM platform is
reported to process 4 trillion records a month and Safaricom's data revenue
overtook voice in the year to March 2026, but everything published describes
internal analytics and fintech rather than third party data sales. The row for
it is evidence C and says so. Mining and agribusiness purchases of earth
observation in Africa were also searched for and nothing usable was found, so
no row was written.

## 8. Deliberately excluded

- **Per-firm revenue and customer lists.** Not available for any firm in the
  register at a quality worth coding.
- **Gulf and North African government contract values.** Searched for, not
  found in published form. The absence is itself a finding about these states.
- **Telecom operator data deals.** Negotiated bilaterally with terms that are
  never published; the two telecom rows are evidence C for that reason.
- **Market sizing forecasts.** Several vendor and analyst reports project the
  alternative data or web scraping markets years forward. Forecasts are not
  observations and none is recorded as a price signal.
- **Advertising technology spend.** Large, adjacent, and about placement rather
  than about collection, so outside the register's boundary.

## 9. What would need to be true for this to be wrong

The entry-cohort result would be wrong if the register systematically
under-collected older firms in the segments that look new, which is plausible:
a defunct 1990s annotation firm leaves less trace than a defunct 1990s polling
house. That would inflate the recent share of AI training data and web data.
The countervailing error runs the other way in field agencies, where firms
founded in the last five years in Africa are the hardest of all to find.

The buyer-side result would be wrong if commercial purchasing were documented
as well as public procurement is and simply had not been searched for. That is
not the case here; the search was run across both and the asymmetry in what came
back is stated in section 2 rather than being presented as a finding about
the state's role.
