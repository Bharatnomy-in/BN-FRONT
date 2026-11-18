# Multidimensional poverty by district, 2015-16 and 2019-21 — Maharashtra

Share of people who are multidimensionally poor (deprived in at least a third of 12 weighted indicators of health, education and living standards), how deprived they are on average, and the MPI, for each district, state and India, from NFHS-4 (2015-16) and NFHS-5 (2019-21).

## Coverage

- **Rows:** 72
- **Period:** 2015-16 to 2019-21
- **Districts:** 36 of 36
- 2 state-total row(s) from the warehouse table are left out; add up district rows instead.

## Source

- **Data:** NITI Aayog, *National Multidimensional Poverty Index: A Progress Review 2023* (July 2023), computed from NFHS-4 and NFHS-5
- **Table taken from:** each state's "<State>: Overview of Districts — Headcount Ratio, Intensity and MPI" table, and the "<State>'s Headcount Ratio, Intensity and MPI" table of each state profile (state rows) and of the India overview (All India)
- **Link:** https://www.niti.gov.in/sites/default/files/2023-08/India-National-Multidimentional-Poverty-Index-2023.pdf
- **Downloaded:** 12 Nov 2026 (PDF in [`_sources/niti-mpi/raw/`](https://github.com/sarveshkant2003-afk/bharatnomy-data/tree/930603697458e4ad288a0344bcd0c4c001d4462c/_sources/niti-mpi/raw/))
- **Script:** [`pipelines/niti-mpi/build_mpi_district.py`](https://github.com/sarveshkant2003-afk/bharatnomy-data/tree/930603697458e4ad288a0344bcd0c4c001d4462c/pipelines/niti-mpi/build_mpi_district.py)

## Columns

| Column | Type | Unit | Description |
|---|---|---|---|
| `state_ut` | text |  | State or UT; `All India` for the national row |
| `lgd_state_code` | text |  | State/UT code in the Local Government Directory (LGD), from [`_reference/geography.csv`](https://github.com/sarveshkant2003-afk/bharatnomy-data/tree/930603697458e4ad288a0344bcd0c4c001d4462c/_reference/geography.csv) |
| `district` | text |  | District as spelled in the report (alternative names in brackets as printed). `State total` = the state's own figure |
| `lgd_district_code` | text |  | District code in the LGD. Blank for totals and names that could not be matched |
| `year` | text |  | NFHS round: `2015-16` (NFHS-4) or `2019-21` (NFHS-5) |
| `headcount_ratio_pct` | number | % | Headcount ratio (H): % of population who are multidimensionally poor |
| `intensity_pct` | number | % | Intensity (A): average share of weighted deprivations among the poor, % |
| `mpi` | number |  | Multidimensional Poverty Index = H x A (0 to 1) |
| `source_flag` | text |  | `not_available` where the report prints "–" (district did not exist in NFHS-4, e.g. Palghar) |

Units are read from the column name (warehouse convention). Empty cells (`null` in JSON) mean no value.

## Notes from the warehouse

These describe the full warehouse table (all states).

- **Bihar's districts are missing.** In the PDF, Bihar's district table (page 80 of the report) is printed on top of a hidden, squeezed copy of Assam's table; the two layers share the same font and colour and cannot be separated reliably. Bihar's state figures are included.
- Districts are those of NFHS-5 (2019-21); some states have since split districts (e.g. Andhra Pradesh had 13 districts then and has 28 in LGD today). Only 575 districts are comparable between the two rounds (report, p. 33).
- Some names differ from LGD (e.g. SPSR Nellore, Warangal Rural/Urban, Kanchipuram); 17 district names have no `lgd_district_code`.
- Intensity is blank (`–`) where the headcount ratio is 0.
- The report's other tables (state-wise rural/urban MPI, deprivation in each indicator, standard errors; Annex tables 1-21) are printed rotated and are not yet extracted.
- Checks (12 Nov 2026): 1,416 rows = (671 districts + 36 state totals + All India) x 2 rounds; no duplicate keys; MPI equals H x A (within rounding) in every row; headcount 0-74.35%, intensity 33.33-57.27%, MPI 0-0.412; spot checks against the PDF: Maharashtra 2015-16 14.80% / 43.76% / 0.065, Nagpur 2019-21 1.25% / 34.18% / 0.004, All India 2019-21 14.96% / 44.39% / 0.066.

## Where this comes from

- Warehouse folder [`SOC_multidimensional-poverty_2015-16-to-2019-21_STATES_NITI_DIST`](https://github.com/sarveshkant2003-afk/bharatnomy-data/tree/930603697458e4ad288a0344bcd0c4c001d4462c/SOC_multidimensional-poverty_2015-16-to-2019-21_STATES_NITI_DIST) at commit `930603697458`
- Filtered to `lgd_state_code` and cleaned by `build.py` in this repo. Files: `SOC_multidimensional-poverty_2015-16-to-2019-21_MH_NITI_DIST.csv`, `SOC_multidimensional-poverty_2015-16-to-2019-21_MH_NITI_DIST.json`.
