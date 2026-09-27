# Type of data demanded, not supplied

`docs/market_gaps.md` asks which segments and places are thinly served. This
asks what *kind* of data buyers ask for and nobody produces, holding the segment
fixed. It is the stronger claim of the two, because it survives the objection
that somebody already sells in the segment: they sell a different type.

A type here is the combination of four coded properties of what an organisation
produces: the unit one row describes, how often that row is refreshed, how far
the same instrument reaches, and whether anyone outside the buyer can see a
record. `scripts/15_data_type_gaps.py` recomputes every table.

**Limits.** The register codes one unit, one frequency and one scope per
organisation, so a producer of two types is represented by its main one and
every count is a lower bound. Nothing codes how far back a series runs, so this
says nothing about historical depth. No revenue variable exists, so nothing here
is a market size.

---

## 1. The unit mismatch: buyers ask about an asset, suppliers describe an area

The demand file records what unit the buyer names. Underwriters buy "asset level
physical risk". Disclosure rules under ISSB and CSRD ask a company about itself.
The EU due diligence and forced labour rules ask about a worker. The supply base
answers at a coarser unit.

| Domain | Firms | At the unit demanded | At area level |
|---|---|---|---|
| Climate and environment | 100 | 11 (firm, building, site) | 70 |
| Supply chain | 35 | **2** (worker, household) | 13 at vehicle level |
| Agriculture | 79 | 6 (farm as firm or site) | 47 |
| Infrastructure | 52 | 2 (user, household) | 30 |
| Energy and extractives | 23 | 5 | 9 |
| Biodiversity | 9 | 1 | 8 |

Climate is the clearest. Zero of the 100 climate organisations treat a company
as the unit of observation, while the whole of ISSB and CSRD reporting is a
company describing itself. The eleven that work at asset level are six American,
two Israeli, and three African community mapping projects, of which Zenvus in
Nigeria is the only African commercial one.

Supply chain is the sharpest. Regulation now asks importers to evidence
conditions for the people in their chain, and two organisations in the register
observe a person in a supply chain context: Teralytics in Switzerland, which
infers movement from telecom signalling, and Aydi in Egypt. Thirteen observe a
vehicle. The market currently answers a question about workers with data about
containers.

Most of the 139 empty cells in the full domain by unit matrix are not markets.
These six are, because a demand row names the unit.

---

## 2. The frequency mismatch: fast data is about machines, slow data is about people

| Unit of one row | Firms | Weekly or faster | Real time |
|---|---|---|---|
| Vehicle | 25 | 100% | 23 |
| Transaction | 32 | 100% | 9 |
| Device | 30 | 90% | 9 |
| Document | 76 | 71% | 14 |
| Area | 106 | 70% | 13 |
| Patient | 30 | 50% | 2 |
| Firm | 29 | 41% | 1 |
| Individual | 430 | 31% | 16 |
| Household | 62 | **31%** | **0** |

No organisation anywhere in the register observes a household in real time. By
domain, the slowest supply sits under some of the most time-sensitive decisions:

| Domain | Firms | Weekly or faster |
|---|---|---|
| Labour and employment | 109 | 10% |
| Education | 57 | 12% |
| Housing and property | 31 | 19% |
| Public opinion | 309 | 21% |
| Migration and displacement | 36 | 31% |

Labour is the one to look at. Ministries set wages, donors target programmes and
central banks read slack on a quarterly cycle because that is what exists; the
eleven organisations producing labour data weekly or faster are mostly American
survey platforms and AI hiring marketplaces measuring their own users, not a
labour market. Displacement moves in days and 25 of 36 suppliers work slower
than a week.

Where fast people-data does exist, it comes from one instrument: telecom
network signalling. Positium, Teralytics, Orange Flux Vision and Flowminder
produce daily population movement, and that method has no MENA-based and no
African commercial user at all, which is the same finding
`docs/market_gaps.md` section 2 reaches from the method side.

---

## 3. The terms mismatch: which types are readable at all

Share of each unit's suppliers offering any route, commercial or academic, to a
record instead of an aggregate only.

| Unit of one row | Accessible | Firms | Share |
|---|---|---|---|
| Patient | 21 | 30 | 70% |
| Household | 33 | 62 | 53% |
| Document | 30 | 76 | 39% |
| Individual | 116 | 430 | 27% |
| Area | 27 | 106 | 25% |
| Firm | 4 | 29 | 14% |
| Vehicle | 3 | 25 | 12% |
| Device | 2 | 30 | 7% |
| Transaction | 1 | 32 | **3%** |

The ordering is not about sensitivity. Patient records are the most regulated
data in the file and the most readable, because health research built the
consent and access machinery to make them so. Transaction and device data are
less regulated and almost entirely closed, because nobody built that machinery
for them. One organisation of 32 producing transaction-level data offers any
outside route to a record, and across all 38 credit risk organisations worldwide
the count is zero.

That is a type gap with a named beneficiary. African lenders score thin-file
borrowers on mobile money history, airtime purchase and utility payments, which
is transaction data about individuals, and Sub-Saharan Africa holds 13 of the
world's 38 credit risk producers. None of them, and none of their competitors
anywhere, lets a borrower, a regulator or a researcher see a record. An entrant
building transaction-level scoring with an audit route attached would be the
first, in the region that already produces the most of this data type.

---

## 4. The linkage gap: types that exist only as two separate files

153 of the 351 possible domain pairs are held by no single organisation. Most of
those pairs are meaningless. Six are products that buyers already need and
nobody sells, because selling them means joining two files that no one owns at
once.

| The join nobody makes | Firms on each side | Who needs it |
|---|---|---|
| Labour x supply chain | 109, 35 | Importers under the EU due diligence and forced labour rules |
| Climate x firmographic | 100, 64 | Every company filing under ISSB or CSRD |
| Health x supply chain | 142, 35 | Falsified medicine and cold chain oversight |
| Displacement x retail prices | 36, 61 | Famine and displacement early warning |
| Credit risk x mobility | 38, 45 | Thin-file lending where movement is the only signal |
| Agriculture x firmographic | 79, 64 | Agricultural lending to the farm as a business |

Credit risk is the loneliest domain of any size in the register: 38
organisations, linked to 11 of 26 possible partner domains, and to none of
mobility, prices, media, health, education, migration, web content or public
opinion. A credit file in this industry is a closed object that touches nothing
else, which is precisely the opposite of how thin-file scoring is supposed to
work.

---

## 5. The border mismatch: the phenomenon crosses borders, the instrument does not

Share of each domain's suppliers operating in a single country.

| Domain | Firms | Single country | Global |
|---|---|---|---|
| Public opinion | 309 | 64% | 25 |
| Labour and employment | 109 | 63% | 16 |
| Media and audience | 77 | 44% | 17 |
| Health clinical | 142 | 43% | 26 |
| Credit risk | 38 | 37% | 5 |
| Migration and displacement | 36 | 36% | **2** |

Satellite and sensor domains run the other way: 6% of earth observation and
agriculture suppliers, and 6% of supply chain suppliers, are single-country. The
split is instrumental. An orbit does not stop at a border and a field team does.

Migration is the contradiction worth naming. Displacement is definitionally a
cross-border phenomenon and two of its 36 suppliers work globally, with 13
confined to one country. Anyone wanting a comparable measurement of the same
person's movement across a border is assembling it from national pieces that
were not built to join, which is a reason the corridor data everyone cites is
modelled instead of observed.

---

## 6. Types already supplied, so not an opening

Listed so the analysis above can be falsified by its own file.

| Type | Firms | Accessible | MENA | SSA |
|---|---|---|---|---|
| Patient level clinical records | 30 | 21 | 2 | 5 |
| Vessel and vehicle positioning | 25 | 3 | 2 | 3 |
| Document level labelled text | 24 | 9 | 8 | 10 |
| Transaction level credit history | 38 | 0 | 5 | 13 |

Two of these deserve saying out loud. Document-level labelled text is the one
data type where MENA and Africa lead the world outright, 18 of 24 producers, and
it is the type the sovereign Arabic model programmes are buying. And
patient-level records are proof that the terms problem in row 3 is solvable: the
most sensitive type in the register is also its most readable, because one field
built the consent infrastructure to make it so and the others did not.
