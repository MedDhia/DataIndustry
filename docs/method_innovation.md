# Entering a crowded segment with a method nobody else had

This is the register's method layer: `data/method_innovations.csv`, 69 firms
whose entry rested on a collection method their segment did not already have,
each with the method named, the practice it displaced, the year the firm first
deployed it, and whether the method has since drawn litigation, regulatory
action or documented accuracy disputes.

It was built over two rounds: a first pass that added 28 organisations to the
register and coded 35 that were already in it, and a MENA and Africa round that
added 15 more and coded 6 of them here. The layer spans firms added in both
rounds and firms that predate them, so the question below has a population to be
asked of rather than a hand-picked list.

## 1. How crowded was it, actually

For each firm, count the organisations already in its segment when it first
deployed the method. Exited firms count, because they were competitors at the
time even if they are gone now.

Median prior occupants: **20**. Range 1 to 81. **40 of 69 entered a segment that
already held 20 or more organisations**, and only 7 entered one holding fewer
than five.

The most crowded entries in the file:

| Firm | Segment | Novelty | First deployed | Prior occupants |
|---|---|---|---|---|
| RIWI | Full-service survey | new sampling frame | 2011 | 80 |
| Amini | Earth observation | new substrate | 2023 | 79 |
| Satellite Vu | Earth observation | new sensor | 2023 | 79 |
| Pixxel | Earth observation | new sensor | 2022 | 77 |
| Orbital Sidekick | Earth observation | new sensor | 2021 | 73 |
| Unseenlabs | Earth observation | new sensor | 2019 | 67 |
| ATLAN Space | Earth observation | new substrate | 2018 | 60 |
| Atlas AI | Earth observation | new substrate | 2018 | 60 |
| HawkEye 360 | Earth observation | new sensor | 2018 | 60 |
| ICEYE | Earth observation | new sensor | 2018 | 60 |
| Lelapa AI | AI training data | new contract | 2022 | 50 |

Read that count carefully. It is a property of this register's enumeration as
much as of the industry: earth observation and survey work are enumerated deeply
here, wifi sensing and digital olfaction are not. A count of 60 means a segment
this file knows well. The number compares innovators against each other within a
segment far better than across segments, and every table in
`scripts/10_innovation.R` prints the segment for that reason.

What survives the caveat is the shape. Nobody in this file found an empty
market. The two segments that attracted the most methodologically distinct
entrants, earth observation and health real-world data, are the two the register
already showed as most crowded.

## 2. Six kinds of new, and they are not equally new

| Type | n | What it means |
|---|---|---|
| `new_sensor` | 21 | A physical sensing method the segment did not have: radar from a smallsat, thermal from orbit, acoustics on fibre, environmental DNA, wastewater, wifi propagation, a sewer network, a beehive |
| `new_substrate` | 21 | Data made from a source nobody treated as data: retail listings as inflation, parking lots as revenue, platform video as evidence, satellite pixels as household wealth, the contents of a phone |
| `new_sampling_frame` | 13 | A different way of reaching the same population: abandoned domains, the television set, app SDKs, other people's dashcams, unpaid citizen reports |
| `new_contract` | 5 | The terms of the work are the innovation: royalties on resale, local retention of the corpus, open publication instead of licensing |
| `new_inference` | 5 | Ordinary collection, a new quantity extracted: appliance use from one meter signal, health state from a few seconds of speech |
| `new_incentive` | 4 | Contributors paid in a way the segment did not pay them: tokens for hosting a base station, a receiver, a weather station, a car |

`new_contract` and `new_incentive` are not technical at all, and the first is
where the register's non-Western entries concentrate. Of the five `new_contract`
rows, four are headquartered outside North America and Western Europe and three
of those are African: Karya in India, Digital Umuganda in Rwanda, Lelapa AI and
Sunbird AI in South Africa and Uganda. The fifth is Sama, a US-headquartered firm
whose annotation workforce is Kenyan, and it is the one of the five coded
contested.

That is the sharper version of a point the demand layer already made. Of 69
methodological innovations here, 51 are in North America or Western Europe.
The contribution from elsewhere is not a new instrument. It is a claim about who
owns the data and how the person who produced it gets paid.

## 3. What draws a legal challenge is not the sensor

18 of the 69 methods are coded contested, meaning the method itself has drawn
litigation, regulatory action, or sustained documented accuracy disputes. The
rate by type:

| Type | Contested |
|---|---|
| `new_substrate` | 10 of 21 |
| `new_sampling_frame` | 4 of 13 |
| `new_contract` | 1 of 5 |
| `new_inference` | 1 of 5 |
| `new_sensor` | 2 of 21 |
| `new_incentive` | 0 of 4 |

Building a new instrument and pointing it at the world is almost never
challenged: 2 of 21, and both of those are radio frequency geolocation and
gunshot acoustics, where the dispute is about evidentiary use rather than about
collection. What gets challenged is taking material that already exists and
turning it into data about people who never agreed to it: bank credentials
(Yodlee), card transactions (Second Measure), residential connections (Bright
Data), the television set (Alphonso, Samba TV), app store telemetry (Sensor
Tower), a listed company's parking lot (RS Metrics), and, at the far end of the
same logic, the contents of the phone in someone's pocket (Cellebrite, NSO Group).

The pattern holds in the other direction too. The four token-incentive networks
are the only category with no contested row in it, and the thing that
distinguishes them is that the contributor is asked, paid, and can stop.

## 4. Innovators are bought

9 of the 69 are no longer independent, 13.0%, against 9.4% across the register
as a whole. The direction reverses on the narrower measure: **7.2% of innovators
have ceased entirely against 8.8% register-wide.** They are bought more often
and they die slightly less often. Five were absorbed outright and four continue
under an owner:

| Firm | Outcome | Acquirer |
|---|---|---|
| Silixa | absorbed | Luna Innovations |
| OptaSense | absorbed | Luna Innovations |
| CARMERA | absorbed | Woven by Toyota |
| Orbital Insight | absorbed | Privateer |
| Second Measure | absorbed | Bloomberg |
| Alphonso | acquired, operating | LG Electronics |
| Opensignal | acquired, operating | Comlinkdata |
| PriceStats | acquired, operating | State Street |
| Yodlee | acquired, operating | STG |

Two things in that list are worth naming. Luna Innovations bought both fibre
sensing firms in the register, three years apart, which is a modality
consolidating into one owner. And four of the nine were bought by the buyer
rather than by a competitor: State Street, Bloomberg, LG and Toyota are the
demand side of their segments purchasing the method outright instead of
subscribing to it. The method survived in every case. The independent firm did
not.

## 5. Do they disclose more than the firms they displaced

Slightly, and the honest version of the comparison is much weaker than the
flattering one.

Among operating for-profit firms in the same segments as the innovators,
**9 of 53 innovators release record-level data to researchers, 17.0%, against
48 of 388 for everyone else, 12.4%**.

Including the nonprofits in the innovation layer produces 31.2%, which would be
a trick: Airwars, Mnemonic, Wildlife Insights, WastewaterSCAN, Rainforest
Connection, Ushahidi and Sunbird AI publish by constitution and would carry the
entire difference on their own. The for-profit-only figure is the one to use,
and a five point gap on those denominators is a hint, not a result.

## 6. What the first round added to the taxonomy

Three modality codes were added to `data/modalities.csv`, taking it from 19 to
22, because three methods in that round had no honest home in the existing list:

- `fiber_das`, distributed acoustic sensing along installed optical fibre, which
  turns cable laid for telecommunications into a continuous sensor array.
- `web_intercept`, instruments served to people who arrive at controlled web
  properties by accident, so the frame is a set of domains rather than a list of
  persons.
- `rf_sensing`, inference of presence and body state from how radio signals
  propagate through a room, which is distinct from `signals_rf`, the geolocation
  of emitters, and from `sensor_hardware`, which assumes something was installed.

Adding a code to a taxonomy is a substantive act and it is recorded here rather
than done quietly. The test applied was whether coding the firm with an existing
modality would have misdescribed what it does, not whether a new code would be
more flattering.

## 7. The MENA and Africa round, and what it cost the taxonomy

The first pass at this layer produced 12 innovations outside North America and
Western Europe out of 63. A round aimed at MENA and Africa alone added 15
organisations to the register and 6 to this layer, taking that to 18 of 69. What
it found is not a second Silicon Valley and does not resemble one.

### MENA now means Israel more than it used to

MENA holds 120 operating organisations in the register. The largest national
group is now Israel at 26, ahead of Turkiye at 15 and the UAE at 14. Ten of this
round's 15 additions are MENA and seven of those ten are Israeli, which is a
consequence of where firms of this kind exist and can be documented, not a
research choice made independently of that.

The register's MENA aggregate should therefore be read with the warning already
in `docs/demand.md` section 6: the region code mixes a country with a dense
venture-funded sensing industry, a country with the region's largest political
polling market, Gulf states that produce statistics in-house, conflict economies
where the buyer is the humanitarian system, and North African states that license
who may ask a question. Any MENA mean is a mean over those.

### Collection against the subject, which the vocabulary could not describe

Four of the additions sell collection from a person who has not agreed and is not
asked: Cellebrite, which acquires the contents of a seized handset, and NSO
Group, Candiru and Paragon Solutions, which take the contents of one in use by
remote compromise.

The register had no way to code them. `consent_model` offered explicit consent,
platform terms, a third-party contract, public record, or `not_applicable`, and
that last code means there is no human subject, which is a different claim
entirely. A new value, `no_consent_basis`, was added for collection that proceeds
without any consent from the subject and without a public-record or contractual
basis.

That gap is worth stating plainly rather than quietly patching. The vocabulary
was built by reading firms that all claimed a consent basis of some kind, so it
encoded the assumption that one always exists. It does not. The four firms now
carrying the new code are all headquartered in the region this register was built
to cover, and their product is used against people in it.

Two of the four are in the innovation layer and two are not. Cellebrite's
forensic acquisition (2007) and NSO's remote compromise (2012) are distinct
methods and both are coded. Candiru and Paragon arrived later with NSO's method
and are excluded by the same rule that excludes SeeTree for arriving after
Aerobotics with tree-level sensing. Following a method is not innovating.

### Two new modalities, and a gap on the other side

`device_extraction` covers acquisition of a device's contents whether by forensic
connection or by remote compromise. `citizen_report` covers reports submitted
voluntarily through SMS, web or messaging with no task assignment and no payment,
and Ushahidi is its case: built in under a week in January 2008 to map Kenyan
post-election violence, since deployed over 150,000 times.

Ushahidi sits at the opposite end of the same axis from the four firms above. In
both, the person is the source. In one the person decides to report and decides
what counts as reportable; in the other the person is never asked and cannot
refuse. A taxonomy that had neither code was missing both ends of its own range.

### What Africa added

Six organisations, and the pattern from the demand round repeats. Sunbird AI in
Kampala publishes its Luganda, Runyankole, Acholi, Lugbara and Ateso datasets
openly instead of licensing them, making it the third African entry in
`new_contract` and the only one in the whole layer that gives the data away.
Terragon in Lagos assembles mobile audience profiles across four African markets,
which puts an African firm in consumer brokerage, the segment consolidating
everywhere else in the register. Dataphyte extracts Nigerian budget and
procurement records that the state publishes in forms designed not to be read.
Zenvus sells soil sensing priced for a smallholder plot.

Of those, only Sunbird AI is in the innovation layer. The others are real
collectors doing established things in places where nobody was doing them, which
is worth recording in the register and is not a new method. Holding that line is
the only thing that keeps this layer meaning anything.

## 8. What was deliberately left out

- **Firms whose novelty is model architecture rather than collection.** A better
  classifier over the same images is not a new method by this file's standard.
- **Aryballe**, digital olfaction, and several similar sensor vendors. The
  register has no unit of observation that fits an odour sample, and forcing one
  would have been worse than the omission.
- **Fotech**, fibre sensing. The reported Viavi acquisition could not be
  confirmed and the BP relationship turned out to be an investment rather than
  an acquisition, so nothing was coded.
- **Tutela**, which is in `companies.csv` as an exit but not in this layer,
  because its method is the same as Opensignal's and the layer holds one row per
  firm, not one per deployment.
- **Founding years that could not be established.** OptaSense, Tutela and Bayanat
  carry `NA` rather than a plausible guess, which costs them their place in every
  cohort table and is the right price.
- **Followers of a method already in the layer.** SeeTree arrived two years after
  Aerobotics with tree-level sensing; Candiru and Paragon Solutions arrived after
  NSO with remote device compromise. All three are in `companies.csv` and none is
  in this layer. The rule is applied the same way to an Israeli spyware firm and
  to an Israeli agritech firm.
- **Real collectors doing established things in new places.** Lean Technologies
  brings account aggregation to the Gulf, Terragon brings consumer brokerage to
  West Africa, Zenvus brings soil sensing to smallholder plots, Dataphyte and SB
  Morgen do research with ordinary methods. Every one is in the register and none
  is a new method.
- **North African data collection firms.** Searched directly across Egypt,
  Tunisia, Algeria and Morocco. What came back was directory listings, AI
  consultancies and university projects rather than firms that collect. Nothing
  was coded on that basis, and the emptiness is consistent with what the demand
  layer found about commercial demand in the Maghreb.
