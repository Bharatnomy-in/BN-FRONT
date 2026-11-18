# Bharatnomy data: front repo

The clean, public copy of Bharatnomy's district data, split by state and organised by Bharatnomy's five lenses.
Files here are what [bharatnomy.com](https://bharatnomy.com) links to for downloads, and what maps and dashboards read.

Everything under `states/` is **generated** by `build.py` from the warehouse repo
[`sarveshkant2003-afk/bharatnomy-data`](https://github.com/sarveshkant2003-afk/bharatnomy-data), at the commit pinned in
[`config/warehouse.lock`](config/warehouse.lock). The warehouse keeps data as collected; this repo filters it to one state,
cleans it, and adds CSV, JSON, READMEs, a district profile and a district map.

## What's here

```
states/<state>/
  README.md                 datasets by lens, data-as-of, how to use
  district-profile.csv/.json  one row per district, key indicators (with the year used)
  districts.geojson         district boundaries, keyed by lgd_district_code
  climate-adaptation/  energy-policy/  macro/  commodities/  equity/
    <DATASET>/<DATASET>.csv, <DATASET>.json, README.md
config/                     the only hand-edited inputs (see below)
frontbuild/                 the build code (build.py is the entry point)
tests/                      pytest checks
BUILD_INFO.json             warehouse commit, build date, datasets and row counts
BUILD_REPORT.md             warnings and decisions from the last build
ATTRIBUTION.md              every original source used
CHANGELOG.md                one entry each time the warehouse lock moves
```

Start with [`states/maharashtra/README.md`](states/maharashtra/README.md).

**Rules for using the data:** join and filter on `lgd_district_code` / `lgd_state_code` (text), never on names.
Missing values are empty in CSV and `null` in JSON. Rows that were state totals in the warehouse are left out; add up districts instead.

## Rebuild

```bash
pip install -r requirements.txt     # Python 3.11+
python build.py                     # build from the pinned warehouse commit, then run checks
python build.py --check             # checks only
python build.py --update-lock       # move to the warehouse's latest main, rebuild, add a CHANGELOG entry
```

The build downloads the warehouse into `.cache/warehouse/` (git-ignored). The same lock and config always give byte-identical
output; CI ([`validate.yml`](.github/workflows/validate.yml)) rebuilds on every push and fails if the committed output differs.
**Never edit files under `states/` by hand**: change `config/` or the code, then rebuild.

## Config files

| File | What it controls |
|---|---|
| `warehouse.lock` | Warehouse repo URL and the pinned commit SHA |
| `states.csv` | States to build (`state_slug,state_code_short,lgd_state_code`) |
| `lens_folders.csv` | Lens ID → folder name |
| `dataset_lens.csv` | Lens for datasets that are missing from, or tied in, the warehouse's `variables.csv` |
| `excluded_datasets.csv` | District tables deliberately not shipped, with the reason |
| `derived_columns.csv` | Extra computed columns (`dataset,new_column,formula,unit,description`) |
| `profile_indicators.csv` | Columns of the district profile |

## Add a state

1. Add one line to `config/states.csv`, e.g. `karnataka,KA,29` (the LGD state code is in the warehouse's `_reference/geography.csv`).
2. Run `python build.py`. Every district table with rows for that state is filtered, named with the state code, and written to `states/<slug>/`.
3. Read `BUILD_REPORT.md`: check new lens questions, missing districts and districts with no 2011 boundary.
4. The district profile uses the same indicators for every state (the `MH` in dataset names is swapped for the state's code); indicators with no data for a state show up under Errors in the report.

## Licence

Bharatnomy's own calculations (tables with `BNY` as SOURCE in the name, the district profile) are licensed under [LICENSE](LICENSE).
Government and third-party data keep their original terms; see [ATTRIBUTION.md](ATTRIBUTION.md).
