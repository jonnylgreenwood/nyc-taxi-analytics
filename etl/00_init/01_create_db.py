import duckdb
from pathlib import Path

# Base project directory (one level up from /SQL)
base_dir = Path(__file__).resolve().parent.parent.parent

print(base_dir)

# Connect to database in project root
con = duckdb.connect(base_dir / 'etl/analytics.duckdb')

con.close()