# Heat and rainfall indicators for Nagpur, 1951 to 2025 — Maharashtra

One row per year for Nagpur: hottest day and night, heat wave days, warm nights, hot days and nights relative to normal, annual and monsoon rainfall with departure from normal, and land surface temperature from satellite. Computed by Bharatnomy from IMD gridded data and NASA MODIS; IMD does not publish these figures for Nagpur as a table.

## Coverage

- **Rows:** 75
- **Period:** 1951 to 2025
- **Districts:** 1 of 36 (Nagpur)

## Source

- **Data:** India Meteorological Department (IMD) Pune daily gridded data: maximum and minimum temperature, 1.0 x 1.0 degree, 1951-2024; rainfall, 0.25 x 0.25 degree, 1951-2025. NASA MOD11A2 v6.1 land surface temperature (Terra MODIS, 8-day, 1 km)
- **Link:** https://imdpune.gov.in/lrfindex.php ; https://modis.ornl.gov/rst/api/v1/
- **Downloaded:** 28 Oct 2026
- **Original files:** [`_sources/imd-gridded/`](https://github.com/sarveshkant2003-afk/bharatnomy-data/tree/cd7ce2d673103cc0e606e3cc37e49a9ae75f849a/_sources/imd-gridded/) (not committed, 1.9 GB; download steps in its README) and [`_sources/nasa-modis-lst/raw/`](https://github.com/sarveshkant2003-afk/bharatnomy-data/tree/cd7ce2d673103cc0e606e3cc37e49a9ae75f849a/_sources/nasa-modis-lst/raw/)

## How it is computed

- **Temperature** is the IMD grid interpolated (bilinear) to Nagpur city, 21.1458 N 79.0882 E.
- **Rainfall** is the average of the 42 IMD 0.25-degree cells with centres in 20.50-21.75 N, 78.25-79.75 E, a box around Nagpur district (not its exact boundary).
- **Normal** = 1991-2020 for temperature (daily, smoothed with a 31-day running mean); 1971-2020 for rainfall (IMD's long period average).
- **Heat wave day** (IMD criteria for the plains): Tmax at least 40 C and at least 4.5 C above normal, or Tmax at least 45 C. **Severe**: at least 6.5 C above normal or Tmax at least 47 C.
- **Warm night** (IMD): Tmin at least 4.5 C above normal while Tmax is at least 40 C.
- **Above p90**: Tmax (or Tmin) above the 90th percentile of the same calendar days (5-day window) in 1991-2020.
- **LST**: mean of clear 1 km pixels in a 21 x 21 km box centred on the city, for each 8-day composite with at least half the box clear.

## Columns

| Column | Type | Unit | Description |
|---|---|---|---|
| `state_ut` | text |  | Maharashtra, Nagpur |
| `lgd_state_code` | text |  | State/UT code in the Local Government Directory (LGD), from [`_reference/geography.csv`](https://github.com/sarveshkant2003-afk/bharatnomy-data/tree/cd7ce2d673103cc0e606e3cc37e49a9ae75f849a/_reference/geography.csv). Blank for All India and for old units LGD no longer lists |
| `district` | text |  | Maharashtra, Nagpur |
| `lgd_district_code` | text |  | District code in the Local Government Directory (LGD), from [`_reference/geography.csv`](https://github.com/sarveshkant2003-afk/bharatnomy-data/tree/cd7ce2d673103cc0e606e3cc37e49a9ae75f849a/_reference/geography.csv). Blank for totals and names that could not be matched |
| `year` | text |  | Calendar year |
| `tmax_highest_c` | number | °C | Highest daily maximum / minimum temperature of the year, C |
| `tmax_mean_mar_may_c` | number | °C | Mean daily max / min temperature, March-May, C |
| `tmin_highest_c` | number | °C | Highest daily maximum / minimum temperature of the year, C |
| `tmin_mean_mar_may_c` | number | °C | Mean daily max / min temperature, March-May, C |
| `days_tmax_40c_or_more` | integer |  | Days with Tmax at or above 40 C / 45 C |
| `days_tmax_45c_or_more` | integer |  | Days with Tmax at or above 40 C / 45 C |
| `heatwave_days` | integer |  | Days meeting the IMD heat wave / severe heat wave criteria |
| `severe_heatwave_days` | integer |  | Days meeting the IMD heat wave / severe heat wave criteria |
| `warm_nights` | integer |  | Nights meeting the IMD warm night criteria |
| `days_tmax_above_p90` | integer |  | Days with Tmax / Tmin above the 1991-2020 90th percentile |
| `nights_tmin_above_p90` | integer |  | Days with Tmax / Tmin above the 1991-2020 90th percentile |
| `rainfall_annual_mm` | number | mm | Rainfall in the year / in the south-west monsoon (June-September), mm |
| `rainfall_annual_departure_pct` | number | % | Departure from the 1971-2020 average, % |
| `rainfall_jun_sep_mm` | number | mm | Rainfall in the year / in the south-west monsoon (June-September), mm |
| `rainfall_jun_sep_departure_pct` | number | % | Departure from the 1971-2020 average, % |
| `lst_day_mean_mar_may_c` | number | °C | Mean land surface temperature (about 10:30 and 22:30 local time), March-May, C |
| `lst_day_highest_8day_c` | number | °C | Highest 8-day mean land surface temperature of the year, C |
| `lst_night_mean_mar_may_c` | number | °C | Mean land surface temperature (about 10:30 and 22:30 local time), March-May, C |
| `lst_night_highest_8day_c` | number | °C | Highest 8-day mean land surface temperature of the year, C |

Units are read from the column name (warehouse convention). Empty cells (`null` in JSON) mean no value.

## Notes from the warehouse

These describe the full warehouse table (all states).

- **The 1-degree grid smooths out extremes.** Gridded Tmax for Nagpur peaks around 42-45 C, while the Nagpur (Sonegaon) observatory reaches 46-47 C in hot years. IMD's heat wave and warm night rules are written for station readings, so `heatwave_days` and `warm_nights` here are much lower than station-based counts and are best read as a trend, not a count of declared heat waves. The percentile columns do not depend on absolute thresholds and are the better measure of change over time.
- IMD notes that its gridded temperature from 2008 onward is based on fewer stations (about 180).
- Temperature is not yet available for 2025 (IMD has published 2024 so far).
- **LST is incomplete for now:** day LST covers 2002-2022 and night LST 2002-2011, because the download was stopped partway; only years with all 8-day composites downloaded are filled. 2001 has gaps in the MODIS record and is left blank.
- Land surface temperature is the temperature of the ground and roofs, not of the air; it runs well above air temperature on summer afternoons.
- Blank cells are years outside a source's coverage.
- `lgd_state_code` and `lgd_district_code` added on 5 Nov 2026 from the LGD directory (see [`_reference/README.md`](https://github.com/sarveshkant2003-afk/bharatnomy-data/tree/cd7ce2d673103cc0e606e3cc37e49a9ae75f849a/_reference/README.md)). LGD codes identify today's state or district; for years before a split (Telangana 2014, Ladakh 2019, new districts) the same code covers a larger area than it does now.

## Where this comes from

- Warehouse folder [`CLM_heat-indicators-nagpur_1951-to-2025_MH_BNY_DIST`](https://github.com/sarveshkant2003-afk/bharatnomy-data/tree/cd7ce2d673103cc0e606e3cc37e49a9ae75f849a/CLM_heat-indicators-nagpur_1951-to-2025_MH_BNY_DIST) at commit `cd7ce2d67310`
- Filtered to `lgd_state_code` and cleaned by `build.py` in this repo. Files: `CLM_heat-indicators-nagpur_1951-to-2025_MH_BNY_DIST.csv`, `CLM_heat-indicators-nagpur_1951-to-2025_MH_BNY_DIST.json`.
