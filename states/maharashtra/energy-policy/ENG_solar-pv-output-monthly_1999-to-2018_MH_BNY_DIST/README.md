# Solar PV output by district and month of the year, 1999 to 2018 (long-term average) — Maharashtra

Potential electricity a solar panel would produce per day in each calendar month, in every district: the seasonal profile behind [`ENG_solar-resource_1999-to-2018_STATES_BNY_DIST`](https://github.com/sarveshkant2003-afk/bharatnomy-data/tree/b8f4a587d0b96c3fc3154b3b92bd76a81dd5dded/ENG_solar-resource_1999-to-2018_STATES_BNY_DIST/). Computed by Bharatnomy from the Global Solar Atlas.

## Coverage

- **Rows:** 420
- **Period:** 1999 to 2018
- **Districts:** 35 of 36

## Source

- **Data:** Global Solar Atlas 2.0 (Solargis, for the World Bank / ESMAP), India country GIS data, long-term averages of daily totals (`India_GISdata_LTAy_AvgDailyTotals_GlobalSolarAtlas-v2_GEOTIFF`). Irradiation and PV output cover 1999-2018, air temperature 1994-2018. CC BY 4.0
- **Link:** https://globalsolaratlas.info/download/india (file list: https://api.globalsolaratlas.info/download/India; no login)
- **Downloaded:** 18 Nov 2026 (rasters not committed, about 820 MB; `pipelines/global-solar-atlas/fetch_gsa.sh` downloads them, see [`_sources/global-solar-atlas/`](https://github.com/sarveshkant2003-afk/bharatnomy-data/tree/b8f4a587d0b96c3fc3154b3b92bd76a81dd5dded/_sources/global-solar-atlas/))
- **District boundaries:** Census 2011 district map from DataMeet (see [`_sources/datameet-maps/`](https://github.com/sarveshkant2003-afk/bharatnomy-data/tree/b8f4a587d0b96c3fc3154b3b92bd76a81dd5dded/_sources/datameet-maps/))
- **Script:** [`pipelines/global-solar-atlas/build_district_solar_resource.py`](https://github.com/sarveshkant2003-afk/bharatnomy-data/tree/b8f4a587d0b96c3fc3154b3b92bd76a81dd5dded/pipelines/global-solar-atlas/build_district_solar_resource.py) (writes both solar tables)

## How it is computed

- District value = plain mean of the grid cells whose centre lies inside the district's 2011 boundary (GHI, DNI, DIF, GTI on a 9 arc-second grid, about 250 m; PVOUT and temperature on 30 arc-seconds, about 1 km; optimum tilt on 2 arc-minutes). Same method as [`CLM_wind-resource-100m_*`](https://github.com/sarveshkant2003-afk/bharatnomy-data/tree/b8f4a587d0b96c3fc3154b3b92bd76a81dd5dded/CLM_wind-resource-100m_2008-to-2017_STATES_BNY_DIST/).
- `raster_coverage_pct` = cells with a value as % of the cells the district's area would hold; a district below 50% would be left blank (none is; Lakshadweep is lowest at 53%, its islands are small).

## Columns

| Column | Type | Unit | Description |
|---|---|---|---|
| `state_ut` | text |  | Place (2011 boundary; today's name and LGD code; LGD code blank for Mahe and Yanam) |
| `lgd_state_code` | text |  | Place (2011 boundary; today's name and LGD code; LGD code blank for Mahe and Yanam) |
| `district` | text |  | Place (2011 boundary; today's name and LGD code; LGD code blank for Mahe and Yanam) |
| `lgd_district_code` | text |  | Place (2011 boundary; today's name and LGD code; LGD code blank for Mahe and Yanam) |
| `district_census_code` | text |  | Place (2011 boundary; today's name and LGD code; LGD code blank for Mahe and Yanam) |
| `month_of_year` | integer |  | Calendar month, 1 (January) to 12 (December); each value is the 1999-2018 average for that month |
| `pvout_kwh_kwp_day` | number |  | Potential PV output per kW-peak installed, average day of that month, kWh/kWp/day |

Units are read from the column name (warehouse convention). Empty cells (`null` in JSON) mean no value.

## Notes from the warehouse

These describe the full warehouse table (all states).

- **Our calculation from a modelled satellite product**; same PV configuration and caveats as the yearly table.
- The month is a calendar month averaged over 1999-2018, not a specific year, so the column is `month_of_year`, not `month`.
- Checks (18 Nov 2026): 7,680 rows = 640 districts x 12 months; no duplicate keys; no blank values; the day-weighted mean over the months equals the yearly PVOUT within 0.001. The monsoon dip is clear: Nagpur 4.58 in May, 2.79 in July.

## Where this comes from

- Warehouse folder [`ENG_solar-pv-output-monthly_1999-to-2018_STATES_BNY_DIST`](https://github.com/sarveshkant2003-afk/bharatnomy-data/tree/b8f4a587d0b96c3fc3154b3b92bd76a81dd5dded/ENG_solar-pv-output-monthly_1999-to-2018_STATES_BNY_DIST) at commit `b8f4a587d0b9`
- Filtered to `lgd_state_code` and cleaned by `build.py` in this repo. Files: `ENG_solar-pv-output-monthly_1999-to-2018_MH_BNY_DIST.csv`, `ENG_solar-pv-output-monthly_1999-to-2018_MH_BNY_DIST.json`.
