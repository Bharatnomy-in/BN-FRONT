# Primary Census Abstract by district, 2011 — Maharashtra

Population, households, literacy, Scheduled Castes and Tribes, and workers by category (cultivators, agricultural labourers, household industry, other workers; main and marginal) for every district of India in Census 2011, each split into total, rural and urban.

## Coverage

- **Rows:** 105
- **Period:** 2011
- **Districts:** 35 of 36
- 3 state-total row(s) from the warehouse table are left out; add up district rows instead.

## Source

- **Data:** Office of the Registrar General & Census Commissioner, India (ORGI), Census of India 2011, Primary Census Abstract (PCA)
- **Table taken from:** "PCA SD: Primary census abstract (PCA) data, India & States/UTs - State and district level - 2011", file `DDW_PCA0000_2011_Indiastatedist.xlsx`
- **Link:** https://censusindia.gov.in/nada/index.php/catalog/6191
- **Downloaded:** 28 Oct 2026
- **Original file:** [`_sources/orgi-census2011/raw/`](https://github.com/sarveshkant2003-afk/bharatnomy-data/tree/cd7ce2d673103cc0e606e3cc37e49a9ae75f849a/_sources/orgi-census2011/raw/)

## Columns

| Column | Type | Unit | Description |
|---|---|---|---|
| `state_ut` | text |  | State or UT as it was in 2011 (Andhra Pradesh includes Telangana; Jammu & Kashmir includes Ladakh; Dadra & Nagar Haveli and Daman & Diu are separate) |
| `lgd_state_code` | text |  | State/UT code in the Local Government Directory (LGD), from [`_reference/geography.csv`](https://github.com/sarveshkant2003-afk/bharatnomy-data/tree/cd7ce2d673103cc0e606e3cc37e49a9ae75f849a/_reference/geography.csv). Blank for All India and for old units LGD no longer lists |
| `district` | text |  | District as spelled by the Census. `State total` = the state's published total; blank on the `All India` row |
| `lgd_district_code` | text |  | District code in the Local Government Directory (LGD), from [`_reference/geography.csv`](https://github.com/sarveshkant2003-afk/bharatnomy-data/tree/cd7ce2d673103cc0e606e3cc37e49a9ae75f849a/_reference/geography.csv). Blank for totals and names that could not be matched |
| `state_census_code` | text |  | Census 2011 codes (Nagpur = 27 / 505) |
| `district_census_code` | text |  | Census 2011 codes (Nagpur = 27 / 505) |
| `area` | text |  | `total`, `rural` or `urban` |
| `households` | integer |  | Number of households |
| `population_persons` | integer |  | Population, all ages and age 0-6 |
| `population_males` | integer |  | Population, all ages and age 0-6 |
| `population_females` | integer |  | Population, all ages and age 0-6 |
| `population_age_0_6_persons` | integer |  | Population, all ages and age 0-6 |
| `population_age_0_6_males` | integer |  | Population, all ages and age 0-6 |
| `population_age_0_6_females` | integer |  | Population, all ages and age 0-6 |
| `scheduled_castes_persons` | integer |  | SC and ST population |
| `scheduled_castes_males` | integer |  | SC and ST population |
| `scheduled_castes_females` | integer |  | SC and ST population |
| `scheduled_tribes_persons` | integer |  | SC and ST population |
| `scheduled_tribes_males` | integer |  | SC and ST population |
| `scheduled_tribes_females` | integer |  | SC and ST population |
| `literates_persons` | integer |  | Literate and illiterate population |
| `literates_males` | integer |  | Literate and illiterate population |
| `literates_females` | integer |  | Literate and illiterate population |
| `illiterates_persons` | integer |  | Literate and illiterate population |
| `illiterates_males` | integer |  | Literate and illiterate population |
| `illiterates_females` | integer |  | Literate and illiterate population |
| `total_workers_persons` | integer |  | Main + marginal workers |
| `total_workers_males` | integer |  | Main + marginal workers |
| `total_workers_females` | integer |  | Main + marginal workers |
| `main_workers_persons` | integer |  | Worked 6 months or more in the year. Split into `main_cultivators_*`, `main_agricultural_labourers_*`, `main_household_industry_workers_*`, `main_other_workers_*` |
| `main_workers_males` | integer |  | Worked 6 months or more in the year. Split into `main_cultivators_*`, `main_agricultural_labourers_*`, `main_household_industry_workers_*`, `main_other_workers_*` |
| `main_workers_females` | integer |  | Worked 6 months or more in the year. Split into `main_cultivators_*`, `main_agricultural_labourers_*`, `main_household_industry_workers_*`, `main_other_workers_*` |
| `main_cultivators_persons` | integer |  | Worked 6 months or more in the year. Split into `main_cultivators_*`, `main_agricultural_labourers_*`, `main_household_industry_workers_*`, `main_other_workers_*` |
| `main_cultivators_males` | integer |  | Worked 6 months or more in the year. Split into `main_cultivators_*`, `main_agricultural_labourers_*`, `main_household_industry_workers_*`, `main_other_workers_*` |
| `main_cultivators_females` | integer |  | Worked 6 months or more in the year. Split into `main_cultivators_*`, `main_agricultural_labourers_*`, `main_household_industry_workers_*`, `main_other_workers_*` |
| `main_agricultural_labourers_persons` | integer |  | Worked 6 months or more in the year. Split into `main_cultivators_*`, `main_agricultural_labourers_*`, `main_household_industry_workers_*`, `main_other_workers_*` |
| `main_agricultural_labourers_males` | integer |  | Worked 6 months or more in the year. Split into `main_cultivators_*`, `main_agricultural_labourers_*`, `main_household_industry_workers_*`, `main_other_workers_*` |
| `main_agricultural_labourers_females` | integer |  | Worked 6 months or more in the year. Split into `main_cultivators_*`, `main_agricultural_labourers_*`, `main_household_industry_workers_*`, `main_other_workers_*` |
| `main_household_industry_workers_persons` | integer |  | Worked 6 months or more in the year. Split into `main_cultivators_*`, `main_agricultural_labourers_*`, `main_household_industry_workers_*`, `main_other_workers_*` |
| `main_household_industry_workers_males` | integer |  | Worked 6 months or more in the year. Split into `main_cultivators_*`, `main_agricultural_labourers_*`, `main_household_industry_workers_*`, `main_other_workers_*` |
| `main_household_industry_workers_females` | integer |  | Worked 6 months or more in the year. Split into `main_cultivators_*`, `main_agricultural_labourers_*`, `main_household_industry_workers_*`, `main_other_workers_*` |
| `main_other_workers_persons` | integer |  | Worked 6 months or more in the year. Split into `main_cultivators_*`, `main_agricultural_labourers_*`, `main_household_industry_workers_*`, `main_other_workers_*` |
| `main_other_workers_males` | integer |  | Worked 6 months or more in the year. Split into `main_cultivators_*`, `main_agricultural_labourers_*`, `main_household_industry_workers_*`, `main_other_workers_*` |
| `main_other_workers_females` | integer |  | Worked 6 months or more in the year. Split into `main_cultivators_*`, `main_agricultural_labourers_*`, `main_household_industry_workers_*`, `main_other_workers_*` |
| `marginal_workers_persons` | integer |  | Worked less than 6 months, with the same four categories (`marginal_cultivators_*` ...) and split by duration: `..._3_to_6_months_*` and `..._less_than_3_months_*` |
| `marginal_workers_males` | integer |  | Worked less than 6 months, with the same four categories (`marginal_cultivators_*` ...) and split by duration: `..._3_to_6_months_*` and `..._less_than_3_months_*` |
| `marginal_workers_females` | integer |  | Worked less than 6 months, with the same four categories (`marginal_cultivators_*` ...) and split by duration: `..._3_to_6_months_*` and `..._less_than_3_months_*` |
| `marginal_cultivators_persons` | integer |  | Worked less than 6 months, with the same four categories (`marginal_cultivators_*` ...) and split by duration: `..._3_to_6_months_*` and `..._less_than_3_months_*` |
| `marginal_cultivators_males` | integer |  | Worked less than 6 months, with the same four categories (`marginal_cultivators_*` ...) and split by duration: `..._3_to_6_months_*` and `..._less_than_3_months_*` |
| `marginal_cultivators_females` | integer |  | Worked less than 6 months, with the same four categories (`marginal_cultivators_*` ...) and split by duration: `..._3_to_6_months_*` and `..._less_than_3_months_*` |
| `marginal_agricultural_labourers_persons` | integer |  |  |
| `marginal_agricultural_labourers_males` | integer |  |  |
| `marginal_agricultural_labourers_females` | integer |  |  |
| `marginal_household_industry_workers_persons` | integer |  |  |
| `marginal_household_industry_workers_males` | integer |  |  |
| `marginal_household_industry_workers_females` | integer |  |  |
| `marginal_other_workers_persons` | integer |  |  |
| `marginal_other_workers_males` | integer |  |  |
| `marginal_other_workers_females` | integer |  |  |
| `marginal_workers_3_to_6_months_persons` | integer |  | Worked less than 6 months, with the same four categories (`marginal_cultivators_*` ...) and split by duration: `..._3_to_6_months_*` and `..._less_than_3_months_*` |
| `marginal_workers_3_to_6_months_males` | integer |  | Worked less than 6 months, with the same four categories (`marginal_cultivators_*` ...) and split by duration: `..._3_to_6_months_*` and `..._less_than_3_months_*` |
| `marginal_workers_3_to_6_months_females` | integer |  | Worked less than 6 months, with the same four categories (`marginal_cultivators_*` ...) and split by duration: `..._3_to_6_months_*` and `..._less_than_3_months_*` |
| `marginal_cultivators_3_to_6_months_persons` | integer |  | Worked less than 6 months, with the same four categories (`marginal_cultivators_*` ...) and split by duration: `..._3_to_6_months_*` and `..._less_than_3_months_*` |
| `marginal_cultivators_3_to_6_months_males` | integer |  | Worked less than 6 months, with the same four categories (`marginal_cultivators_*` ...) and split by duration: `..._3_to_6_months_*` and `..._less_than_3_months_*` |
| `marginal_cultivators_3_to_6_months_females` | integer |  | Worked less than 6 months, with the same four categories (`marginal_cultivators_*` ...) and split by duration: `..._3_to_6_months_*` and `..._less_than_3_months_*` |
| `marginal_agricultural_labourers_3_to_6_months_persons` | integer |  | Worked less than 6 months, with the same four categories (`marginal_cultivators_*` ...) and split by duration: `..._3_to_6_months_*` and `..._less_than_3_months_*` |
| `marginal_agricultural_labourers_3_to_6_months_males` | integer |  | Worked less than 6 months, with the same four categories (`marginal_cultivators_*` ...) and split by duration: `..._3_to_6_months_*` and `..._less_than_3_months_*` |
| `marginal_agricultural_labourers_3_to_6_months_females` | integer |  | Worked less than 6 months, with the same four categories (`marginal_cultivators_*` ...) and split by duration: `..._3_to_6_months_*` and `..._less_than_3_months_*` |
| `marginal_household_industry_workers_3_to_6_months_persons` | integer |  | Worked less than 6 months, with the same four categories (`marginal_cultivators_*` ...) and split by duration: `..._3_to_6_months_*` and `..._less_than_3_months_*` |
| `marginal_household_industry_workers_3_to_6_months_males` | integer |  | Worked less than 6 months, with the same four categories (`marginal_cultivators_*` ...) and split by duration: `..._3_to_6_months_*` and `..._less_than_3_months_*` |
| `marginal_household_industry_workers_3_to_6_months_females` | integer |  | Worked less than 6 months, with the same four categories (`marginal_cultivators_*` ...) and split by duration: `..._3_to_6_months_*` and `..._less_than_3_months_*` |
| `marginal_other_workers_3_to_6_months_persons` | integer |  | Worked less than 6 months, with the same four categories (`marginal_cultivators_*` ...) and split by duration: `..._3_to_6_months_*` and `..._less_than_3_months_*` |
| `marginal_other_workers_3_to_6_months_males` | integer |  | Worked less than 6 months, with the same four categories (`marginal_cultivators_*` ...) and split by duration: `..._3_to_6_months_*` and `..._less_than_3_months_*` |
| `marginal_other_workers_3_to_6_months_females` | integer |  | Worked less than 6 months, with the same four categories (`marginal_cultivators_*` ...) and split by duration: `..._3_to_6_months_*` and `..._less_than_3_months_*` |
| `marginal_workers_less_than_3_months_persons` | integer |  | Worked less than 6 months, with the same four categories (`marginal_cultivators_*` ...) and split by duration: `..._3_to_6_months_*` and `..._less_than_3_months_*` |
| `marginal_workers_less_than_3_months_males` | integer |  | Worked less than 6 months, with the same four categories (`marginal_cultivators_*` ...) and split by duration: `..._3_to_6_months_*` and `..._less_than_3_months_*` |
| `marginal_workers_less_than_3_months_females` | integer |  | Worked less than 6 months, with the same four categories (`marginal_cultivators_*` ...) and split by duration: `..._3_to_6_months_*` and `..._less_than_3_months_*` |
| `marginal_cultivators_less_than_3_months_persons` | integer |  | Worked less than 6 months, with the same four categories (`marginal_cultivators_*` ...) and split by duration: `..._3_to_6_months_*` and `..._less_than_3_months_*` |
| `marginal_cultivators_less_than_3_months_males` | integer |  | Worked less than 6 months, with the same four categories (`marginal_cultivators_*` ...) and split by duration: `..._3_to_6_months_*` and `..._less_than_3_months_*` |
| `marginal_cultivators_less_than_3_months_females` | integer |  | Worked less than 6 months, with the same four categories (`marginal_cultivators_*` ...) and split by duration: `..._3_to_6_months_*` and `..._less_than_3_months_*` |
| `marginal_agricultural_labourers_less_than_3_months_persons` | integer |  | Worked less than 6 months, with the same four categories (`marginal_cultivators_*` ...) and split by duration: `..._3_to_6_months_*` and `..._less_than_3_months_*` |
| `marginal_agricultural_labourers_less_than_3_months_males` | integer |  | Worked less than 6 months, with the same four categories (`marginal_cultivators_*` ...) and split by duration: `..._3_to_6_months_*` and `..._less_than_3_months_*` |
| `marginal_agricultural_labourers_less_than_3_months_females` | integer |  | Worked less than 6 months, with the same four categories (`marginal_cultivators_*` ...) and split by duration: `..._3_to_6_months_*` and `..._less_than_3_months_*` |
| `marginal_household_industry_workers_less_than_3_months_persons` | integer |  | Worked less than 6 months, with the same four categories (`marginal_cultivators_*` ...) and split by duration: `..._3_to_6_months_*` and `..._less_than_3_months_*` |
| `marginal_household_industry_workers_less_than_3_months_males` | integer |  | Worked less than 6 months, with the same four categories (`marginal_cultivators_*` ...) and split by duration: `..._3_to_6_months_*` and `..._less_than_3_months_*` |
| `marginal_household_industry_workers_less_than_3_months_females` | integer |  | Worked less than 6 months, with the same four categories (`marginal_cultivators_*` ...) and split by duration: `..._3_to_6_months_*` and `..._less_than_3_months_*` |
| `marginal_other_workers_less_than_3_months_persons` | integer |  | Worked less than 6 months, with the same four categories (`marginal_cultivators_*` ...) and split by duration: `..._3_to_6_months_*` and `..._less_than_3_months_*` |
| `marginal_other_workers_less_than_3_months_males` | integer |  | Worked less than 6 months, with the same four categories (`marginal_cultivators_*` ...) and split by duration: `..._3_to_6_months_*` and `..._less_than_3_months_*` |
| `marginal_other_workers_less_than_3_months_females` | integer |  | Worked less than 6 months, with the same four categories (`marginal_cultivators_*` ...) and split by duration: `..._3_to_6_months_*` and `..._less_than_3_months_*` |
| `non_workers_persons` | integer |  | Did not work in the year |
| `non_workers_males` | integer |  | Did not work in the year |
| `non_workers_females` | integer |  | Did not work in the year |

Units are read from the column name (warehouse convention). Empty cells (`null` in JSON) mean no value.

## Notes from the warehouse

These describe the full warehouse table (all states).

- Workers by category are the Census's closest measure of outdoor work: cultivators and agricultural labourers work outdoors; "other workers" mixes indoor and outdoor jobs (construction, transport, street vending are inside it). For job-level detail on Nagpur see `LAB_plfs-persons-nagpur_2025_MH_MOSPI_DIST`.
- Districts are the 640 districts of 2011. Later splits are not reflected.
- `lgd_state_code` and `lgd_district_code` added on 5 Nov 2026 from the LGD directory (see [`_reference/README.md`](https://github.com/sarveshkant2003-afk/bharatnomy-data/tree/cd7ce2d673103cc0e606e3cc37e49a9ae75f849a/_reference/README.md)). LGD codes identify today's state or district; for years before a split (Telangana 2014, Ladakh 2019, new districts) the same code covers a larger area than it does now.

## Where this comes from

- Warehouse folder [`POP_census-pca_2011_STATES_ORGI_DIST`](https://github.com/sarveshkant2003-afk/bharatnomy-data/tree/cd7ce2d673103cc0e606e3cc37e49a9ae75f849a/POP_census-pca_2011_STATES_ORGI_DIST) at commit `cd7ce2d67310`
- Filtered to `lgd_state_code` and cleaned by `build.py` in this repo. Files: `POP_census-pca_2011_MH_ORGI_DIST.csv`, `POP_census-pca_2011_MH_ORGI_DIST.json`.
