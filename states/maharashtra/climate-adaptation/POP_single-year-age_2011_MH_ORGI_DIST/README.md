# Population by single year of age, Maharashtra districts, 2011 — Maharashtra

Census 2011 population of each age from 0 to 99, 100+ and "age not stated", by sex and rural/urban, for Maharashtra and its 35 districts. Use it for the share of elderly people (e.g. 60+ or 65+).

## Coverage

- **Rows:** 3,605
- **Period:** 2011
- **Districts:** 35 of 36
- 103 state-total row(s) from the warehouse table are left out; add up district rows instead.

## Source

- **Data:** Office of the Registrar General & Census Commissioner, India (ORGI), Census of India 2011
- **Table taken from:** "C-13: Single year age returns by residence and sex, Maharashtra - 2011", file `DDW-2700C-13.xls`
- **Link:** https://censusindia.gov.in/nada/index.php/catalog/1457
- **Downloaded:** 28 Oct 2026
- **Original file:** [`_sources/orgi-census2011/raw/`](https://github.com/sarveshkant2003-afk/bharatnomy-data/tree/eea39efd1c2b3c3ee8d93e2a99b9fb7981332889/_sources/orgi-census2011/raw/)

## Columns

| Column | Type | Unit | Description |
|---|---|---|---|
| `state_ut` | text |  | Maharashtra |
| `lgd_state_code` | text |  | State/UT code in the Local Government Directory (LGD), from [`_reference/geography.csv`](https://github.com/sarveshkant2003-afk/bharatnomy-data/tree/eea39efd1c2b3c3ee8d93e2a99b9fb7981332889/_reference/geography.csv). Blank for All India and for old units LGD no longer lists |
| `district` | text |  | District as spelled by the Census. `State total` = Maharashtra's published total |
| `lgd_district_code` | text |  | District code in the Local Government Directory (LGD), from [`_reference/geography.csv`](https://github.com/sarveshkant2003-afk/bharatnomy-data/tree/eea39efd1c2b3c3ee8d93e2a99b9fb7981332889/_reference/geography.csv). Blank for totals and names that could not be matched |
| `district_census_code` | text |  | Census 2011 district code (Nagpur = 505) |
| `age` | text |  | `All ages`, `0` ... `99`, `100+`, `Age not stated` |
| `persons_total` | integer |  | Population, rural + urban |
| `males_total` | integer |  | Population, rural + urban |
| `females_total` | integer |  | Population, rural + urban |
| `persons_rural` | integer |  | Same, rural and urban |
| `males_rural` | integer |  | Same, rural and urban |
| `females_rural` | integer |  | Same, rural and urban |
| `persons_urban` | integer |  | Same, rural and urban |
| `males_urban` | integer |  | Same, rural and urban |
| `females_urban` | integer |  | Same, rural and urban |

Units are read from the column name (warehouse convention). Empty cells (`null` in JSON) mean no value.

## Notes from the warehouse

These describe the full warehouse table (all states).

- Only Maharashtra is here; other states' C-13 tables are separate files on the same portal (catalog "C-13 ... <state> - 2011").
- `All ages` rows are the published totals; leave them out before adding ages up.
- `lgd_state_code` and `lgd_district_code` added on 5 Nov 2026 from the LGD directory (see [`_reference/README.md`](https://github.com/sarveshkant2003-afk/bharatnomy-data/tree/eea39efd1c2b3c3ee8d93e2a99b9fb7981332889/_reference/README.md)). LGD codes identify today's state or district; for years before a split (Telangana 2014, Ladakh 2019, new districts) the same code covers a larger area than it does now.

## Where this comes from

- Warehouse folder [`POP_single-year-age_2011_MH_ORGI_DIST`](https://github.com/sarveshkant2003-afk/bharatnomy-data/tree/eea39efd1c2b3c3ee8d93e2a99b9fb7981332889/POP_single-year-age_2011_MH_ORGI_DIST) at commit `eea39efd1c2b`
- Filtered to `lgd_state_code` and cleaned by `build.py` in this repo. Files: `POP_single-year-age_2011_MH_ORGI_DIST.csv`, `POP_single-year-age_2011_MH_ORGI_DIST.json`.
