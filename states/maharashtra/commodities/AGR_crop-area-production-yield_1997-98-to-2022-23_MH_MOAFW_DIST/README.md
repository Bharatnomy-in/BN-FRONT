# Crop area, production and yield by district, 2010-11 to 2022-23 — Maharashtra

Area sown, production and yield of every crop and season reported for every district of India, by agricultural year. This is one of two files (split by year range to keep each under 25 MB); the other is [`AGR_crop-area-production-yield_1997-98-to-2009-10_STATES_MOAFW_DIST`](https://github.com/sarveshkant2003-afk/bharatnomy-data/tree/b8f4a587d0b96c3fc3154b3b92bd76a81dd5dded/AGR_crop-area-production-yield_1997-98-to-2009-10_STATES_MOAFW_DIST/).

## Coverage

- **Rows:** 20,978
- **Period:** 1997-98 to 2022-23
- **Districts:** 36 of 36
- Merged from 2 warehouse tables split by period.

## Source (1997-98 to 2009-10)

- **Data:** Directorate of Economics & Statistics (DES), Ministry of Agriculture & Farmers Welfare, Crop Production Statistics (Area, Production and Yield, APY), district level
- **Table taken from:** "Crops APY report" on the DES data portal: all states one at a time, all districts, all crops, all seasons, 1997-98 to 2022-23, format "Horizontal Crop and Vertical Year"
- **Link:** https://data.desagri.gov.in/website/crops-apy-report-web
- **Downloaded:** 12 Nov 2026 (report pages not committed, about 150 MB; `pipelines/moafw-apy/fetch_apy.py` downloads them, see [`_sources/moafw-apy/`](https://github.com/sarveshkant2003-afk/bharatnomy-data/tree/b8f4a587d0b96c3fc3154b3b92bd76a81dd5dded/_sources/moafw-apy/))
- **Script:** [`pipelines/moafw-apy/build_apy.py`](https://github.com/sarveshkant2003-afk/bharatnomy-data/tree/b8f4a587d0b96c3fc3154b3b92bd76a81dd5dded/pipelines/moafw-apy/build_apy.py)

## Source (2010-11 to 2022-23)

- **Data:** Directorate of Economics & Statistics (DES), Ministry of Agriculture & Farmers Welfare, Crop Production Statistics (Area, Production and Yield, APY), district level
- **Table taken from:** "Crops APY report" on the DES data portal: all states one at a time, all districts, all crops, all seasons, 1997-98 to 2022-23, format "Horizontal Crop and Vertical Year"
- **Link:** https://data.desagri.gov.in/website/crops-apy-report-web
- **Downloaded:** 12 Nov 2026 (report pages not committed, about 150 MB; `pipelines/moafw-apy/fetch_apy.py` downloads them, see [`_sources/moafw-apy/`](https://github.com/sarveshkant2003-afk/bharatnomy-data/tree/b8f4a587d0b96c3fc3154b3b92bd76a81dd5dded/_sources/moafw-apy/))
- **Script:** [`pipelines/moafw-apy/build_apy.py`](https://github.com/sarveshkant2003-afk/bharatnomy-data/tree/b8f4a587d0b96c3fc3154b3b92bd76a81dd5dded/pipelines/moafw-apy/build_apy.py)

## Columns

| Column | Type | Unit | Description |
|---|---|---|---|
| `state_ut` | text |  | State or UT (`Dadra & Nagar Haveli`, `Daman & Diu` as reported for the years before their merger) |
| `lgd_state_code` | text |  | State/UT code in the Local Government Directory (LGD), from [`_reference/geography.csv`](https://github.com/sarveshkant2003-afk/bharatnomy-data/tree/b8f4a587d0b96c3fc3154b3b92bd76a81dd5dded/_reference/geography.csv) |
| `district` | text |  | District as spelled by DES |
| `lgd_district_code` | text |  | District code in the LGD; blank where the DES name could not be matched (50 of 748 names, e.g. old or differently spelled districts) |
| `year` | text |  | Agricultural year (July-June), e.g. `2022-23` |
| `crop` | text |  | Crop as named by DES (includes DES totals such as `Total foodgrain`, `Pulses total`, `Oilseeds total` where reported) |
| `season` | text |  | `Kharif`, `Rabi`, `Autumn`, `Winter`, `Summer`, `Whole Year` |
| `area_ha` | number | hectares | Area, hectares |
| `production` | number |  | Production, in `production_unit` |
| `yield` | number |  | Yield, in `yield_unit` (production / area) |
| `production_unit` | text |  | `Tonnes`; `Bales` for cotton (lint), jute and mesta; `Nuts` for coconut (as labelled by DES) |
| `yield_unit` | text |  | `Tonne/Hectare`, `Bales/Hectare` or `Nuts/Hectare` |

Units are read from the column name (warehouse convention). Empty cells (`null` in JSON) mean no value.

## Notes from the warehouse

These describe the full warehouse table (all states).

- One row per district, year, crop and season that has at least one value. Blank cells are blank in the report (DES gives no reason). Crop-season pairs not reported for a district do not appear.
- Values are as printed by DES (thousands separators removed, decimals kept). Some values look odd but are DES's own, e.g. Ahilyanagar sugarcane 1997-98: 45,900 ha, 38,940 tonnes, yield 0.85; checked against single-crop queries of the same portal.
- No state or India totals: the report gives districts only.
- District boundaries and names change over time (new districts appear in later years); match across years with care.
- Checks (12 Nov 2026): 224,209 rows in this file (407,903 in both); no duplicate district-year-crop-season keys; all state names valid; yield equals production / area within rounding in all but 11 of 402,928 rows that have all three (tiny areas such as 0.01 ha); no negative values.

## Where this comes from

- Warehouse folder [`AGR_crop-area-production-yield_1997-98-to-2009-10_STATES_MOAFW_DIST`](https://github.com/sarveshkant2003-afk/bharatnomy-data/tree/b8f4a587d0b96c3fc3154b3b92bd76a81dd5dded/AGR_crop-area-production-yield_1997-98-to-2009-10_STATES_MOAFW_DIST) at commit `b8f4a587d0b9`
- Warehouse folder [`AGR_crop-area-production-yield_2010-11-to-2022-23_STATES_MOAFW_DIST`](https://github.com/sarveshkant2003-afk/bharatnomy-data/tree/b8f4a587d0b96c3fc3154b3b92bd76a81dd5dded/AGR_crop-area-production-yield_2010-11-to-2022-23_STATES_MOAFW_DIST) at commit `b8f4a587d0b9`
- Filtered to `lgd_state_code` and cleaned by `build.py` in this repo. Files: `AGR_crop-area-production-yield_1997-98-to-2022-23_MH_MOAFW_DIST.csv`, `AGR_crop-area-production-yield_1997-98-to-2022-23_MH_MOAFW_DIST.json`.
