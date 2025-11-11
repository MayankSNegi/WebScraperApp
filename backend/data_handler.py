import csv
import os
from typing import List, Dict

class DataHandler:
    """Handles saving and reading CSV data"""

    DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')
    CSV_FILE = os.path.join(DATA_DIR, 'scraped_data.csv')

    @staticmethod
    def ensure_data_dir():
        """Ensure the /data directory exists"""
        if not os.path.exists(DataHandler.DATA_DIR):
            os.makedirs(DataHandler.DATA_DIR)

    @staticmethod
    def save_to_csv(books: List[Dict]) -> bool:
        """
        Save scraped data to CSV.
        Overwrites previous file each run (fresh scrape).
        """
        try:
            DataHandler.ensure_data_dir()
            if not books:
                print("⚠️ No data to save")
                return False

            fieldnames = list(books[0].keys())

            # ✅ Write with UTF-8 BOM to ensure £, €, ₹ etc. render correctly in Excel
            with open(DataHandler.CSV_FILE, 'w', newline='', encoding='utf-8-sig') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(books)

            print(f"✅ Data saved to {DataHandler.CSV_FILE}")
            return True

        except Exception as e:
            print(f"❌ Error saving to CSV: {e}")
            return False

    @staticmethod
    def read_from_csv() -> List[Dict]:
        """Read and return CSV data"""
        try:
            if not os.path.exists(DataHandler.CSV_FILE):
                return []

            with open(DataHandler.CSV_FILE, 'r', encoding='utf-8-sig') as csvfile:
                reader = csv.DictReader(csvfile)
                return list(reader)

        except Exception as e:
            print(f"❌ Error reading CSV: {e}")
            return []

    @staticmethod
    def get_csv_filename() -> str:
        """Return file name only"""
        return os.path.basename(DataHandler.CSV_FILE)
