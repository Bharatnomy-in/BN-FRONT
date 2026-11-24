# Population by district from the GHSL grid, 1975 to 2030 (every 5 years) — Maharashtra

Resident population of every district every five years from 1975 (2025 and 2030 are JRC projections), from the EU Global Human Settlement Layer population grid, with population density. Computed by Bharatnomy. Unlike the Census (last one 2011), it gives a consistent district series up to 2020 and beyond, at the cost of being a model.

## Coverage

- **Rows:** 420
- **Period:** 1975 to 2030
- **Districts:** 35 of 36

## Source

- **Data:** European Commission, Joint Research Centre (JRC), GHSL Data Package 2023, GHS-POP R2023A: residential population, 30 arc-second grid (about 1 km), epochs 1975-2030. Census counts from the Census of India disaggregated to the grid using GHSL built-up surface, then fitted to UN World Population Prospects totals
- **Link:** https://ghsl.jrc.ec.europa.eu/ghs_pop2023.php (no login)
- **Citation:** Schiavina M., Freire S., Carioli A., MacManus K. (2023): GHS-POP R2023A - GHS population grid multitemporal (1975-2030). European Commission, Joint Research Centre (JRC)
- **Downloaded:** 18 Nov 2026 (grids not committed, about 4.2 GB; `pipelines/jrc-ghsl/fetch_ghsl_pop.sh` downloads them, see [`_sources/jrc-ghsl/`](https://github.com/sarveshkant2003-afk/bharatnomy-data/tree/41650b8bb1975a4f4e082ba172d8b5dfb8f7db8a/_sources/jrc-ghsl/))
- **District boundaries:** Census 2011 district map from DataMeet (see [`_sources/datameet-maps/`](https://github.com/sarveshkant2003-afk/bharatnomy-data/tree/41650b8bb1975a4f4e082ba172d8b5dfb8f7db8a/_sources/datameet-maps/))
- **Script:** [`pipelines/jrc-ghsl/build_district_population.py`](https://github.com/sarveshkant2003-afk/bharatnomy-data/tree/41650b8bb1975a4f4e082ba172d8b5dfb8f7db8a/pipelines/jrc-ghsl/build_district_population.py)

## How it is computed

- Each grid cell holds a number of residents. A cell belongs to the district that contains its centre (same assignment as [`ENV_built-up-surface_*`](https://github.com/sarveshkant2003-afk/bharatnomy-data/tree/41650b8bb1975a4f4e082ba172d8b5dfb8f7db8a/ENV_built-up-surface_1975-to-2030_STATES_BNY_DIST/)).
- District population = sum of its cells, rounded to whole persons. Density = population / the same cells' area on the WGS84 ellipsoid.

## Columns

| Column | Type | Unit | Description |
|---|---|---|---|
| `state_ut` | text |  | Place (2011 boundary; today's name and LGD code; LGD code blank for Mahe and Yanam) |
| `lgd_state_code` | text |  | Place (2011 boundary; today's name and LGD code; LGD code blank for Mahe and Yanam) |
| `district` | text |  | Place (2011 boundary; today's name and LGD code; LGD code blank for Mahe and Yanam) |
| `lgd_district_code` | text |  | Place (2011 boundary; today's name and LGD code; LGD code blank for Mahe and Yanam) |
| `district_census_code` | text |  | Place (2011 boundary; today's name and LGD code; LGD code blank for Mahe and Yanam) |
| `year` | text |  | GHSL epoch: 1975, 1980, ... 2030 |
| `population_persons` | integer |  | Resident population, persons |
| `grid_land_area_sq_km` | number | km² | District area as covered by the grid cells, sq km (close to, not equal to, the official area) |
| `population_density_per_sq_km` | number | km² | Persons per sq km of `grid_land_area_sq_km` |
| `source_flag` | text |  | `estimated` for 2025 and 2030 (JRC's projections) |

Units are read from the column name (warehouse convention). Empty cells (`null` in JSON) mean no value.

## Notes from the warehouse

These describe the full warehouse table (all states).

- **Our calculation from a modelled product.** For official counts use the Census ([`POP_census-pca_2011_STATES_ORGI_DIST`](https://github.com/sarveshkant2003-afk/bharatnomy-data/tree/41650b8bb1975a4f4e082ba172d8b5dfb8f7db8a/POP_census-pca_2011_STATES_ORGI_DIST/)). GHSL totals follow the UN, so the India total is a little above the Census (1,239.7 million in 2010 vs 1,210.9 million in Census 2011, which counted 1 March 2011).
- **Small districts are unreliable.** With 1 km cells and community boundaries, a few small districts get far too few or too many people: against Census 2011, Imphal West 0.10x and Imphal East 2.0x (their cells fall on each other's side), Ganderbal 0.23x, Daman 0.47x, Poonch 1.9x, Mahe 2.8x. For 90% of districts the 2010 value is within 0.89x-1.17x of Census 2011.
- 2011 boundaries throughout: `Thane` includes today's Palghar, etc.
- Checks (18 Nov 2026): 7,680 rows = 640 districts x 12 epochs; no duplicate keys; no negative values; log correlation with Census 2011 district population 0.990, median ratio 1.025. India total (in district polygons): 622.9 million (1975), 1,058.7 (2000), 1,395.3 (2020), 1,513.9 (2030). Nagpur: 4,763,502 (2010; Census 2011: 4,653,570), 5,312,775 (2020).

## Where this comes from

- Warehouse folder [`POP_population-grid_1975-to-2030_STATES_BNY_DIST`](https://github.com/sarveshkant2003-afk/bharatnomy-data/tree/41650b8bb1975a4f4e082ba172d8b5dfb8f7db8a/POP_population-grid_1975-to-2030_STATES_BNY_DIST) at commit `41650b8bb197`
- Filtered to `lgd_state_code` and cleaned by `build.py` in this repo. Files: `POP_population-grid_1975-to-2030_MH_BNY_DIST.csv`, `POP_population-grid_1975-to-2030_MH_BNY_DIST.json`.
