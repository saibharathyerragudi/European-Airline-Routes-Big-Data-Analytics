from __future__ import annotations

import csv
import json
import sys
import zipfile
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.eu_air_routes.schema import CORE_COLUMNS, RAW_CSV_NAME, RAW_ZIP_PATH


def inspect_dataset(zip_path: Path = Path(RAW_ZIP_PATH)) -> dict:
    if not zip_path.exists():
        raise FileNotFoundError(f"Dataset archive not found: {zip_path}")

    with zipfile.ZipFile(zip_path) as archive:
        names = archive.namelist()
        if RAW_CSV_NAME not in names:
            raise ValueError(f"{RAW_CSV_NAME} not found in archive. Found: {names}")

        with archive.open(RAW_CSV_NAME) as raw_file:
            text_file = (line.decode("utf-8") for line in raw_file)
            reader = csv.DictReader(text_file)
            first_rows = []
            for row in reader:
                first_rows.append(row)
                if len(first_rows) == 3:
                    break

            missing_columns = sorted(set(CORE_COLUMNS).difference(reader.fieldnames or []))
            return {
                "archive": str(zip_path),
                "csv": RAW_CSV_NAME,
                "column_count": len(reader.fieldnames or []),
                "columns": reader.fieldnames,
                "missing_expected_columns": missing_columns,
                "sample_row_count": len(first_rows),
            }


def main() -> None:
    print(json.dumps(inspect_dataset(), indent=2))


if __name__ == "__main__":
    main()
