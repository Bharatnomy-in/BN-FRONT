# Coastal districts and their population, 2011 — Maharashtra

Which districts (2011 boundaries) touch the sea coast, how much coastline each has, and their Census 2011 population, with state and All India totals for coastal districts. Computed by Bharatnomy from map data and the Census.

## Coverage

- **Rows:** 35
- **Period:** 2011
- **Districts:** 35 of 36
- 1 state-total row(s) from the warehouse table are left out; add up district rows instead.

## Source

- **Coastline:** Natural Earth 1:10m coastline (public domain), file version 5.0.0-pre9, https://www.naturalearthdata.com/downloads/10m-physical-vectors/10m-coastline/ (file in [`_sources/natural-earth/raw/`](https://github.com/sarveshkant2003-afk/bharatnomy-data/tree/cd7ce2d673103cc0e606e3cc37e49a9ae75f849a/_sources/natural-earth/raw/))
- **District boundaries:** Census 2011 district map from DataMeet (see [`_sources/datameet-maps/`](https://github.com/sarveshkant2003-afk/bharatnomy-data/tree/cd7ce2d673103cc0e606e3cc37e49a9ae75f849a/_sources/datameet-maps/))
- **Population:** ORGI Census 2011 Primary Census Abstract, from [`POP_census-pca_2011_STATES_ORGI_DIST`](https://github.com/sarveshkant2003-afk/bharatnomy-data/tree/cd7ce2d673103cc0e606e3cc37e49a9ae75f849a/POP_census-pca_2011_STATES_ORGI_DIST/)
- **Downloaded:** 12 Nov 2026
- **Script:** [`pipelines/natural-earth/build_coastal_districts.py`](https://github.com/sarveshkant2003-afk/bharatnomy-data/tree/cd7ce2d673103cc0e606e3cc37e49a9ae75f849a/pipelines/natural-earth/build_coastal_districts.py)

## How it is computed

- A district is **coastal** if its 2011 boundary comes within 0.01 degree (about 1 km) of the Natural Earth coastline. The tolerance absorbs small mismatches between the two maps.
- **Coastline length** = length of the coastline lying within that 1 km band around the district, km (approximate).

## Columns

| Column | Type | Unit | Description |
|---|---|---|---|
| `state_ut` | text |  | Place (2011 boundary; names as in the Census PCA dataset) |
| `lgd_state_code` | text |  | Place (2011 boundary; names as in the Census PCA dataset) |
| `district` | text |  | Place (2011 boundary; names as in the Census PCA dataset) |
| `lgd_district_code` | text |  | Place (2011 boundary; names as in the Census PCA dataset) |
| `district_census_code` | text |  | Place (2011 boundary; names as in the Census PCA dataset) |
| `is_coastal` | text |  | `yes` / `no` |
| `coastline_within_1km_km` | number | km | Coastline length along the district, km (0 for inland districts) |
| `year` | text |  | `2011` (Census) |
| `population_persons` | integer |  | Census 2011 population and households of the district |
| `population_males` | integer |  | Census 2011 population and households of the district |
| `population_females` | integer |  | Census 2011 population and households of the district |
| `households` | integer |  | Census 2011 population and households of the district |

Units are read from the column name (warehouse convention). Empty cells (`null` in JSON) mean no value.

## Notes from the warehouse

These describe the full warehouse table (all states).

- **Our calculation, not an official list.** Natural Earth draws the coast into estuaries and lagoons, so some districts on river mouths or backwaters count as coastal (e.g. Haora on the Hooghly, Kottayam on Vembanad Lake, Vadodara and Cuttack on estuaries), and map mismatches can add an inland district (Virudhunagar, Tamil Nadu, gets 64 km, which looks wrong). Check the borderline cases, or use `coastline_within_1km_km` to keep only districts with a substantial coast.
- Yanam (Puducherry), on the Godavari delta, is about 4 km from the Natural Earth coast and is not counted.
- 2011 boundaries: e.g. Palghar is inside Thane; Morbi and Devbhumi Dwarka are inside Rajkot and Jamnagar.
- Checks (12 Nov 2026): 640 districts, 79 coastal in 13 states/UTs; coastal-district population 218,195,291 (18% of the 2011 population); populations equal the PCA values.

## Where this comes from

- Warehouse folder [`POP_coastal-districts_2011_STATES_BNY_DIST`](https://github.com/sarveshkant2003-afk/bharatnomy-data/tree/cd7ce2d673103cc0e606e3cc37e49a9ae75f849a/POP_coastal-districts_2011_STATES_BNY_DIST) at commit `cd7ce2d67310`
- Filtered to `lgd_state_code` and cleaned by `build.py` in this repo. Files: `POP_coastal-districts_2011_MH_BNY_DIST.csv`, `POP_coastal-districts_2011_MH_BNY_DIST.json`.
