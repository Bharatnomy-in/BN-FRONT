# Aerosols, soil wetness, evaporation and mixing height by district, Maharashtra, monthly, 1981 to 2025 — Maharashtra

One row per district per month: aerosol optical depth (haze and dust), soil wetness, evaporation from land, the top of the boundary layer, and an approximate mixing height and ventilation coefficient (how well the air disperses pollution). Computed by Bharatnomy from NASA POWER monthly data.

## Coverage

- **Rows:** 18,900
- **Period:** 1981 to 2025
- **Districts:** 35 of 36

## Source

- **Data:** NASA Prediction Of Worldwide Energy Resources (POWER), monthly, from the MERRA-2 reanalysis on a 0.5 x 0.625 degree grid (parameters AOD_55, GWETTOP, GWETROOT, GWETPROF, EVLAND, PBLTOP, PS, T2M, WS10M)
- **Link:** https://power.larc.nasa.gov/ (monthly point API, no login)
- **Downloaded:** 12 Nov 2026
- **District boundaries:** Census 2011 district map from DataMeet (see [`_sources/datameet-maps/`](https://github.com/sarveshkant2003-afk/bharatnomy-data/tree/930603697458e4ad288a0344bcd0c4c001d4462c/_sources/datameet-maps/))
- **Original files:** [`_sources/nasa-power/`](https://github.com/sarveshkant2003-afk/bharatnomy-data/tree/930603697458e4ad288a0344bcd0c4c001d4462c/_sources/nasa-power/) (not committed; `pipelines/nasa-power/fetch_power_monthly.py` downloads them in about 5 minutes)
- **Script:** [`pipelines/nasa-power/build_district_monthly.py`](https://github.com/sarveshkant2003-afk/bharatnomy-data/tree/930603697458e4ad288a0344bcd0c4c001d4462c/pipelines/nasa-power/build_district_monthly.py)

## How it is computed

- **District value** = area-weighted average of the POWER cells overlapping the district's 2011 boundary (2 to 14 cells).
- **Mixing height (approx.)** = (287.05 x T / 9.81) x ln(surface pressure / boundary-layer-top pressure), with T the 2 m temperature in kelvin: the height of the boundary-layer top above the ground, from the two pressures.
- **Ventilation coefficient (approx.)** = mixing height x 10 m wind speed. Both use monthly means, so they are rougher than values from hourly data (pollution forecasters use the daily minimum, often at night or early morning).

## Columns

| Column | Type | Unit | Description |
|---|---|---|---|
| `state_ut` | text |  | Place (2011 boundary; today's name and LGD code) |
| `lgd_state_code` | text |  | Place (2011 boundary; today's name and LGD code) |
| `district` | text |  | Place (2011 boundary; today's name and LGD code) |
| `lgd_district_code` | text |  | Place (2011 boundary; today's name and LGD code) |
| `district_census_code` | text |  | Place (2011 boundary; today's name and LGD code) |
| `month` | text |  | Year; month as YYYY-MM |
| `year` | text |  | Year; month as YYYY-MM |
| `aod_550nm` | number |  | Aerosol optical depth at 550 nm, no unit (0.1 clear, above 1 very hazy) |
| `soil_wetness_surface_frac` | number | fraction (0-1) | Surface soil wetness, top 5 cm: 0 = completely dry, 1 = saturated |
| `soil_wetness_root_zone_frac` | number | fraction (0-1) | Root-zone soil wetness, top ~1 m, 0 to 1 |
| `soil_wetness_profile_frac` | number | fraction (0-1) | Soil wetness of the whole soil column, 0 to 1 |
| `evaporation_land_mm_day` | number | mm/day | Evaporation from land (soil, plants, wet surfaces: evapotranspiration), mm per day, monthly mean |
| `pbl_top_pressure_kpa` | number |  | Air pressure at the top of the planetary boundary layer, kPa |
| `surface_pressure_kpa` | number |  | Surface air pressure, kPa |
| `temperature_2m_c` | number | °C | Mean air temperature at 2 m, C |
| `wind_speed_10m_ms` | number | m/s | Mean wind speed at 10 m, m/s |
| `mixing_height_approx_m` | number |  | Approximate mixing height, m (see above) |
| `ventilation_coefficient_approx_m2s` | number |  | Approximate ventilation coefficient, m2/s (see above) |
| `source_flag` | text |  | `not_available` where `aod_550nm` is blank (POWER has no aerosol data before 2001) |

Units are read from the column name (warehouse convention). Empty cells (`null` in JSON) mean no value.

## Notes from the warehouse

These describe the full warehouse table (all states).

- **Model data, not measurements.** MERRA-2 is a reanalysis (a weather model fitted to observations) with cells about 55 x 65 km. AOD here is MERRA-2's, not MODIS satellite retrievals (those need a NASA Earthdata login).
- Soil wetness is a 0-1 index, not volumetric soil moisture (m3/m3).
- POWER's month "13" (its annual value) is not kept.
- `Thane` includes today's Palghar (2011 boundaries).
- Checks (12 Nov 2026): 18,900 rows = 35 districts x 540 months; no duplicate keys; blanks only in `aod_550nm` before 2001 (8,400 cells); soil wetness within 0-1; no negative evaporation.

## Where this comes from

- Warehouse folder [`CLM_aerosol-soil-evaporation-boundary-layer_1981-to-2025_MH_BNY_DIST`](https://github.com/sarveshkant2003-afk/bharatnomy-data/tree/930603697458e4ad288a0344bcd0c4c001d4462c/CLM_aerosol-soil-evaporation-boundary-layer_1981-to-2025_MH_BNY_DIST) at commit `930603697458`
- Filtered to `lgd_state_code` and cleaned by `build.py` in this repo. Files: `CLM_aerosol-soil-evaporation-boundary-layer_1981-to-2025_MH_BNY_DIST.csv`, `CLM_aerosol-soil-evaporation-boundary-layer_1981-to-2025_MH_BNY_DIST.json`.
