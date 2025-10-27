import os
import re
import requests
from bs4 import BeautifulSoup

# Config
DATA_DIR = "data/raw"
os.makedirs(DATA_DIR, exist_ok=True)

BASE_URL = "https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page"
YELLOW_PATTERN = r"yellow_tripdata_(\d{4}-\d{2})\.parquet"

# Fetch page
print("Fetching TLC dataset page...")
response = requests.get(BASE_URL)
soup = BeautifulSoup(response.text, "html.parser")

# Extract all links
links = [a.get("href") for a in soup.find_all("a", href=True)]

# Filter yellow taxi parquet files
parquet_links = [
    link for link in links
    if re.search(YELLOW_PATTERN, link) and link.startswith("http")
]

print(f"Found {len(parquet_links)} Yellow Taxi parquet files.")

for link in parquet_links:
    filename = re.search(YELLOW_PATTERN, link).group(0)
    filepath = os.path.join(DATA_DIR, filename)

    if os.path.exists(filepath):
        print(f"Already downloaded: {filename}")
        continue

    print(f"Downloading: {filename}")
    try:
        file_data = requests.get(link)
        with open(filepath, "wb") as f:
            f.write(file_data.content)
        print(f"✅ Saved: {filepath}")
    except Exception as e:
        print(f"❌ Failed to download {filename}: {e}")

print("Done! 🚕✨")
