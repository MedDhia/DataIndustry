# Entering a crowded segment with a method nobody else had

This is the register's method layer: `data/method_innovations.csv`, 63 firms
whose entry rested on a collection method their segment did not already have,
each with the method named, the practice it displaced, the year the firm first
deployed it, and whether the method has since drawn litigation, regulatory
action or documented accuracy disputes.

Twenty-eight of the firms were added to the register in this round. The other
thirty-five were already in it; the layer was built across both so that the
question below has a population to be asked of rather than a hand-picked list.

## 1. How crowded was it, actually

For each firm, count the organisations already in its segment when it first
deployed the method. Exited firms count, because they were competitors at the
time even if they are gone now.

Median prior occupants: **20**. Range 1 to 80. **35 of 63 entered a segment that
already held 20 or more organisations**, and only 6 entered one holding fewer
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
| `new_sensor` | 19 | A physical sensing method the segment did not have: radar from a smallsat, thermal from orbit, acoustics on fibre, environmental DNA, wastewater, wifi propagation |
| `new_substrate` | 19 | Data made from a source nobody treated as data: retail listings as inflation, parking lots as revenue, platform video as evidence, satellite pixels as household wealth |
| `new_sampling_frame` | 12 | A different way of reaching the same population: abandoned domains, the television set, app SDKs, other people's dashcams |
| `new_inference` | 5 | Ordinary collection, a new quantity extracted: appliance use from one meter signal, health state from a few seconds of speech |
| `new_incentive` | 4 | Contributors paid in a way the segment did not pay them: tokens for hosting a base station, a receiver, a weather station, a car |
| `new_contract` | 4 | The terms of the work are the innovation: royalties on resale, local retention of the corpus |

The last two are not technical at all, and they are where the register's
non-Western entries concentrate. Of the four `new_contract` rows, three are
headquartered outside North America and Western Europe: Karya in India, Digital
Umuganda in Rwanda, Lelapa AI in South Africa. The fourth is Sama, a US-headquartered
firm whose annotation workforce is Kenyan, and it is the one coded contested.

That is the sharper version of a point the demand layer already made. Of 63
methodological innovations here, 51 are in North America or Western Europe.
The contribution from elsewhere is not a new instrument. It is a claim about who
owns the data and how the person who produced it gets paid.

## 3. What draws a legal challenge is not the sensor

16 of the 63 methods are coded contested, meaning the method itself has drawn
litigation, regulatory action, or sustained documented accuracy disputes. The
rate by type:

| Type | Contested |
|---|---|
| `new_substrate` | 8 of 19 |
| `new_sampling_frame` | 4 of 12 |
| `new_contract` | 1 of 4 |
| `new_inference` | 1 of 5 |
| `new_sensor` | 2 of 19 |
| `new_incentive` | 0 of 4 |

Building a new instrument and pointing it at the world is almost never
challenged: 2 of 19, and both of those are radio frequency geolocation and
gunshot acoustics, where the dispute is about evidentiary use rather than about
collection. What gets challenged is taking material that already exists and
turning it into data about people who never agreed to it: bank credentials
(Yodlee), card transactions (Second Measure), residential connections (Bright
Data), the television set (Alphonso, Samba TV), app store telemetry (Sensor
Tower), a listed company's parking lot (RS Metrics).

The pattern holds in the other direction too. The four token-incentive networks
are the only category with no contested row in it, and the thing that
distinguishes them is that the contributor is asked, paid, and can stop.

## 4. Innovators are bought

9 of the 63 are no longer independent, 14.3%, against 8.7% across the register
as a whole. Five were absorbed outright and four continue under an owner:

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
**9 of 49 innovators release record-level data to researchers, 18.4%, against
48 of 383 for everyone else, 12.5%**.

Including the nonprofits in the innovation layer produces 31.0%, which would be
a trick: Airwars, Mnemonic, Wildlife Insights, WastewaterSCAN and Rainforest
Connection publish by constitution and would carry the entire difference on
their own. The for-profit-only figure is the one to use, and a six point gap on
those denominators is a hint, not a result.

## 6. What this round added to the taxonomy

Three modality codes were added to `data/modalities.csv`, taking it from 19 to
22, because three methods in this round had no honest home in the existing list:

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

## 7. What was deliberately left out

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
- **Founding years that could not be established.** OptaSense and Tutela carry
  `NA` rather than a plausible guess, which costs them their place in every
  cohort table and is the right price.
