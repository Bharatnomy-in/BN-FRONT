# Main workers by industry, age and sex, every district of India, 2011 — Maharashtra

Number of main workers (people who worked 6 months or more in the year) in each industry, by age group and sex, total / rural / urban, for every district, state and India. Census 2011 table B-04. Its **mining and quarrying** column is the closest district-level count of the coal-mining workforce (see Notes), and **electricity, gas and water** covers power-plant and utility jobs.

## Coverage

- **Rows:** 1,470
- **Period:** 2011
- **Districts:** 35 of 36
- 42 state-total row(s) from the warehouse table are left out; add up district rows instead.

## Source

- **Data:** Office of the Registrar General & Census Commissioner, India (ORGI), Census of India 2011, table B-04 "Main workers classified by age, industrial category and sex" (one file per state/UT plus India, `DDW-B04-<state>00.xls`)
- **Link:** https://censusindia.gov.in/nada/index.php/catalog (catalog ids 43036-43071, idno `PC11_B04-<state>`; e.g. Jharkhand: https://censusindia.gov.in/nada/index.php/catalog/43056)
- **Downloaded:** 18 Nov 2026
- **Original files:** [`_sources/orgi-census2011/raw/b04/`](https://github.com/sarveshkant2003-afk/bharatnomy-data/tree/41650b8bb1975a4f4e082ba172d8b5dfb8f7db8a/_sources/orgi-census2011/raw/b04/) (36 files, 15 MB); catalog ids in [`raw/orgi-census2011_b04-catalog-ids_2011.tsv`](https://github.com/sarveshkant2003-afk/bharatnomy-data/tree/41650b8bb1975a4f4e082ba172d8b5dfb8f7db8a/_sources/orgi-census2011/raw/orgi-census2011_b04-catalog-ids_2011.tsv)
- **Scripts:** [`pipelines/orgi-census2011/fetch_b04.sh`](https://github.com/sarveshkant2003-afk/bharatnomy-data/tree/41650b8bb1975a4f4e082ba172d8b5dfb8f7db8a/pipelines/orgi-census2011/fetch_b04.sh), [`build_b04.py`](https://github.com/sarveshkant2003-afk/bharatnomy-data/tree/41650b8bb1975a4f4e082ba172d8b5dfb8f7db8a/pipelines/orgi-census2011/build_b04.py)

## Columns

| Column | Type | Unit | Description |
|---|---|---|---|
| `state_ut` | text |  | District rows: today's state and LGD code (from [`_reference/geography.csv`](https://github.com/sarveshkant2003-afk/bharatnomy-data/tree/41650b8bb1975a4f4e082ba172d8b5dfb8f7db8a/_reference/geography.csv)). `State total` rows: the state **as in 2011** (see Notes). `All India` row: blank code |
| `lgd_state_code` | text |  | District rows: today's state and LGD code (from [`_reference/geography.csv`](https://github.com/sarveshkant2003-afk/bharatnomy-data/tree/41650b8bb1975a4f4e082ba172d8b5dfb8f7db8a/_reference/geography.csv)). `State total` rows: the state **as in 2011** (see Notes). `All India` row: blank code |
| `state_census_code` | text |  | Census 2011 state code (`00` = India) |
| `district` | text |  | District by today's name and LGD code; `State total` for the state's published total, blank on the India row. LGD code blank for Mahe and Yanam (Puducherry regions LGD does not list as districts) |
| `lgd_district_code` | text |  | District by today's name and LGD code; `State total` for the state's published total, blank on the India row. LGD code blank for Mahe and Yanam (Puducherry regions LGD does not list as districts) |
| `district_census_code` | text |  | Census 2011 district code and name as printed |
| `district_census_name` | text |  | Census 2011 district code and name as printed |
| `residence` | text |  | `Total`, `Rural` or `Urban` |
| `age_group` | text |  | `Total`, `5-9`, `10-14`, ... `70-79`, `80+`, `Age not stated` |
| `main_workers_total_persons` | integer |  | All main workers |
| `main_workers_total_males` | integer |  | All main workers |
| `main_workers_total_females` | integer |  | All main workers |
| `a_cultivators_persons` | integer |  | NIC section A: agriculture, split as the Census prints it |
| `a_cultivators_males` | integer |  | NIC section A: agriculture, split as the Census prints it |
| `a_cultivators_females` | integer |  | NIC section A: agriculture, split as the Census prints it |
| `a_agricultural_labourers_persons` | integer |  | NIC section A: agriculture, split as the Census prints it |
| `a_agricultural_labourers_males` | integer |  | NIC section A: agriculture, split as the Census prints it |
| `a_agricultural_labourers_females` | integer |  | NIC section A: agriculture, split as the Census prints it |
| `a_plantation_livestock_forestry_fishing_persons` | integer |  | NIC section A: agriculture, split as the Census prints it |
| `a_plantation_livestock_forestry_fishing_males` | integer |  | NIC section A: agriculture, split as the Census prints it |
| `a_plantation_livestock_forestry_fishing_females` | integer |  | NIC section A: agriculture, split as the Census prints it |
| `b_mining_quarrying_persons` | integer |  | NIC section B: mining and quarrying (coal and lignite, crude oil and gas, metal ores, stone, sand, other minerals) |
| `b_mining_quarrying_males` | integer |  | NIC section B: mining and quarrying (coal and lignite, crude oil and gas, metal ores, stone, sand, other minerals) |
| `b_mining_quarrying_females` | integer |  | NIC section B: mining and quarrying (coal and lignite, crude oil and gas, metal ores, stone, sand, other minerals) |
| `c_manufacturing_hhi_persons` | integer |  | NIC section C: manufacturing, in household industry (HHI) and outside it |
| `c_manufacturing_hhi_males` | integer |  | NIC section C: manufacturing, in household industry (HHI) and outside it |
| `c_manufacturing_hhi_females` | integer |  | NIC section C: manufacturing, in household industry (HHI) and outside it |
| `c_manufacturing_non_hhi_persons` | integer |  | NIC section C: manufacturing, in household industry (HHI) and outside it |
| `c_manufacturing_non_hhi_males` | integer |  | NIC section C: manufacturing, in household industry (HHI) and outside it |
| `c_manufacturing_non_hhi_females` | integer |  | NIC section C: manufacturing, in household industry (HHI) and outside it |
| `d_e_electricity_gas_water_waste_persons` | integer |  | NIC sections D and E: electricity, gas, steam and air conditioning supply; water supply, sewerage and waste management |
| `d_e_electricity_gas_water_waste_males` | integer |  | NIC sections D and E: electricity, gas, steam and air conditioning supply; water supply, sewerage and waste management |
| `d_e_electricity_gas_water_waste_females` | integer |  | NIC sections D and E: electricity, gas, steam and air conditioning supply; water supply, sewerage and waste management |
| `f_construction_persons` | integer |  | NIC section F |
| `f_construction_males` | integer |  | NIC section F |
| `f_construction_females` | integer |  | NIC section F |
| `g_trade_repair_hhi_persons` | integer |  | NIC section G: wholesale and retail trade, repair of motor vehicles, HHI / non-HHI |
| `g_trade_repair_hhi_males` | integer |  | NIC section G: wholesale and retail trade, repair of motor vehicles, HHI / non-HHI |
| `g_trade_repair_hhi_females` | integer |  | NIC section G: wholesale and retail trade, repair of motor vehicles, HHI / non-HHI |
| `g_trade_repair_non_hhi_persons` | integer |  | NIC section G: wholesale and retail trade, repair of motor vehicles, HHI / non-HHI |
| `g_trade_repair_non_hhi_males` | integer |  | NIC section G: wholesale and retail trade, repair of motor vehicles, HHI / non-HHI |
| `g_trade_repair_non_hhi_females` | integer |  | NIC section G: wholesale and retail trade, repair of motor vehicles, HHI / non-HHI |
| `h_transport_storage_persons` | integer |  | NIC sections H and I |
| `h_transport_storage_males` | integer |  | NIC sections H and I |
| `h_transport_storage_females` | integer |  | NIC sections H and I |
| `i_accommodation_food_persons` | integer |  | NIC sections H and I |
| `i_accommodation_food_males` | integer |  | NIC sections H and I |
| `i_accommodation_food_females` | integer |  | NIC sections H and I |
| `j_information_communication_hhi_persons` | integer |  | NIC section J, HHI / non-HHI (as printed) |
| `j_information_communication_hhi_males` | integer |  | NIC section J, HHI / non-HHI (as printed) |
| `j_information_communication_hhi_females` | integer |  | NIC section J, HHI / non-HHI (as printed) |
| `j_information_communication_non_hhi_persons` | integer |  | NIC section J, HHI / non-HHI (as printed) |
| `j_information_communication_non_hhi_males` | integer |  | NIC section J, HHI / non-HHI (as printed) |
| `j_information_communication_non_hhi_females` | integer |  | NIC section J, HHI / non-HHI (as printed) |
| `k_to_m_finance_real_estate_professional_persons` | integer |  | NIC sections K to M: finance and insurance, real estate, professional, scientific and technical |
| `k_to_m_finance_real_estate_professional_males` | integer |  | NIC sections K to M: finance and insurance, real estate, professional, scientific and technical |
| `k_to_m_finance_real_estate_professional_females` | integer |  | NIC sections K to M: finance and insurance, real estate, professional, scientific and technical |
| `n_to_o_administrative_public_administration_persons` | integer |  | NIC sections N and O: administrative and support services; public administration and defence |
| `n_to_o_administrative_public_administration_males` | integer |  | NIC sections N and O: administrative and support services; public administration and defence |
| `n_to_o_administrative_public_administration_females` | integer |  | NIC sections N and O: administrative and support services; public administration and defence |
| `p_to_q_education_health_persons` | integer |  | NIC sections P and Q |
| `p_to_q_education_health_males` | integer |  | NIC sections P and Q |
| `p_to_q_education_health_females` | integer |  | NIC sections P and Q |
| `r_to_u_other_services_hhi_persons` | integer |  | NIC sections R to U: arts, other services, households as employers, extra-territorial bodies, HHI / non-HHI |
| `r_to_u_other_services_hhi_males` | integer |  | NIC sections R to U: arts, other services, households as employers, extra-territorial bodies, HHI / non-HHI |
| `r_to_u_other_services_hhi_females` | integer |  | NIC sections R to U: arts, other services, households as employers, extra-territorial bodies, HHI / non-HHI |
| `r_to_u_other_services_non_hhi_persons` | integer |  | NIC sections R to U: arts, other services, households as employers, extra-territorial bodies, HHI / non-HHI |
| `r_to_u_other_services_non_hhi_males` | integer |  | NIC sections R to U: arts, other services, households as employers, extra-territorial bodies, HHI / non-HHI |
| `r_to_u_other_services_non_hhi_females` | integer |  | NIC sections R to U: arts, other services, households as employers, extra-territorial bodies, HHI / non-HHI |

Units are read from the column name (warehouse convention). Empty cells (`null` in JSON) mean no value.

## Notes from the warehouse

These describe the full warehouse table (all states).

- **Mining is not coal alone.** The Census does not split section B by mineral at district level. In the coal belt (e.g. Dhanbad 83,813 mining workers, 15.3% of all main workers; Chandrapur, Karimnagar, Barddhaman, Korba, Angul, Singrauli) it is mostly coal; elsewhere it can be stone, sand, iron ore or oil (e.g. Pakur, 10.2%, is mainly stone quarrying; Jodhpur is sandstone). Cuddalore's is mostly Neyveli lignite.
- **Main workers only.** Marginal workers (less than 6 months' work) are not in this table, so it understates seasonal and informal mining work.
- **The printed header gives only section letters** (A, B, C, D & E, ...); the column names add the standard NIC 2008 section titles.
- **2011 geography.** District rows are the 640 districts of 2011 with today's names, LGD codes and states, so a 2011 Andhra Pradesh district now in Telangana has `state_ut` = Telangana. `State total` rows are the 35 states/UTs of 2011 as published: the Andhra Pradesh total includes today's Telangana, Jammu & Kashmir includes Ladakh, and Dadra & Nagar Haveli and Daman & Diu are separate. Add up district rows by `lgd_state_code` for today's states. Districts created after 2011 are inside their parent (e.g. 2011 Barddhaman is shown as Purba Bardhaman, but it includes today's Paschim Bardhaman, the Raniganj-Asansol coalfield).
- Checks (18 Nov 2026): 28,392 rows = (640 districts + 35 states + India) x Total/Rural/Urban x 14 age groups, minus places with no rural or urban population; no duplicate keys; no negative counts; persons = males + females everywhere; the industry columns add up to `main_workers_total` exactly in every row; rural + urban = total; age groups add up to `Total`; districts add up to their `State total` and the states to `All India` exactly. India: 362,611,115 main workers, of whom 1,801,326 in mining and quarrying and 1,866,613 in electricity, gas and water.

## Where this comes from

- Warehouse folder [`LAB_main-workers-by-industry_2011_STATES_ORGI_DIST`](https://github.com/sarveshkant2003-afk/bharatnomy-data/tree/41650b8bb1975a4f4e082ba172d8b5dfb8f7db8a/LAB_main-workers-by-industry_2011_STATES_ORGI_DIST) at commit `41650b8bb197`
- Filtered to `lgd_state_code` and cleaned by `build.py` in this repo. Files: `LAB_main-workers-by-industry_2011_MH_ORGI_DIST.csv`, `LAB_main-workers-by-industry_2011_MH_ORGI_DIST.json`.
