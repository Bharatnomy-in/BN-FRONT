# Disabled population by type of disability, age and sex, states and districts, 2011 — Maharashtra

Number of people with a disability, by type (seeing, hearing, speech, movement, mental retardation, mental illness, any other, multiple), age group and sex, for total, rural and urban areas of every district, state and India, from Census 2011.

## Coverage

- **Rows:** 1,365
- **Period:** 2011
- **Districts:** 35 of 36
- 39 state-total row(s) from the warehouse table are left out; add up district rows instead.

## Source

- **Data:** Office of the Registrar General & Census Commissioner, India (ORGI), Census of India 2011, Table C-20 "Disabled population by type of disability, age and sex"
- **Link:** https://censusindia.gov.in/nada/index.php/catalog (one file per state/UT plus India; catalog ids in [`_sources/orgi-census2011/raw/orgi-census2011_c20-catalog-ids_2011.tsv`](https://github.com/sarveshkant2003-afk/bharatnomy-data/tree/41650b8bb1975a4f4e082ba172d8b5dfb8f7db8a/_sources/orgi-census2011/raw/orgi-census2011_c20-catalog-ids_2011.tsv))
- **Downloaded:** 12 Nov 2026 (originals in [`_sources/orgi-census2011/raw/c20/`](https://github.com/sarveshkant2003-afk/bharatnomy-data/tree/41650b8bb1975a4f4e082ba172d8b5dfb8f7db8a/_sources/orgi-census2011/raw/c20/))
- **Scripts:** [`pipelines/orgi-census2011/fetch_c20.sh`](https://github.com/sarveshkant2003-afk/bharatnomy-data/tree/41650b8bb1975a4f4e082ba172d8b5dfb8f7db8a/pipelines/orgi-census2011/fetch_c20.sh), [`pipelines/orgi-census2011/build_c20.py`](https://github.com/sarveshkant2003-afk/bharatnomy-data/tree/41650b8bb1975a4f4e082ba172d8b5dfb8f7db8a/pipelines/orgi-census2011/build_c20.py)

## Columns

| Column | Type | Unit | Description |
|---|---|---|---|
| `state_ut` | text |  | State or UT as in 2011 (`Dadra & Nagar Haveli` and `Daman & Diu` separately); `All India` |
| `lgd_state_code` | text |  | State/UT code in the Local Government Directory (LGD), from [`_reference/geography.csv`](https://github.com/sarveshkant2003-afk/bharatnomy-data/tree/41650b8bb1975a4f4e082ba172d8b5dfb8f7db8a/_reference/geography.csv); blank for All India and the two pre-2020 UTs |
| `state_census_code` | text |  | Census 2011 state code (`00` = India) |
| `district` | text |  | District (today's name from [`_reference/geography.csv`](https://github.com/sarveshkant2003-afk/bharatnomy-data/tree/41650b8bb1975a4f4e082ba172d8b5dfb8f7db8a/_reference/geography.csv), 2011 boundary); `State total`; `All India` |
| `lgd_district_code` | text |  | District code in the LGD; blank for totals and for Mahe and Yanam |
| `district_census_code` | text |  | Census 2011 district code; blank for state and India rows |
| `census2011_name` | text |  | Area name as printed in the table |
| `area` | text |  | `total`, `rural` or `urban` |
| `age_group` | text |  | `Total`, `0-4`, `5-9`, `10-19`, then 10-year groups to `80-89`, `90+`, `Age Not Stated` |
| `disabled_total_persons` | integer |  | All disabled persons |
| `disabled_total_males` | integer |  | All disabled persons |
| `disabled_total_females` | integer |  | All disabled persons |
| `disabled_seeing_persons` | integer |  | Disabled in seeing, hearing, speech, movement |
| `disabled_seeing_males` | integer |  | All disabled persons |
| `disabled_seeing_females` | integer |  | All disabled persons |
| `disabled_hearing_persons` | integer |  | Disabled in seeing, hearing, speech, movement |
| `disabled_hearing_males` | integer |  | All disabled persons |
| `disabled_hearing_females` | integer |  | All disabled persons |
| `disabled_speech_persons` | integer |  | Disabled in seeing, hearing, speech, movement |
| `disabled_speech_males` | integer |  | All disabled persons |
| `disabled_speech_females` | integer |  | All disabled persons |
| `disabled_movement_persons` | integer |  | Disabled in seeing, hearing, speech, movement |
| `disabled_movement_males` | integer |  | All disabled persons |
| `disabled_movement_females` | integer |  | All disabled persons |
| `disabled_mental_retardation_persons` | integer |  | Mental retardation, mental illness (Census 2011 terms) |
| `disabled_mental_retardation_males` | integer |  | All disabled persons |
| `disabled_mental_retardation_females` | integer |  | All disabled persons |
| `disabled_mental_illness_persons` | integer |  | Mental retardation, mental illness (Census 2011 terms) |
| `disabled_mental_illness_males` | integer |  | All disabled persons |
| `disabled_mental_illness_females` | integer |  | All disabled persons |
| `disabled_any_other_persons` | integer |  | Any other disability; multiple disability |
| `disabled_any_other_males` | integer |  | All disabled persons |
| `disabled_any_other_females` | integer |  | All disabled persons |
| `disabled_multiple_persons` | integer |  | Any other disability; multiple disability |
| `disabled_multiple_males` | integer |  | All disabled persons |
| `disabled_multiple_females` | integer |  | All disabled persons |

Units are read from the column name (warehouse convention). Empty cells (`null` in JSON) mean no value.

## Notes from the warehouse

These describe the full warehouse table (all states).

- Counts of persons. For a share of the population, divide by `population_persons` in [`POP_census-pca_2011_STATES_ORGI_DIST`](https://github.com/sarveshkant2003-afk/bharatnomy-data/tree/41650b8bb1975a4f4e082ba172d8b5dfb8f7db8a/POP_census-pca_2011_STATES_ORGI_DIST/) (same Census codes).
- District names are today's (LGD) for the 2011 district; `census2011_name` keeps the 2011 spelling. Districts created after 2011 (e.g. Palghar) are inside their 2011 parent.
- The C-20 tables for Scheduled Castes, Scheduled Tribes and million-plus cities are separate catalog entries and are not taken yet.
- Checks (12 Nov 2026): 26,364 rows = 676 places (India, 35 states/UTs, 640 districts) x 3 areas x 13 age groups; no duplicate keys or negatives; persons = males + females; the eight types add up to the total; age groups add up to Total; rural + urban = total; districts add up to their state; the India file's state rows equal the state files' (1,365 rows, no difference); the states add up to All India, 26,814,994.

## Where this comes from

- Warehouse folder [`POP_disabled-population_2011_STATES_ORGI_DIST`](https://github.com/sarveshkant2003-afk/bharatnomy-data/tree/41650b8bb1975a4f4e082ba172d8b5dfb8f7db8a/POP_disabled-population_2011_STATES_ORGI_DIST) at commit `41650b8bb197`
- Filtered to `lgd_state_code` and cleaned by `build.py` in this repo. Files: `POP_disabled-population_2011_MH_ORGI_DIST.csv`, `POP_disabled-population_2011_MH_ORGI_DIST.json`.
