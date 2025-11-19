duckdb etl/analytics.duckdb -f 


# Init
| Description            | files                     | cmd           |
|:-----------------------|:------------------------|:----------------|
|Create db with schema and display them|etl/00_init/01_create_db.py<br> etl/00_init/02_create_schema.sql<br> etl/00_init/03_get_schema.sql<br> |duckdb etl/analytics.duckdb -f etl/00_init/02_create_schema.sql<br>duckdb etl/analytics.duckdb -f etl/00_init/03_get_schema.sql|


# Loop 1
## L0
| Description            | files                     | cmd           |
|:-----------------------|:------------------------|:----------------|
|Get raw taxi data|etl/02_l0/nyc_taxi_rd/01_get_rd.py<br>|etl/02_l0/nyc_taxi_rd/01_get_rd.py<br>|
|Create ingestion table and seed ingestion table|etl/02_l0/nyc_taxi_rd/02_add_ingestion_control_table.sql<br>etl/02_l0/nyc_taxi_rd/03_seed_ingestion_control_table.sql|duckdb etl/analytics.duckdb -f etl/02_l0/nyc_taxi_rd/02_add_ingestion_control_table.sql<br>duckdb etl/analytics.duckdb -f etl/02_l0/nyc_taxi_rd/03_seed_ingestion_control_table.sql|
|Load taxi parquets to database|etl/02_l0/nyc_taxi_rd/04_load_raw_data_using_controls.py<br>etl/02_l0/nyc_taxi_rd/05_check_load.sql|etl/02_l0/nyc_taxi_rd/04_load_raw_data_using_controls.py<br>duckdb etl/analytics.duckdb -f etl/02_l0/nyc_taxi_rd/05_check_load.sql|
|Load taxi zone lookups|tl/02_l0/taxi_zone/01_load_taxi_zone_lookup.sql|duckdb etl/analytics.duckdb -f tl/02_l0/taxi_zone/01_load_taxi_zone_lookup.sql|

## Profile Data
| Description            | files                     | cmd           |
|:-----------------------|:------------------------|:----------------|
|Profile sample files and add to markdown file|etl/01_dq/raw_data_profiling/02_profile_schemas_compare.py<br>etl/01_dq/raw_data_profiling/04_profile_sample_files.py<br>|duckdb etl/analytics.duckdb -f etl/01_dq/raw_data_profiling/02_profile_schemas_compare.py<br>duckdb etl/analytics.duckdb -f etl/01_dq/raw_data_profiling/04_profile_sample_files.py<br>|

## L1
| Description            | files                     | cmd           |
|:-----------------------|:------------------------|:----------------|
|Pull from l0 to l1 and apply standardisations|etl/03_l1/dim_location/dim_location.sql<br>etl/03_l1/fact_trips/01_create_fact_trips.sql<br>etl/03_l1/fact_trips/02_insert_fact_trips.py<br>etl/03_l1/fact_trips/sample_fact_trips_tables.sql|duckdb etl/analytics.duckdb -f etl/03_l1/dim_location/dim_location.sql<br>duckdb etl/analytics.duckdb -f etl/03_l1/fact_trips/01_create_fact_trips.sql<br>etl/03_l1/fact_trips/02_insert_fact_trips.py<br>duckdb etl/analytics.duckdb -f etl/03_l1/fact_trips/sample_fact_trips_tables.sql|

## L2
| Description            | files                     | cmd           |
|:-----------------------|:------------------------|:----------------|
|Fully refresh l2 data|etl/04_l2/dim_calendar/03_create_dim_calendar.sql<br>etl/04_l2/dim_location/06_create_dim_location.sql<br>etl/04_l2/dim_location/view_dim_location.sql<br>etl/04_l2/dim_payment_types/04_create_dim_payment_types.sql<br>etl/04_l2/dim_rate_code/05_create_dim_rate_code.sql<br>etl/04_l2/fact_trips/01_create_fact_trips.sql<br>etl/04_l2/fact_trips/02_insert_fact_trips.sql<br>etl/04_l2/fact_trips/07_add_business_rules_fact_trips.sql<br>etl/04_l2/fact_trips/sample_fact_trips_tables.sql|duckdb etl/analytics.duckdb -f etl/04_l2/dim_calendar/03_create_dim_calendar.sql<br>duckdb etl/analytics.duckdb -f etl/04_l2/dim_location/06_create_dim_location.sql<br>duckdb etl/analytics.duckdb -f etl/04_l2/dim_location/view_dim_location.sql<br>duckdb etl/analytics.duckdb -f etl/04_l2/dim_payment_types/04_create_dim_payment_types.sql<br>duckdb etl/analytics.duckdb -f etl/04_l2/dim_rate_code/05_create_dim_rate_code.sql<br>duckdb etl/analytics.duckdb -f etl/04_l2/fact_trips/01_create_fact_trips.sql<br>duckdb etl/analytics.duckdb -f etl/04_l2/fact_trips/02_insert_fact_trips.sql<br>duckdb etl/analytics.duckdb -f etl/04_l2/fact_trips/07_add_business_rules_fact_trips.sql<br>duckdb etl/analytics.duckdb -f etl/04_l2/fact_trips/sample_fact_trips_tables.sql|




duckdb etl/analytics.duckdb -f etl/04_l2/fact_trips/01_create_fact_trips.sql
duckdb etl/analytics.duckdb -f etl/04_l2/fact_trips/02_insert_fact_trips.sql
duckdb etl/analytics.duckdb -f etl/04_l2/fact_trips/07_add_business_rules_fact_trips.sql
duckdb etl/analytics.duckdb -f etl/04_l2/fact_trips/sample_fact_trips_tables.sql


duckdb etl/analytics.duckdb -f etl/04_l2/dim_calendar/03_create_dim_calendar.sql
duckdb etl/analytics.duckdb -f etl/04_l2/dim_location/06_create_dim_location.sql
duckdb etl/analytics.duckdb -f etl/04_l2/dim_location/view_dim_location.sql
duckdb etl/analytics.duckdb -f etl/04_l2/dim_payment_types/04_create_dim_payment_types.sql
duckdb etl/analytics.duckdb -f etl/04_l2/dim_rate_code/05_create_dim_rate_code.sql