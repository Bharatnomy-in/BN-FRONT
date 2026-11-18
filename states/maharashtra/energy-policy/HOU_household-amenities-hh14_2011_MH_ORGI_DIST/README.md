# Household amenities and assets by district, Maharashtra, 2011 — Maharashtra

Share of households by condition and material of the house (roof, wall, floor), rooms, size, ownership, drinking water source and location, lighting, latrine, bathing, drainage, cooking fuel, kitchen, banking and assets, for every district of Maharashtra, total / rural / urban. All 135 indicators of Census 2011 table HH-14. This is the district rows of [`HOU_household-amenities-hh14_2011_MH_ORGI_SDT`](https://github.com/sarveshkant2003-afk/bharatnomy-data/tree/930603697458e4ad288a0344bcd0c4c001d4462c/HOU_household-amenities-hh14_2011_MH_ORGI_SDT/) (which also has the tehsils), kept as its own table so district-level users and the front repo can use it directly. It covers the household energy-access variables: main source of lighting (electricity) and main cooking fuel (LPG/PNG, firewood, crop residue, cowdung, coal, kerosene, electricity, biogas).

## Coverage

- **Rows:** 103
- **Period:** 2011
- **Districts:** 35 of 36

## Source

- **Data:** Office of the Registrar General & Census Commissioner, India (ORGI), Census of India 2011, Houselisting and Housing Census, table HH-14 "Percentage of households to total households by amenities and assets" (one file per district, `HLPCA-27<district code>-2011_H14_census.xlsx`)
- **Link:** https://censusindia.gov.in/nada/index.php/catalog (catalog ids 9795-9829; e.g. Nagpur: https://censusindia.gov.in/nada/index.php/catalog/9803)
- **Downloaded:** 5 Nov 2026
- **Original files:** [`_sources/orgi-census2011/raw/hl14-mh/`](https://github.com/sarveshkant2003-afk/bharatnomy-data/tree/930603697458e4ad288a0344bcd0c4c001d4462c/_sources/orgi-census2011/raw/hl14-mh/)
- **Scripts:** [`pipelines/orgi-census2011/fetch_hl14_mh.sh`](https://github.com/sarveshkant2003-afk/bharatnomy-data/tree/930603697458e4ad288a0344bcd0c4c001d4462c/pipelines/orgi-census2011/fetch_hl14_mh.sh), [`build_hl14_mh.py`](https://github.com/sarveshkant2003-afk/bharatnomy-data/tree/930603697458e4ad288a0344bcd0c4c001d4462c/pipelines/orgi-census2011/build_hl14_mh.py) (writes this table and the sub-district one)

## Columns

| Column | Type | Unit | Description |
|---|---|---|---|
| `state_ut` | text |  | Maharashtra, 27 |
| `lgd_state_code` | text |  | Maharashtra, 27 |
| `district` | text |  | District by its current name and LGD code (from [`_reference/geography.csv`](https://github.com/sarveshkant2003-afk/bharatnomy-data/tree/930603697458e4ad288a0344bcd0c4c001d4462c/_reference/geography.csv)) |
| `lgd_district_code` | text |  | District by its current name and LGD code (from [`_reference/geography.csv`](https://github.com/sarveshkant2003-afk/bharatnomy-data/tree/930603697458e4ad288a0344bcd0c4c001d4462c/_reference/geography.csv)) |
| `district_census_code` | text |  | Census 2011 district code and name |
| `district_census_name` | text |  | Census 2011 district code and name |
| `residence` | text |  | `Total`, `Rural` or `Urban` |
| `house_condition_total_total_pct` | integer | % | Households by condition of the census house (`good`, `livable`, `dilapidated`, `total`), for all houses (`total`), houses used only as residence (`residence`) and residence-cum-other use, % of households |
| `house_condition_total_good_pct` | number | % | Households by condition of the census house (`good`, `livable`, `dilapidated`, `total`), for all houses (`total`), houses used only as residence (`residence`) and residence-cum-other use, % of households |
| `house_condition_total_livable_pct` | number | % | Households by condition of the census house (`good`, `livable`, `dilapidated`, `total`), for all houses (`total`), houses used only as residence (`residence`) and residence-cum-other use, % of households |
| `house_condition_total_dilapidated_pct` | number | % | Households by condition of the census house (`good`, `livable`, `dilapidated`, `total`), for all houses (`total`), houses used only as residence (`residence`) and residence-cum-other use, % of households |
| `house_condition_residence_total_pct` | number | % | Households by condition of the census house (`good`, `livable`, `dilapidated`, `total`), for all houses (`total`), houses used only as residence (`residence`) and residence-cum-other use, % of households |
| `house_condition_residence_good_pct` | number | % | Households by condition of the census house (`good`, `livable`, `dilapidated`, `total`), for all houses (`total`), houses used only as residence (`residence`) and residence-cum-other use, % of households |
| `house_condition_residence_livable_pct` | number | % | Households by condition of the census house (`good`, `livable`, `dilapidated`, `total`), for all houses (`total`), houses used only as residence (`residence`) and residence-cum-other use, % of households |
| `house_condition_residence_dilapidated_pct` | number | % | Households by condition of the census house (`good`, `livable`, `dilapidated`, `total`), for all houses (`total`), houses used only as residence (`residence`) and residence-cum-other use, % of households |
| `house_condition_residence_cum_other_use_total_pct` | number | % | Households by condition of the census house (`good`, `livable`, `dilapidated`, `total`), for all houses (`total`), houses used only as residence (`residence`) and residence-cum-other use, % of households |
| `house_condition_residence_cum_other_use_good_pct` | number | % | Households by condition of the census house (`good`, `livable`, `dilapidated`, `total`), for all houses (`total`), houses used only as residence (`residence`) and residence-cum-other use, % of households |
| `house_condition_residence_cum_other_use_livable_pct` | number | % | Households by condition of the census house (`good`, `livable`, `dilapidated`, `total`), for all houses (`total`), houses used only as residence (`residence`) and residence-cum-other use, % of households |
| `house_condition_residence_cum_other_use_dilapidated_pct` | number | % | Households by condition of the census house (`good`, `livable`, `dilapidated`, `total`), for all houses (`total`), houses used only as residence (`residence`) and residence-cum-other use, % of households |
| `roof_grass_thatch_bamboo_wood_mud_etc_pct` | number | % | Households by predominant material of roof / wall / floor, % (e.g. `roof_g_i_metal_asbestos_sheets_pct`, `roof_grass_thatch_bamboo_wood_mud_etc_pct`, `roof_concrete_pct`) |
| `roof_plastic_polythene_pct` | number | % | Households by predominant material of roof / wall / floor, % (e.g. `roof_g_i_metal_asbestos_sheets_pct`, `roof_grass_thatch_bamboo_wood_mud_etc_pct`, `roof_concrete_pct`) |
| `roof_hand_made_tiles_pct` | number | % | Households by predominant material of roof / wall / floor, % (e.g. `roof_g_i_metal_asbestos_sheets_pct`, `roof_grass_thatch_bamboo_wood_mud_etc_pct`, `roof_concrete_pct`) |
| `roof_machine_made_tiles_pct` | number | % | Households by predominant material of roof / wall / floor, % (e.g. `roof_g_i_metal_asbestos_sheets_pct`, `roof_grass_thatch_bamboo_wood_mud_etc_pct`, `roof_concrete_pct`) |
| `roof_burnt_brick_pct` | number | % | Households by predominant material of roof / wall / floor, % (e.g. `roof_g_i_metal_asbestos_sheets_pct`, `roof_grass_thatch_bamboo_wood_mud_etc_pct`, `roof_concrete_pct`) |
| `roof_stone_slate_pct` | number | % | Households by predominant material of roof / wall / floor, % (e.g. `roof_g_i_metal_asbestos_sheets_pct`, `roof_grass_thatch_bamboo_wood_mud_etc_pct`, `roof_concrete_pct`) |
| `roof_g_i_metal_asbestos_sheets_pct` | number | % | Households by predominant material of roof / wall / floor, % (e.g. `roof_g_i_metal_asbestos_sheets_pct`, `roof_grass_thatch_bamboo_wood_mud_etc_pct`, `roof_concrete_pct`) |
| `roof_concrete_pct` | number | % | Households by predominant material of roof / wall / floor, % (e.g. `roof_g_i_metal_asbestos_sheets_pct`, `roof_grass_thatch_bamboo_wood_mud_etc_pct`, `roof_concrete_pct`) |
| `roof_any_other_material_pct` | number | % | Households by predominant material of roof / wall / floor, % (e.g. `roof_g_i_metal_asbestos_sheets_pct`, `roof_grass_thatch_bamboo_wood_mud_etc_pct`, `roof_concrete_pct`) |
| `wall_grass_thatch_bamboo_etc_pct` | number | % | Households by predominant material of roof / wall / floor, % (e.g. `roof_g_i_metal_asbestos_sheets_pct`, `roof_grass_thatch_bamboo_wood_mud_etc_pct`, `roof_concrete_pct`) |
| `wall_plastic_polythene_pct` | number | % | Households by predominant material of roof / wall / floor, % (e.g. `roof_g_i_metal_asbestos_sheets_pct`, `roof_grass_thatch_bamboo_wood_mud_etc_pct`, `roof_concrete_pct`) |
| `wall_mud_unburnt_brick_pct` | number | % | Households by predominant material of roof / wall / floor, % (e.g. `roof_g_i_metal_asbestos_sheets_pct`, `roof_grass_thatch_bamboo_wood_mud_etc_pct`, `roof_concrete_pct`) |
| `wall_wood_pct` | number | % | Households by predominant material of roof / wall / floor, % (e.g. `roof_g_i_metal_asbestos_sheets_pct`, `roof_grass_thatch_bamboo_wood_mud_etc_pct`, `roof_concrete_pct`) |
| `wall_stone_not_packed_with_mortar_pct` | number | % | Households by predominant material of roof / wall / floor, % (e.g. `roof_g_i_metal_asbestos_sheets_pct`, `roof_grass_thatch_bamboo_wood_mud_etc_pct`, `roof_concrete_pct`) |
| `wall_stone_packed_with_mortar_pct` | number | % | Households by predominant material of roof / wall / floor, % (e.g. `roof_g_i_metal_asbestos_sheets_pct`, `roof_grass_thatch_bamboo_wood_mud_etc_pct`, `roof_concrete_pct`) |
| `wall_g_i_metal_asbestos_sheets_pct` | number | % | Households by predominant material of roof / wall / floor, % (e.g. `roof_g_i_metal_asbestos_sheets_pct`, `roof_grass_thatch_bamboo_wood_mud_etc_pct`, `roof_concrete_pct`) |
| `wall_burnt_brick_pct` | number | % | Households by predominant material of roof / wall / floor, % (e.g. `roof_g_i_metal_asbestos_sheets_pct`, `roof_grass_thatch_bamboo_wood_mud_etc_pct`, `roof_concrete_pct`) |
| `wall_concrete_pct` | number | % | Households by predominant material of roof / wall / floor, % (e.g. `roof_g_i_metal_asbestos_sheets_pct`, `roof_grass_thatch_bamboo_wood_mud_etc_pct`, `roof_concrete_pct`) |
| `wall_any_other_material_pct` | number | % | Households by predominant material of roof / wall / floor, % (e.g. `roof_g_i_metal_asbestos_sheets_pct`, `roof_grass_thatch_bamboo_wood_mud_etc_pct`, `roof_concrete_pct`) |
| `floor_mud_pct` | number | % | Households by predominant material of roof / wall / floor, % (e.g. `roof_g_i_metal_asbestos_sheets_pct`, `roof_grass_thatch_bamboo_wood_mud_etc_pct`, `roof_concrete_pct`) |
| `floor_wood_bamboo_pct` | number | % | Households by predominant material of roof / wall / floor, % (e.g. `roof_g_i_metal_asbestos_sheets_pct`, `roof_grass_thatch_bamboo_wood_mud_etc_pct`, `roof_concrete_pct`) |
| `floor_burnt_brick_pct` | number | % | Households by predominant material of roof / wall / floor, % (e.g. `roof_g_i_metal_asbestos_sheets_pct`, `roof_grass_thatch_bamboo_wood_mud_etc_pct`, `roof_concrete_pct`) |
| `floor_stone_pct` | number | % | Households by predominant material of roof / wall / floor, % (e.g. `roof_g_i_metal_asbestos_sheets_pct`, `roof_grass_thatch_bamboo_wood_mud_etc_pct`, `roof_concrete_pct`) |
| `floor_cement_pct` | number | % | Households by predominant material of roof / wall / floor, % (e.g. `roof_g_i_metal_asbestos_sheets_pct`, `roof_grass_thatch_bamboo_wood_mud_etc_pct`, `roof_concrete_pct`) |
| `floor_mosaic_floor_tiles_pct` | number | % | Households by predominant material of roof / wall / floor, % (e.g. `roof_g_i_metal_asbestos_sheets_pct`, `roof_grass_thatch_bamboo_wood_mud_etc_pct`, `roof_concrete_pct`) |
| `floor_any_other_material_pct` | number | % | Households by predominant material of roof / wall / floor, % (e.g. `roof_g_i_metal_asbestos_sheets_pct`, `roof_grass_thatch_bamboo_wood_mud_etc_pct`, `roof_concrete_pct`) |
| `dwelling_rooms_no_exclusive_room_pct` | number | % | Households by number of dwelling rooms, persons, married couples, % |
| `dwelling_rooms_one_room_pct` | number | % | Households by number of dwelling rooms, persons, married couples, % |
| `dwelling_rooms_two_rooms_pct` | number | % | Households by number of dwelling rooms, persons, married couples, % |
| `dwelling_rooms_three_rooms_pct` | number | % | Households by number of dwelling rooms, persons, married couples, % |
| `dwelling_rooms_four_rooms_pct` | number | % | Households by number of dwelling rooms, persons, married couples, % |
| `dwelling_rooms_five_rooms_pct` | number | % | Households by number of dwelling rooms, persons, married couples, % |
| `dwelling_rooms_six_rooms_and_above_pct` | number | % | Households by number of dwelling rooms, persons, married couples, % |
| `household_size_1_pct` | number | % | Households by number of dwelling rooms, persons, married couples, % |
| `household_size_2_pct` | number | % | Households by number of dwelling rooms, persons, married couples, % |
| `household_size_3_pct` | number | % | Households by number of dwelling rooms, persons, married couples, % |
| `household_size_4_pct` | number | % | Households by number of dwelling rooms, persons, married couples, % |
| `household_size_5_pct` | number | % | Households by number of dwelling rooms, persons, married couples, % |
| `household_size_6_to_8_pct` | number | % | Households by number of dwelling rooms, persons, married couples, % |
| `household_size_9_plus_pct` | number | % | Households by number of dwelling rooms, persons, married couples, % |
| `ownership_owned_pct` | number | % | Ownership of the house, % |
| `ownership_rented_pct` | number | % | Ownership of the house, % |
| `ownership_any_others_pct` | number | % | Ownership of the house, % |
| `married_couples_none_pct` | number | % | Households by number of dwelling rooms, persons, married couples, % |
| `married_couples_1_pct` | number | % | Households by number of dwelling rooms, persons, married couples, % |
| `married_couples_2_pct` | number | % | Households by number of dwelling rooms, persons, married couples, % |
| `married_couples_3_pct` | number | % | Households by number of dwelling rooms, persons, married couples, % |
| `married_couples_4_pct` | number | % | Households by number of dwelling rooms, persons, married couples, % |
| `married_couples_5_plus_pct` | number | % | Households by number of dwelling rooms, persons, married couples, % |
| `drinking_water_source_tapwater_from_treated_source_pct` | number | % | Main source of drinking water (treated / untreated tap water, wells, handpump, tubewell, spring, river, tank, other), % |
| `drinking_water_source_tapwater_from_un_treated_source_pct` | number | % | Main source of drinking water (treated / untreated tap water, wells, handpump, tubewell, spring, river, tank, other), % |
| `drinking_water_source_covered_well_pct` | number | % | Main source of drinking water (treated / untreated tap water, wells, handpump, tubewell, spring, river, tank, other), % |
| `drinking_water_source_un_covered_well_pct` | number | % | Main source of drinking water (treated / untreated tap water, wells, handpump, tubewell, spring, river, tank, other), % |
| `drinking_water_source_handpump_pct` | number | % | Main source of drinking water (treated / untreated tap water, wells, handpump, tubewell, spring, river, tank, other), % |
| `drinking_water_source_tubewell_borehole_pct` | number | % | Main source of drinking water (treated / untreated tap water, wells, handpump, tubewell, spring, river, tank, other), % |
| `drinking_water_source_spring_pct` | number | % | Main source of drinking water (treated / untreated tap water, wells, handpump, tubewell, spring, river, tank, other), % |
| `drinking_water_source_river_canal_pct` | number | % | Main source of drinking water (treated / untreated tap water, wells, handpump, tubewell, spring, river, tank, other), % |
| `drinking_water_source_tank_pond_lake_pct` | number | % | Main source of drinking water (treated / untreated tap water, wells, handpump, tubewell, spring, river, tank, other), % |
| `drinking_water_source_other_sources_pct` | number | % | Main source of drinking water (treated / untreated tap water, wells, handpump, tubewell, spring, river, tank, other), % |
| `drinking_water_location_within_premises_pct` | number | % | Location of the drinking water source, % |
| `drinking_water_location_near_premises_pct` | number | % | Location of the drinking water source, % |
| `drinking_water_location_away_pct` | number | % | Location of the drinking water source, % |
| `lighting_electricity_pct` | number | % | Main source of lighting (electricity, kerosene, solar, other oil, any other, none), % |
| `lighting_kerosene_pct` | number | % | Main source of lighting (electricity, kerosene, solar, other oil, any other, none), % |
| `lighting_solar_energy_pct` | number | % | Main source of lighting (electricity, kerosene, solar, other oil, any other, none), % |
| `lighting_other_oil_pct` | number | % | Main source of lighting (electricity, kerosene, solar, other oil, any other, none), % |
| `lighting_any_other_pct` | number | % | Main source of lighting (electricity, kerosene, solar, other oil, any other, none), % |
| `lighting_no_lighting_pct` | number | % | Main source of lighting (electricity, kerosene, solar, other oil, any other, none), % |
| `latrine_within_premises_total_pct` | number | % | Households with a latrine within the premises, and by type, % |
| `latrine_flush_piped_sewer_pct` | number | % | Households with a latrine within the premises, and by type, % |
| `latrine_flush_septic_tank_pct` | number | % | Households with a latrine within the premises, and by type, % |
| `latrine_flush_other_system_pct` | number | % | Households with a latrine within the premises, and by type, % |
| `latrine_pit_with_slab_pct` | number | % | Households with a latrine within the premises, and by type, % |
| `latrine_pit_without_slab_pct` | number | % | Households with a latrine within the premises, and by type, % |
| `latrine_night_soil_open_drain_pct` | number | % | Households with a latrine within the premises, and by type, % |
| `latrine_service_removed_by_human_pct` | number | % | Households with a latrine within the premises, and by type, % |
| `latrine_service_serviced_by_animal_pct` | number | % | Households with a latrine within the premises, and by type, % |
| `latrine_none_within_premises_total_pct` | number | % | Households without a latrine within the premises, and what they use instead, % |
| `latrine_none_public_latrine_pct` | number | % | Households without a latrine within the premises, and what they use instead, % |
| `latrine_none_open_pct` | number | % | Households without a latrine within the premises, and what they use instead, % |
| `bathing_within_premises_bathroom_pct` | number | % | Bathing facility within premises (bathroom / enclosure without roof / none); waste water outlet (closed / open / no drainage), % |
| `bathing_within_premises_enclosure_without_roof_pct` | number | % | Bathing facility within premises (bathroom / enclosure without roof / none); waste water outlet (closed / open / no drainage), % |
| `bathing_none_within_premises_pct` | number | % | Bathing facility within premises (bathroom / enclosure without roof / none); waste water outlet (closed / open / no drainage), % |
| `waste_water_closed_drainage_pct` | number | % | Bathing facility within premises (bathroom / enclosure without roof / none); waste water outlet (closed / open / no drainage), % |
| `waste_water_open_drainage_pct` | number | % | Bathing facility within premises (bathroom / enclosure without roof / none); waste water outlet (closed / open / no drainage), % |
| `waste_water_no_drainage_pct` | number | % | Bathing facility within premises (bathroom / enclosure without roof / none); waste water outlet (closed / open / no drainage), % |
| `cooking_fuel_fire_wood_pct` | number | % | Fuel used for cooking (fire-wood, crop residue, cowdung cake, coal, kerosene, LPG/PNG, electricity, biogas, other, no cooking), % |
| `cooking_fuel_crop_residue_pct` | number | % | Fuel used for cooking (fire-wood, crop residue, cowdung cake, coal, kerosene, LPG/PNG, electricity, biogas, other, no cooking), % |
| `cooking_fuel_cowdung_cake_pct` | number | % | Fuel used for cooking (fire-wood, crop residue, cowdung cake, coal, kerosene, LPG/PNG, electricity, biogas, other, no cooking), % |
| `cooking_fuel_coal_lignite_charcoal_pct` | number | % | Fuel used for cooking (fire-wood, crop residue, cowdung cake, coal, kerosene, LPG/PNG, electricity, biogas, other, no cooking), % |
| `cooking_fuel_kerosene_pct` | number | % | Fuel used for cooking (fire-wood, crop residue, cowdung cake, coal, kerosene, LPG/PNG, electricity, biogas, other, no cooking), % |
| `cooking_fuel_lpg_png_pct` | number | % | Fuel used for cooking (fire-wood, crop residue, cowdung cake, coal, kerosene, LPG/PNG, electricity, biogas, other, no cooking), % |
| `cooking_fuel_electricity_pct` | number | % | Fuel used for cooking (fire-wood, crop residue, cowdung cake, coal, kerosene, LPG/PNG, electricity, biogas, other, no cooking), % |
| `cooking_fuel_biogas_pct` | number | % | Fuel used for cooking (fire-wood, crop residue, cowdung cake, coal, kerosene, LPG/PNG, electricity, biogas, other, no cooking), % |
| `cooking_fuel_any_other_pct` | number | % | Fuel used for cooking (fire-wood, crop residue, cowdung cake, coal, kerosene, LPG/PNG, electricity, biogas, other, no cooking), % |
| `cooking_fuel_no_cooking_pct` | number | % | Fuel used for cooking (fire-wood, crop residue, cowdung cake, coal, kerosene, LPG/PNG, electricity, biogas, other, no cooking), % |
| `kitchen_total_pct` | integer | % | Cooking inside / outside the house, with or without a kitchen, % |
| `kitchen_cooking_inside_total_pct` | number | % | Cooking inside / outside the house, with or without a kitchen, % |
| `kitchen_cooking_inside_has_kitchen_pct` | number | % | Cooking inside / outside the house, with or without a kitchen, % |
| `kitchen_cooking_inside_no_kitchen_pct` | number | % | Cooking inside / outside the house, with or without a kitchen, % |
| `kitchen_cooking_outside_total_pct` | number | % | Cooking inside / outside the house, with or without a kitchen, % |
| `kitchen_cooking_outside_has_kitchen_pct` | number | % | Cooking inside / outside the house, with or without a kitchen, % |
| `kitchen_cooking_outside_no_kitchen_pct` | number | % | Cooking inside / outside the house, with or without a kitchen, % |
| `kitchen_no_cooking_pct` | number | % | Cooking inside / outside the house, with or without a kitchen, % |
| `banking_services_availed_pct` | number | % | Households availing banking services, % |
| `assets_radio_transistor_pct` | number | % | Households with radio, TV, computer (with / without internet), phone (landline / mobile / both), bicycle, two-wheeler, car, all of TV-computer-phone-vehicle, none of these, % |
| `assets_television_pct` | number | % | Households with radio, TV, computer (with / without internet), phone (landline / mobile / both), bicycle, two-wheeler, car, all of TV-computer-phone-vehicle, none of these, % |
| `assets_computer_with_internet_pct` | number | % | Households with radio, TV, computer (with / without internet), phone (landline / mobile / both), bicycle, two-wheeler, car, all of TV-computer-phone-vehicle, none of these, % |
| `assets_computer_without_internet_pct` | number | % | Households with radio, TV, computer (with / without internet), phone (landline / mobile / both), bicycle, two-wheeler, car, all of TV-computer-phone-vehicle, none of these, % |
| `assets_phone_landline_only_pct` | number | % | Households with radio, TV, computer (with / without internet), phone (landline / mobile / both), bicycle, two-wheeler, car, all of TV-computer-phone-vehicle, none of these, % |
| `assets_phone_mobile_only_pct` | number | % | Households with radio, TV, computer (with / without internet), phone (landline / mobile / both), bicycle, two-wheeler, car, all of TV-computer-phone-vehicle, none of these, % |
| `assets_phone_both_pct` | number | % | Households with radio, TV, computer (with / without internet), phone (landline / mobile / both), bicycle, two-wheeler, car, all of TV-computer-phone-vehicle, none of these, % |
| `assets_bicycle_pct` | number | % | Households with radio, TV, computer (with / without internet), phone (landline / mobile / both), bicycle, two-wheeler, car, all of TV-computer-phone-vehicle, none of these, % |
| `assets_scooter_motorcycle_moped_pct` | number | % | Households with radio, TV, computer (with / without internet), phone (landline / mobile / both), bicycle, two-wheeler, car, all of TV-computer-phone-vehicle, none of these, % |
| `assets_car_jeep_van_pct` | number | % | Households with radio, TV, computer (with / without internet), phone (landline / mobile / both), bicycle, two-wheeler, car, all of TV-computer-phone-vehicle, none of these, % |
| `assets_tv_computer_phone_and_scooter_or_car_pct` | number | % | Households with radio, TV, computer (with / without internet), phone (landline / mobile / both), bicycle, two-wheeler, car, all of TV-computer-phone-vehicle, none of these, % |
| `assets_none_of_listed_pct` | number | % | Households with radio, TV, computer (with / without internet), phone (landline / mobile / both), bicycle, two-wheeler, car, all of TV-computer-phone-vehicle, none of these, % |
| `house_structure_permanent_pct` | number | % | Type of structure: permanent, semi-permanent, temporary (total, serviceable, non-serviceable), unclassifiable, % |
| `house_structure_semi_permanent_pct` | number | % | Type of structure: permanent, semi-permanent, temporary (total, serviceable, non-serviceable), unclassifiable, % |
| `house_structure_total_temporary_pct` | number | % | Type of structure: permanent, semi-permanent, temporary (total, serviceable, non-serviceable), unclassifiable, % |
| `house_structure_serviceable_pct` | number | % | Type of structure: permanent, semi-permanent, temporary (total, serviceable, non-serviceable), unclassifiable, % |
| `house_structure_non_serviceable_pct` | number | % | Type of structure: permanent, semi-permanent, temporary (total, serviceable, non-serviceable), unclassifiable, % |
| `house_structure_unclassifiable_pct` | number | % | Type of structure: permanent, semi-permanent, temporary (total, serviceable, non-serviceable), unclassifiable, % |

Units are read from the column name (warehouse convention). Empty cells (`null` in JSON) mean no value.

## Notes from the warehouse

These describe the full warehouse table (all states).

- **2011 geography.** Rows are the 35 districts and their tehsils as in Census 2011; `Thane` includes today's Palghar (2014). District names and LGD codes are today's.
- Mumbai City and Mumbai Suburban are fully urban, so they have no `Rural` row.
- Values are percentages as printed (one decimal). A category group adds up to 100 within rounding (99.7 to 100.3).
- Kutcha / tin / asbestos roofs (a heat-exposure indicator) are `roof_grass_thatch_bamboo_wood_mud_etc_pct`, `roof_plastic_polythene_pct` and `roof_g_i_metal_asbestos_sheets_pct`; temporary houses are `house_structure_*temporary_pct`.
- Checks (18 Nov 2026): 103 rows = 35 districts x Total and Urban + 33 Rural; no duplicate keys (`district_census_code`, `residence`); all values 0-100; lighting and cooking-fuel groups add up to 99.8-100.3; identical to the district rows of the sub-district table. Nagpur (total): electricity 92.1%, fire-wood 32.0%, LPG/PNG 60.2%, as in the file.
- For other states, the same table is on the Census portal (one file per district); not taken yet.

## Where this comes from

- Warehouse folder [`HOU_household-amenities-hh14_2011_MH_ORGI_DIST`](https://github.com/sarveshkant2003-afk/bharatnomy-data/tree/930603697458e4ad288a0344bcd0c4c001d4462c/HOU_household-amenities-hh14_2011_MH_ORGI_DIST) at commit `930603697458`
- Filtered to `lgd_state_code` and cleaned by `build.py` in this repo. Files: `HOU_household-amenities-hh14_2011_MH_ORGI_DIST.csv`, `HOU_household-amenities-hh14_2011_MH_ORGI_DIST.json`.
