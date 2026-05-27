# Data

The raw source file is stored as a compressed CSV bundle:

```text
data/raw/europe_air_routes.zip
```

The archive contains:

```text
europe_air_routes.csv
```

The expanded CSV is intentionally ignored by Git. Keep the zip in `data/raw/`, then upload or register the CSV in Databricks as:

```text
workspace.eu_air_routes.europe_air_routes_raw
```

Run this local check to confirm the archive is readable:

```bash
python3 scripts/inspect_dataset.py
```
