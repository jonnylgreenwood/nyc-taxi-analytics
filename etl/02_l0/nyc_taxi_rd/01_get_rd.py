import os
import re
import requests
from bs4 import BeautifulSoup
from datetime import datetime


# Config
DATA_DIR = "data/raw"
os.makedirs(DATA_DIR, exist_ok=True)

BASE_URL = "https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page"
FILE_ID = "fvh"
FILE_PATTERN = fr"{FILE_ID}_tripdata_(\d{4}-\d{2})\.parquet"
START_MONTH = "2024-10"
END_MONTH = "2025-09"



def get_raw_data(BASE_URL="https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page", FILE_ID="yellow", FILE_PATTERN=fr"{FILE_ID}_tripdata_(\d{4}-\d{2})\.parquet", START_MONTH="2024-10", END_MONTH="2025-09"):
    # Define date bounds
    start_month = datetime.strptime(START_MONTH, "%Y-%m")
    end_month   = datetime.strptime(END_MONTH, "%Y-%m")

    def is_in_range(date_str):
        """Checks if YYYY-MM is within defined bounds."""
        dt = datetime.strptime(date_str, "%Y-%m")
        return start_month <= dt <= end_month

    print("Fetching TLC dataset page...")
    response = requests.get(BASE_URL)
    soup = BeautifulSoup(response.text, "html.parser")

    # Extract all links
    links = [a.get("href") for a in soup.find_all("a", href=True)]

    # Filter yellow taxi parquet files
    filtered_links = []
    for link in links:
        match = re.search(FILE_PATTERN, link)
        if match and link.startswith("http"):
            month_str = match.group(1)
            if is_in_range(month_str):
                filtered_links.append(link)

    print(f"✅ Found {len(filtered_links)} Yellow Taxi files in date range ({start_month:%Y-%m} → {end_month:%Y-%m})")

    for link in filtered_links:
        filename = re.search(FILE_PATTERN, link).group(0)
        filepath = os.path.join(DATA_DIR, filename)

        if os.path.exists(filepath):
            print(f"Already exists: {filename}")
            continue

        print(f"⬇️ Downloading: {filename}")
        try:
            file_data = requests.get(link)
            with open(filepath, "wb") as f:
                f.write(file_data.content)
            print(f"✅ Saved: {filepath}")
        except Exception as e:
            print(f"❌ Failed: {filename} — {e}")

    print("✅ Done downloading! 🚕✨")

s_mnth = "2024-10"
e_mnth = "2025-09"

# yellow
get_raw_data(BASE_URL="https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page",
             FILE_ID="yellow",
             FILE_PATTERN=fr"{FILE_ID}_tripdata_(\d{4}-\d{2})\.parquet",
             START_MONTH = s_mnth,
             END_MONTH= e_mnth)

# fvh
get_raw_data(BASE_URL="https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page",
             FILE_ID="fhv",
             FILE_PATTERN=fr"{FILE_ID}_tripdata_(\d{4}-\d{2})\.parquet",
             START_MONTH = s_mnth,
             END_MONTH= e_mnth)

# green
get_raw_data(BASE_URL="https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page",
             FILE_ID="green",
             FILE_PATTERN=fr"{FILE_ID}_tripdata_(\d{4}-\d{2})\.parquet",
             START_MONTH = s_mnth,
             END_MONTH= e_mnth)