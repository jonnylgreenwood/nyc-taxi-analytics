import duckdb

con = duckdb.connect("etl/analytics.duckdb")

# Pull L0 tables dynamically
l0_tables = con.execute("""
    SELECT table_name
    FROM information_schema.tables
    WHERE table_schema='l0'
      AND (
            table_name LIKE 'yellow_trip_%'
         OR table_name LIKE 'green_trip_%'
         OR table_name LIKE 'fhv_trip_%'
      )
""").fetchdf()['table_name']

def have(tbl, col):
    """Check if column exists in source table."""
    return con.execute(f"""
        SELECT COUNT(*)
        FROM information_schema.columns
        WHERE table_schema='l0'
          AND table_name='{tbl}'
          AND column_name='{col}'
    """).fetchone()[0] > 0

for tbl in l0_tables:
    service = tbl.split('_')[0]
    year = tbl.split('_')[2]
    month = tbl.split('_')[3]
    ingestion_month = f"{year}_{month}"

    print(f"🔄 Loading: {tbl} → {service} [{ingestion_month}]")

    if service == "yellow":
        pickup_col = "tpep_pickup_datetime"
        dropoff_col = "tpep_dropoff_datetime"
        dropoff_loc = "DOLocationID"
    elif service == "green":
        pickup_col = "lpep_pickup_datetime"
        dropoff_col = "lpep_dropoff_datetime"
        dropoff_loc = "DOLocationID"
    elif service == "fhv":
        pickup_col = "pickup_datetime"
        dropoff_col = "dropOff_datetime"
        dropoff_loc = "DOlocationID"
    else:
        print(f"⚠️ Skipping unknown: {tbl}")
        continue

    # Build unified select list
    fields = {
        "vendor_id": "CAST(VendorID AS INTEGER)" if have(tbl, "VendorID") else "NULL",
        "affiliated_base_id": "affiliated_base_number" if have(tbl, "affiliated_base_number") else "NULL",
        "pickup_ts": pickup_col if have(tbl, pickup_col) else "NULL",
        "dropoff_ts": dropoff_col if have(tbl, dropoff_col) else "NULL",
        "passenger_count": "CAST(passenger_count AS INTEGER)" if have(tbl, "passenger_count") else "NULL",
        "trip_distance_mi": "CAST(trip_distance AS DOUBLE)" if have(tbl, "trip_distance") else "NULL",
        "rate_code_id": "CAST(RatecodeID AS INTEGER)" if have(tbl, "RatecodeID") else "NULL",
        "shared_ride_flag": "SR_Flag" if have(tbl, "SR_Flag") else "NULL",
        "store_and_fwd_flag": "store_and_fwd_flag" if have(tbl, "store_and_fwd_flag") else "NULL",
        "pickup_location_id": "CAST(PULocationID AS INTEGER)" if have(tbl, "PULocationID") else "NULL",
        "dropoff_location_id": "CAST(DOLocationID AS INTEGER)" if have(tbl, dropoff_loc) else "NULL",
        "payment_type": "CAST(payment_type AS INTEGER)" if have(tbl, "payment_type") else "NULL",
        "fare_amount": "fare_amount" if have(tbl, "fare_amount") else "NULL",
        "extra_fees": "extra" if have(tbl, "extra") else "NULL",
        "mta_tax": "mta_tax" if have(tbl, "mta_tax") else "NULL",
        "tip_amount": "tip_amount" if have(tbl, "tip_amount") else "NULL",
        "tolls_amount": "tolls_amount" if have(tbl, "tolls_amount") else "NULL",
        "total_amount": "total_amount" if have(tbl, "total_amount") else "NULL",
        "improvement_surcharge": "improvement_surcharge" if have(tbl, "improvement_surcharge") else "NULL",
        "congestion_surcharge": "congestion_surcharge" if have(tbl, "congestion_surcharge") else "NULL",
        "cbd_congestion_fee": "cbd_congestion_fee" if have(tbl, "cbd_congestion_fee") else "NULL",
        "airport_fee": "airport_fee" if have(tbl, "airport_fee") else "NULL",
        "dispatch_base_id": "dispatching_base_num" if have(tbl, "dispatching_base_num") else "NULL",
        "ehail_fee": "ehail_fee" if have(tbl, "ehail_fee") else "NULL",
        "hail_service_flag": "CAST(trip_type AS INTEGER)" if have(tbl, "trip_type") else "NULL"
    }

    field_list = ",\n        ".join(f"{v} AS {k}" for k, v in fields.items())

    target = {
        "yellow": "l1.fact_yellow_trips",
        "green": "l1.fact_green_trips",
        "fhv": "l1.fact_fhv_trips"
    }[service]

    sql = f"""
        INSERT INTO {target}
        SELECT
        {field_list},
        '{ingestion_month}' AS _ingestion_month,
        CURRENT_TIMESTAMP AS _l1_loaded_at,
        NULL AS _flag_null_passenger,
        NULL AS _flag_negative_fare,
        NULL AS _flag_invalid_distance
        FROM l0.{tbl};
    """

    con.execute(sql)
    print(f"✅ Loaded → {target}")

print("\n🚀 All L1 loads complete!")
