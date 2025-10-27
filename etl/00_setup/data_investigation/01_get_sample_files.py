import os
import re
import requests
from bs4 import BeautifulSoup

# Config
DATA_DIR = "data/raw"
os.makedirs(DATA_DIR, exist_ok=True)

BASE_URL = "https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page"

# Only download Jan + Jul (samples for schema profile)
SAMPLE_MONTHS = ["-01", "-07"]

# Patterns by dataset type
DATASETS = {
    "yellow": r"yellow_tripdata_(\d{4}-\d{2})\.parquet",
    "green": r"green_tripdata_(\d{4}-\d{2})\.parquet",
    "fhv": r"fhv_tripdata_(\d{4}-\d{2})\.parquet",
    "hvfhv": r"hvfhv_tripdata_(\d{4}-\d{2})\.parquet"
}

print("Fetching TLC dataset page...")
response = requests.get(BASE_URL)
soup = BeautifulSoup(response.text, "html.parser")

# Extract all parquet links
links = [a.get("href") for a in soup.find_all("a", href=True)]

total_downloads = 0

for dataset_type, pattern in DATASETS.items():
    print(f"\n🔍 Searching for {dataset_type.upper()} datasets...")
    
    # Filter matching parquet links
    matches = [
        link for link in links
        if re.search(pattern, link) and link.startswith("http")
    ]

    for link in matches:
        # Extract YYYY-MM
        ym = re.search(pattern, link).group(1)
        
        # Only download symbolic months → Jan + Jul
        if not any(ym.endswith(month) for month in SAMPLE_MONTHS):
            continue

        # Build filename and path
        filename = re.search(pattern, link).group(0)
        filepath = os.path.join(DATA_DIR, filename)

        if os.path.exists(filepath):
            print(f"🟡 Already downloaded: {filename}")
            continue

        print(f"⬇️ Downloading {dataset_type}: {filename}")
        try:
            file_data = requests.get(link)
            with open(filepath, "wb") as f:
                f.write(file_data.content)
            print(f"✅ Saved: {filepath}")
            total_downloads += 1
        except Exception as e:
            print(f"❌ Failed to download {filename}: {e}")

print(f"\n✨ Done! Downloaded {total_downloads} sample Parquet files.")
