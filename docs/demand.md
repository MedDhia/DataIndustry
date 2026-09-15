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

`data/demand.csv` holds 65 rows across all 23 segments and 15 buyer categories.
The largest categories by row count are corporate marketing (9), financial
investors (7), civil government (7), corporate operations (6) and state security
agencies (6).

State and donor buyers are 18 of 65 rows. They are 8 of the 12 rows that reach
evidence level A. That asymmetry is a fact about the record, not about the
industry: a government purchase leaves an award notice, a contract value and
sometimes a court case, while a corporate subscription leaves nothing at all.
Any account of who buys data that relies on public documents will over-count
the state. The demand layer records this in `output/tab37_evidence_visibility.txt`,
where 9 of 12 A rows are public awards and 26 of 33 B rows are trade reporting.

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

## 6. MENA and Africa: the demand side is thin and mostly not commercial

ESOMAR puts the Middle East and Africa together at about 3 percent of global
insights activity, roughly 4.4bn in 2022, the smallest region. Growth was second
highest in the world in nominal terms at 9.2 percent and negative at -1.2
percent once inflation is removed. A region can look like it is growing and be
shrinking in what its buyers actually purchase.

The register's own African and MENA for-profit firms sit overwhelmingly in the
two segments whose documented buyers are donors, states and foreign research
agencies. The commercial buyer that exists elsewhere, a domestic corporate
marketing department with a research budget, is the thinnest part of the
evidence here.

This is also where the demand file is weakest. Four rows carry MENA as their
geography and two of them are evidence C. Gulf procurement values are not
published, so the claim that ministries and sovereign funds are the dominant
buyers of data systems in the GCC rests on commentary and not on award records.
It is coded C and flagged, and it should not be cited as though it were measured.

## 7. Deliberately excluded

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

## 8. What would need to be true for this to be wrong

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
