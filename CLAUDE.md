# CLAUDE.md: Bharatnomy front repo

This repo is the **front repo**: the clean, public, organised copy of Bharatnomy's data.
It is **generated** from the warehouse repo
[`sarveshkant2003-afk/bharatnomy-data`](https://github.com/sarveshkant2003-afk/bharatnomy-data)
by one script, `build.py`. The warehouse holds data as it was collected. This repo holds the same
data split by state, organised by Bharatnomy's 5 lenses and ready for downloads and maps.

Users:
1. The public, who download CSVs from bharatnomy.com, which links to files in this repo.
2. The frontend developer, who reads the CSV, JSON and GeoJSON files directly into maps and dashboards.

## Golden rules

- **Never hand-edit anything under `states/`.** Every file there is written by `build.py`. To change
  output, change `build.py` or a file in `config/`, then rebuild.
- **Never modify the warehouse.** The build only reads it. Cleaning and derived columns happen here, in the build.
- **Join and filter on LGD codes** (`lgd_state_code`, `lgd_district_code`), never on names. Maharashtra is
  `lgd_state_code = 27`. Use names only as a fallback via `_reference/geography.csv` (its `aliases` column),
  and log every fallback match.
- **Never invent data, derived formulas or lens assignments.** If something is unclear, write it to the build
  report (see below) and ask the user.
- **File paths are public URLs.** Once a file is published, its path must not change. Ask before renaming or moving anything.
- Keep the build **deterministic**: the same warehouse commit and config must give byte-identical output
  (sorted rows, fixed column order, no timestamps inside data files).

## Scope for v1

- **State:** Maharashtra only. Write the code so any state can be added later with one config line
  (`config/states.csv`: `state_slug,state_code_short,lgd_state_code`, e.g. `maharashtra,MH,27`). Do not hard-code Maharashtra in logic.
- **Datasets:** every warehouse table at **district level** (folder name ends in `_DIST`) that has rows for
  Maharashtra. That is about 22 tables, including the `_STATES_..._DIST` ones (filter them to Maharashtra) and the
  `_MH_..._DIST` ones.
- **Excluded for v1:** state-level tables (no `_LEVEL` suffix), all-India (`_IN_`), city (`_CITY`), sub-district (`_SDT`),
  and the raw files in `_sources/`. Also skip a district table if it ends up with zero Maharashtra rows after filtering
  (for example, Nagpur-only tables are fine to keep; tables with no MH districts are not), and list it in the build report.

## Getting the warehouse (pinned clone)

- `config/warehouse.lock` holds the repo URL and **one full commit SHA**.
- `build.py` clones the warehouse into `.cache/warehouse/` (git-ignored) and checks out that exact SHA. If it is already
  cloned, it fetches and checks out the SHA. Use `--depth`/`--filter=blob:none` and sparse checkout to skip `_sources/`
  except `_sources/datameet-maps/raw/` (needed for boundaries).
- `python build.py --update-lock` moves the lock to the warehouse's latest `main` commit, then rebuilds. The user runs this
  on purpose; a normal `python build.py` never changes the lock.
- Every build writes `BUILD_INFO.json` at the repo root: warehouse SHA, build date, list of datasets with row counts.

## Output layout

```
states/
  maharashtra/
    README.md                         # generated: datasets, coverage, data-as-of, warehouse SHA
    district-profile.csv
    district-profile.json
    districts.geojson
    climate-adaptation/
      <DATASET_NAME>/
        <DATASET_NAME>.csv
        <DATASET_NAME>.json
        README.md
    energy-policy/
    macro/
    commodities/
    equity/
config/
  warehouse.lock
  states.csv
  lens_folders.csv
  dataset_lens.csv
  derived_columns.csv
  profile_indicators.csv
build.py               # entry point; split into a small package (build/) if it grows past ~300 lines
tests/
BUILD_REPORT.md        # generated: warnings, skipped datasets, name-fallback matches, unmapped items
BUILD_INFO.json
LICENSE  ATTRIBUTION.md  CHANGELOG.md  README.md
.github/workflows/validate.yml
```

### Lens folders (lens folders only, no topic sub-folders)

`config/lens_folders.csv` maps lens IDs (from the warehouse's `_reference/lenses.csv`) to folder names:

| lens_id | folder |
|---|---|
| CAR | climate-adaptation |
| EPM | energy-policy |
| MAC | macro |
| COM | commodities |
| EQM | equity |

Create all five folders for each state even if some are empty; an empty folder gets a `README.md` saying
"No district-level data for this lens yet."

### Which lens each dataset goes in

1. Read `_reference/variables.csv` in the warehouse (columns: `variable_id,name,lens_id,sub_theme_id,dataset,column,...`).
   A dataset's lens is the `lens_id` of its variables there. If its variables span several lenses, use the most common one
   and list the split in the build report.
2. Datasets not in `variables.csv` are looked up in `config/dataset_lens.csv` (`dataset,lens_id,note`).
3. On the **first run**, fill `config/dataset_lens.csv` with a proposed lens for every unmapped dataset, set
   `note=PROPOSED - review`, and **stop and show the user the list for approval**. After that, a dataset with no lens
   fails the build with a clear message.

### File names

Keep the **warehouse naming scheme** (see the warehouse README, "Folder names"):
`CATEGORY_subject_PERIOD_GEOGRAPHY_SOURCE_LEVEL`. Make two automatic changes:

- **GEOGRAPHY becomes the state code**, because each file is filtered to one state:
  `CLM_cyclone-crossings_1982-to-2025_STATES_BNY_DIST` → `CLM_cyclone-crossings_1982-to-2025_MH_BNY_DIST`.
  Names that already say `MH` stay as they are.
- **Merged parts:** tables split into parts with the same CATEGORY, subject, SOURCE and LEVEL but different periods
  (e.g. `AGR_crop-area-production-yield_1997-98-to-2009-10_...` and `..._2010-11-to-2022-23_...`) are concatenated into
  one file, with the period spanning both: `AGR_crop-area-production-yield_1997-98-to-2022-23_MH_MOAFW_DIST`.
  Before merging, check the columns match, drop exact duplicate rows, and report any overlapping year with conflicting
  values (keep the newer part's value).
- **PERIOD must reflect the Maharashtra data**: if filtering narrows the years, use the actual range and note it in the README.

## Per-dataset processing (in this order)

1. Read the warehouse CSV with all columns as strings first, then cast by the column types given in the warehouse dataset
   README. Never let pandas silently turn codes into floats (`466` must not become `466.0`).
2. Filter to the state by `lgd_state_code`.
3. **Clean:** trim whitespace; consistent `NA` handling (empty cell in CSV, `null` in JSON); standardise district names
   to the `district` value in `geography.csv` for that LGD code; dates as ISO `YYYY-MM-DD`, months as `YYYY-MM`, financial
   years as `YYYY-YY`; no thousands separators. Do **not** change values, units or rounding beyond that.
4. **Derived columns:** add only what `config/derived_columns.csv` lists:
   `dataset,new_column,formula,unit,description`, where `formula` is a pandas `eval` expression over existing columns
   (e.g. `households_with_tap / total_households * 100`). Population or area denominators come only from datasets named
   in the formula's row; never assume a source. Ship the file empty except for a commented example. Existing derived
   columns in the warehouse (e.g. `tmax_mean_anomaly_c`) carry over unchanged.
5. Sort rows by LGD district code, then time columns, then remaining key columns.
6. Write `<name>.csv` (UTF-8, comma, header, `\n` line endings) and `<name>.json`
   (an array of row objects, numbers as numbers, codes as strings; pretty-printing off). If a JSON file would exceed
   ~25 MB, write it as JSON Lines (`.jsonl`) instead and say so in the README.
7. Write the dataset `README.md`, generated from the warehouse README: title, what the table holds, source and link,
   the Bharatnomy-calculation note if SOURCE is `BNY`, period and districts covered for this state, row count,
   a column table (name, type, unit, description) including derived columns marked **derived**, and the warehouse folder
   and commit it came from.

## District profile

- `config/profile_indicators.csv`: `indicator_id,label,dataset,column,aggregation,filter,unit`.
  - `aggregation`: `latest` (default: value in the latest year/period available for that district), or later `mean_last_5`, `sum`, etc.
  - `filter`: optional pandas query for long tables, e.g. `crop == 'Rice' and season == 'Kharif'`, so the result is one value per district.
- Output: `district-profile.csv` and `.json`. One row per Maharashtra district (**36 rows**, from `geography.csv`), columns
  `lgd_district_code, district`, then for each indicator two columns: `<indicator_id>` and `<indicator_id>_year`
  (which year was used). A district with no value gets an empty cell, never a zero.
- On the first run, Claude Code proposes 15-20 indicators across the available datasets, marked for review, and **asks the user
  to approve them** before publishing.

## District boundaries (GeoJSON)

- Source: `_sources/datameet-maps/raw/datameet-maps_census2011-districts_2011.shp` in the warehouse (Census 2011 districts).
- Map each polygon to an LGD district code via `census2011_district_code` in `geography.csv`.
- Districts **created after 2011** (`created_after_2011` in `geography.csv`) have no 2011 polygon. Do not fake boundaries:
  include them as features with `geometry: null` and `properties.boundary_note`, list them in the README and build report,
  and ask the user whether to source newer boundaries (e.g. a newer datameet or LGD-based file) in a later step.
- Properties per feature: `lgd_district_code`, `district`, `lgd_state_code`, `state_ut`, `census2011_district_code`.
- Reproject to WGS84 (EPSG:4326), simplify geometry to keep the file under ~3 MB, and round coordinates to 5 decimals.
  Validate the output with a GeoJSON check (all geometries valid, 36 features).

## Generated READMEs and repo docs

- `states/maharashtra/README.md`: table of datasets by lens (name, what it holds, period, rows, link), files for maps
  (profile, GeoJSON), data-as-of = latest period across datasets, warehouse SHA, and a short "How to use" with raw-file URLs.
- Root `README.md` (hand-written; Claude Code drafts it once): what this repo is, how it relates to the warehouse,
  folder layout, how to rebuild (`pip install -r requirements.txt && python build.py`), how to add a state, licence.
- `ATTRIBUTION.md`: generated list of every original source used (organisation, publication, link), from the warehouse READMEs.
- `LICENSE`: ask the user which licence to use for Bharatnomy's own calculations (suggest CC BY 4.0); government source
  data keeps its original terms, which `ATTRIBUTION.md` lists.
- `CHANGELOG.md`: append an entry when the lock moves: date, old SHA → new SHA, datasets added, removed or changed (row-count diffs).

## Checks (`tests/` + CI)

`python build.py --check` and `.github/workflows/validate.yml` (runs on push and PR; does a pinned build and fails if
the committed output differs from a fresh build) must verify:

- every row in `states/<state>/` has that state's `lgd_state_code`;
- every `lgd_district_code` exists in `geography.csv` for that state;
- row count per output file equals the warehouse row count for that state (merged files: the sum minus reported duplicates);
- CSV and JSON of the same table have the same rows and columns;
- every dataset folder has CSV, JSON and README, and every lens folder has a README;
- the district profile has one row per district; the GeoJSON parses and has one feature per district;
- no file over 50 MB (warn) or 95 MB (fail; GitHub's hard limit is 100 MB).

## Build report

Each run rewrites `BUILD_REPORT.md` with: datasets included or skipped (and why), name-fallback matches, unmapped lenses,
merge conflicts, districts missing per dataset, and new or removed columns compared with the last build. Show the user a
short summary of it after every build.

## Tech

- Python 3.11+, `pandas`, `geopandas` (`shapely`, `pyproj`), and `pytest`. Pin versions in `requirements.txt`.
- Clear names, short functions, type hints, and a docstring at the top of each module explaining what it does.
  The user is learning; add brief comments where the logic is not obvious.
- Commit build output and code in separate commits when practical. Commit messages say what changed and which warehouse SHA was used.

## First session: do this in order and pause where marked

1. Create the repo skeleton, `requirements.txt`, `.gitignore` (`.cache/`), config files, and `warehouse.lock` pinned to the
   warehouse's current `main` SHA.
2. Clone the warehouse; list the district-level datasets that have Maharashtra rows, with proposed lens and merge groups.
   **Pause: show the list and the proposed `dataset_lens.csv`; wait for approval.**
3. Build the datasets (CSV, JSON, README) and the checks.
4. Build the GeoJSON. **Pause: report districts without 2011 boundaries.**
5. Propose `profile_indicators.csv`. **Pause for approval**, then build the profile.
6. Generate the READMEs, ATTRIBUTION and BUILD_INFO; run `--check`; add the CI workflow.
7. Show the build report summary and ask the user about the licence before the first push.
