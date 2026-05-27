import unittest
import zipfile
from pathlib import Path

from src.eu_air_routes.schema import CORE_COLUMNS, ENGINEERED_COLUMNS, RAW_CSV_NAME, RAW_ZIP_PATH


class SchemaTests(unittest.TestCase):
    def test_expected_raw_columns(self):
        self.assertIn("iata_from", CORE_COLUMNS)
        self.assertIn("iata_to", CORE_COLUMNS)
        self.assertIn("price", CORE_COLUMNS)
        self.assertIn("departure_latitude", CORE_COLUMNS)
        self.assertIn("arrival_longitude", CORE_COLUMNS)

    def test_engineered_columns(self):
        self.assertIn("distance_km", ENGINEERED_COLUMNS)
        self.assertIn("price_per_km", ENGINEERED_COLUMNS)
        self.assertIn("days_operated", ENGINEERED_COLUMNS)

    def test_raw_zip_contains_expected_csv(self):
        zip_path = Path(RAW_ZIP_PATH)
        self.assertTrue(zip_path.exists())
        with zipfile.ZipFile(zip_path) as archive:
            self.assertIn(RAW_CSV_NAME, archive.namelist())


if __name__ == "__main__":
    unittest.main()
