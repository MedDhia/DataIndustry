# The gaps that survive testing

The register exists to find gaps in the data collection industry. Most of what
looked like a gap was not one: 135 of 138 empty region-by-segment cells were
artefacts of reading headquarters as presence, and 141 of 297 empty
country-by-domain cells were manufactured by a feasibility rule the register's own
fieldwork refutes. Both are documented in section 22 of `docs/coverage_gaps.md`
and in `data/gap_tests.csv`.

What follows is what is left. `scripts/13_real_gaps.py` recomputes all of it, and
the ranking is by one criterion: **would finding more organisations close this?**

---

## 1. The terms of access. Robust to enumeration.

**1,056 of 5,082 country-domain cells have a provider and not one a researcher can
obtain record-level data from.** 21 percent of everything this register knows is
collected is collected on terms that put it out of reach.

| Domain | Cells closed |
|---|---|
| Credit risk | 178 of 178 |
| Financial transactions | 162 of 173 |
| Biometric and identity | 160 of 191 |
| Biodiversity | 77 of 194 |
| Retail prices | 72 of 193 |
| Migration and displacement | 70 of 192 |

**Credit risk is closed everywhere on earth.** Not one organisation in the
register, in any country, makes record-level credit data available to an outside
researcher. That claim was taken to its strongest counterexample and survived:
the Equifax and New York Fed Consumer Credit Panel, the most cited research
dataset of its kind, is restricted by contract to Federal Reserve System
researchers and their coauthors. Everyone else gets aggregates.

Transaction data came within one row of the same status. Testing it found that
Dewey Data resells Consumer Edge card panels to universities, so Consumer Edge is
now coded `researcher_restricted` with route `via_network`. Access exists by
buying it through a reseller. It does not exist from the collector.

This is the gap that enumeration cannot close. New firms arrive on the same
terms, so adding them adds closed cells at the observed rate.

---

## 2. Domestic capacity. Bounded by enumeration, tested in the hardest cases.

**88 of 194 countries have substantial coverage and no organisation based there
providing any of it.** By region: Latin America 27, Eastern Europe 16, Oceania
13, Southeast Asia and Sub-Saharan Africa 7 each, South Asia 5.

The extreme cases are stark. Eritrea has 43 organisations covering it and none
Eritrean. Turkmenistan 48 and none Turkmen. Kiribati 44, Moldova 47, Haiti 54,
Belize 56, each with none.

Four of these were taken to a search, and the searches came back with the same
answer every time. Eritrea's 2025 Population and Health Survey reached 9,794
households across 405 enumeration areas, run by the national statistics office
with UNDP. Guinea-Bissau's MICS was run by its statistics institute with UNICEF,
UNFPA, WFP and the EU. The Central African Republic is monitored by FAO telephone
surveys. Turkmenistan is covered by TGM Research of Singapore, AQR Fieldwork and
2insights, all foreign.

**In the countries with no domestic capacity, the collectors are the state, the
international organisations, and foreign firms.** Nobody independent and local is
asking anything. For a reader interested in who can know a place without the
permission of the people who run it, that is the finding in this register.

It is bounded: more enumeration can only shrink the 88. That is why the four
searches are recorded in `gap_tests.csv` whether or not they found anything.

---

## 3. Absence. Bounded, and mostly already broken.

156 of 5,238 country-domain cells have no provider at all, down from 297 once the
feasibility rule was rebuilt on observation. They concentrate in Guinea-Bissau,
the Central African Republic, Eritrea, Turkmenistan, Liberia, Togo, Sierra Leone
and Mozambique, and in the domains of device telemetry, housing, transactions and
credit.

Every cell here should be read as untested unless `gap_tests.csv` says otherwise.
The three that were tested all fell.

---

## 4. Single-provider dependency. Fragile evidence.

340 country-domain cells rest on one organisation, and five organisations account
for most of them: riskthinking.ai in 87, NuView in 76, HERE Technologies in 21,
BlueDot in 17, Moody's BvD in 14.

Coverage rows are 92 percent modelled at a measured precision near 0.49, so a
count of one is a hypothesis about concentration and not a fact about a country.
It is reported because concentration is the kind of gap that matters and because
the shape of it is consistent: the single providers are all firms selling one
global product, so the dependency is on a product line rather than on a market.

---

## What was rebuilt to get here

**The feasibility gate.** It had said that transaction and credit data are
impossible below upper-middle income and that telemetry and location are
impossible below medium connectivity. 35 hand-coded rows and 15 organisations
contradicted it: Indicina scores credit in Uganda, Orange Flux Vision reads
mobility in Mali and Niger, Hello Tractor telemeters tractors in Burkina Faso,
Kifiya does both in Ethiopia. The rule was manufacturing 224 impossible cells in
exactly the poorest countries, and those cells then read as gaps in the industry.

The gate is now derived from what hand-coded footprints actually show, and
observed rows are never filtered by it at all. An observation beats a rule.
