# Land use and irrigation by district, Maharashtra, 1998-99 to 2024-25 — Maharashtra

The nine-fold land use classification (forests, non-agricultural uses, barren land, pastures, tree crops, culturable waste, fallows, net sown area), cropped area, and net and gross irrigated area by source (canal, tank, tubewell, other wells, other sources) for each district of Maharashtra, in hectares.

## Coverage

- **Rows:** 346
- **Period:** 1998-99 to 2024-25
- **Districts:** 36 of 36
- 3 state-total row(s) from the warehouse table are left out; add up district rows instead.

## Source

- **Data:** Directorate of Economics & Statistics (DES), Ministry of Agriculture & Farmers' Welfare (MoA&FW), Land Use Statistics Information System
- **Table taken from:** LUS portal "Grand Query Report", district data, Maharashtra, all land-use and source-of-irrigation items, unit hectare, queried one year at a time
- **Link:** https://data.desagri.gov.in/weblus/lus-grand-query-report
- **Downloaded:** 28 Oct 2026
- **Original files:** [`_sources/moafw-lus-district/raw/`](https://github.com/sarveshkant2003-afk/bharatnomy-data/tree/eea39efd1c2b3c3ee8d93e2a99b9fb7981332889/_sources/moafw-lus-district/raw/) (the report HTML for each year)

## Columns

| Column | Type | Unit | Description |
|---|---|---|---|
| `state_ut` | text |  | Maharashtra |
| `lgd_state_code` | text |  | State/UT code in the Local Government Directory (LGD), from [`_reference/geography.csv`](https://github.com/sarveshkant2003-afk/bharatnomy-data/tree/eea39efd1c2b3c3ee8d93e2a99b9fb7981332889/_reference/geography.csv). Blank for All India and for old units LGD no longer lists |
| `district` | text |  | District as spelled on the portal (current names, e.g. Ahilyanagar, even for old years). `State total` = the portal's "Total of Maharashtra" row. `Maharashtra_Total` = a second total row the portal prints for 2021-22 to 2023-24 with only cropped-area and irrigation figures |
| `lgd_district_code` | text |  | District code in the Local Government Directory (LGD), from [`_reference/geography.csv`](https://github.com/sarveshkant2003-afk/bharatnomy-data/tree/eea39efd1c2b3c3ee8d93e2a99b9fb7981332889/_reference/geography.csv). Blank for totals and names that could not be matched |
| `year` | text |  | Agricultural year (July-June) |
| `reporting_area_ha` | integer | hectares | Area for which land use is reported, ha |
| `forests_ha` | integer | hectares | Classification of reporting area, ha (same items as `AGR_land-use-classification_*`) |
| `area_non_agricultural_uses_ha` | integer | hectares | Classification of reporting area, ha (same items as `AGR_land-use-classification_*`) |
| `barren_unculturable_land_ha` | integer | hectares | Classification of reporting area, ha (same items as `AGR_land-use-classification_*`) |
| `not_available_for_cultivation_total_ha` | integer | hectares | Classification of reporting area, ha (same items as `AGR_land-use-classification_*`) |
| `permanent_pastures_grazing_land_ha` | integer | hectares | Classification of reporting area, ha (same items as `AGR_land-use-classification_*`) |
| `misc_tree_crops_groves_ha` | integer | hectares | Classification of reporting area, ha (same items as `AGR_land-use-classification_*`) |
| `culturable_waste_land_ha` | integer | hectares | Classification of reporting area, ha (same items as `AGR_land-use-classification_*`) |
| `other_uncultivated_land_total_ha` | integer | hectares | Classification of reporting area, ha (same items as `AGR_land-use-classification_*`) |
| `fallow_other_than_current_ha` | integer | hectares | Classification of reporting area, ha (same items as `AGR_land-use-classification_*`) |
| `current_fallows_ha` | integer | hectares | Classification of reporting area, ha (same items as `AGR_land-use-classification_*`) |
| `fallow_land_total_ha` | integer | hectares | Classification of reporting area, ha (same items as `AGR_land-use-classification_*`) |
| `net_area_sown_ha` | integer | hectares | ha |
| `gross_cropped_area_ha` | integer | hectares | ha |
| `area_sown_more_than_once_ha` | integer | hectares | ha |
| `net_irrigated_canal_government_ha` | integer | hectares | Net irrigated area by source: `canal_government`, `canal_private`, `canal_total`, `tank`, `tubewell`, `other_well`, `well_total`, `other_sources`, `area_total` |
| `net_irrigated_canal_private_ha` | text | hectares | Net irrigated area by source: `canal_government`, `canal_private`, `canal_total`, `tank`, `tubewell`, `other_well`, `well_total`, `other_sources`, `area_total` |
| `net_irrigated_canal_total_ha` | integer | hectares | Net irrigated area by source: `canal_government`, `canal_private`, `canal_total`, `tank`, `tubewell`, `other_well`, `well_total`, `other_sources`, `area_total` |
| `net_irrigated_tank_ha` | integer | hectares | Net irrigated area by source: `canal_government`, `canal_private`, `canal_total`, `tank`, `tubewell`, `other_well`, `well_total`, `other_sources`, `area_total` |
| `net_irrigated_tubewell_ha` | integer | hectares | Net irrigated area by source: `canal_government`, `canal_private`, `canal_total`, `tank`, `tubewell`, `other_well`, `well_total`, `other_sources`, `area_total` |
| `net_irrigated_other_well_ha` | integer | hectares | Net irrigated area by source: `canal_government`, `canal_private`, `canal_total`, `tank`, `tubewell`, `other_well`, `well_total`, `other_sources`, `area_total` |
| `net_irrigated_well_total_ha` | integer | hectares | Net irrigated area by source: `canal_government`, `canal_private`, `canal_total`, `tank`, `tubewell`, `other_well`, `well_total`, `other_sources`, `area_total` |
| `net_irrigated_other_sources_ha` | integer | hectares | Net irrigated area by source: `canal_government`, `canal_private`, `canal_total`, `tank`, `tubewell`, `other_well`, `well_total`, `other_sources`, `area_total` |
| `net_irrigated_area_total_ha` | integer | hectares | Net irrigated area by source: `canal_government`, `canal_private`, `canal_total`, `tank`, `tubewell`, `other_well`, `well_total`, `other_sources`, `area_total` |
| `gross_irrigated_canal_government_ha` | integer | hectares | Gross irrigated area, same sources |
| `gross_irrigated_canal_private_ha` | text | hectares | Gross irrigated area, same sources |
| `gross_irrigated_canal_total_ha` | integer | hectares | Gross irrigated area, same sources |
| `gross_irrigated_tank_ha` | integer | hectares | Gross irrigated area, same sources |
| `gross_irrigated_tubewell_ha` | integer | hectares | Gross irrigated area, same sources |
| `gross_irrigated_other_well_ha` | integer | hectares | Gross irrigated area, same sources |
| `gross_irrigated_well_total_ha` | integer | hectares | Gross irrigated area, same sources |
| `gross_irrigated_other_sources_ha` | integer | hectares | Gross irrigated area, same sources |
| `gross_irrigated_area_total_ha` | integer | hectares | Gross irrigated area, same sources |
| `net_irrigated_pct_of_net_sown` | number |  | Net irrigated area as % of net sown area |
| `cropping_intensity_pct` | number | % | Gross cropped area as % of net sown area (100 = one crop a year) |
| `forest_pct_of_reporting_area` | number |  | Forest as % of reporting area |

Units are read from the column name (warehouse convention). Empty cells (`null` in JSON) mean no value.

## Notes from the warehouse

These describe the full warehouse table (all states).

- The portal has district data for Maharashtra only for 1998-99 to 2002-03 and 2020-21 to 2024-25; other years return empty tables.
- Since 2020-21 most districts show `-` for cropped and irrigated area (district irrigation is not reported), so irrigation is only available for 1998-99 to 2002-03. Cells printed as `-` or left empty are blank here; the portal does not say why.
- Agricultural vs non-agricultural land: agricultural land = net sown + current fallows + other fallows + culturable waste + tree crops (the LUS definition of agricultural or culturable land, as in `agricultural_land_000_ha` of `AGR_land-use-classification_*`); non-agricultural uses are in `area_non_agricultural_uses_ha`. Irrigated vs rain-fed: rain-fed = `net_area_sown_ha` - `net_irrigated_area_total_ha`.
- `lgd_state_code` and `lgd_district_code` added on 5 Nov 2026 from the LGD directory (see [`_reference/README.md`](https://github.com/sarveshkant2003-afk/bharatnomy-data/tree/eea39efd1c2b3c3ee8d93e2a99b9fb7981332889/_reference/README.md)). LGD codes identify today's state or district; for years before a split (Telangana 2014, Ladakh 2019, new districts) the same code covers a larger area than it does now.

## Where this comes from

- Warehouse folder [`AGR_land-use-irrigation_1998-99-to-2024-25_MH_MOAFW_DIST`](https://github.com/sarveshkant2003-afk/bharatnomy-data/tree/eea39efd1c2b3c3ee8d93e2a99b9fb7981332889/AGR_land-use-irrigation_1998-99-to-2024-25_MH_MOAFW_DIST) at commit `eea39efd1c2b`
- Filtered to `lgd_state_code` and cleaned by `build.py` in this repo. Files: `AGR_land-use-irrigation_1998-99-to-2024-25_MH_MOAFW_DIST.csv`, `AGR_land-use-irrigation_1998-99-to-2024-25_MH_MOAFW_DIST.json`.
