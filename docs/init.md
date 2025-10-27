1. Nav to proj folder
   cd nyc-taxi-analytics
2. create venv
   python3 -m venv .venv
3. Activate venv
   source .venv/bin/activate
4. Install dependencies
   pip install requests beautifulsoup4 pandas duckdb pyarrow
5. freeze reqs
   pip freeze > requirements.txt
6. Add VS Code integration
   Python: Select Interpreter
7. Update .gitignore
   .venv/
   data/raw/
   __pycache__/

1. create db and schema
std command prompt for running scripts:
duckdb analytics.db -f x
Eg duckdb analytics.db -f etl/00_setup/02_create_schema.sql


Open file: data/raw/yellow_tripdata_2025-09.parquet
Rows: 4251015

Columns: 20

Column names & types:

  VendorID: int32
  
  tpep_pickup_datetime: timestamp[us]
  
  tpep_dropoff_datetime: timestamp[us]
  
  passenger_count: int64
  
  trip_distance: double
  
  RatecodeID: int64
  
  store_and_fwd_flag: large_string
  
  PULocationID: int32
  
  DOLocationID: int32
  
  payment_type: int64
  
  fare_amount: double
  
  extra: double
  
  mta_tax: double
  
  tip_amount: double
  
  tolls_amount: double
  
  improvement_surcharge: double
  
  total_amount: double
  
  congestion_surcharge: double
  
  Airport_fee: double
  
  cbd_congestion_fee: double
  
Null counts for key cols:

tpep_pickup_datetime           0

tpep_dropoff_datetime          0

passenger_count          1067195

dtype: int64

Min/Max trip_distance, fare_amount:

0.0 318608.57

-998.0 323800.27
