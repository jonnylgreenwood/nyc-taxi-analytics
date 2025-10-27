import duckdb

con = duckdb.connect("etl/analytics.duckdb")

tables = con.execute("""
    SELECT table_name
    FROM information_schema.tables
    WHERE table_schema = 'l0'
      AND (
            table_name LIKE 'yellow_trip_%'
         OR table_name LIKE 'green_trip_%'
         OR table_name LIKE 'fhv_trip_%'
          );
""").fetchdf()['table_name']

for tbl in tables:
    service = tbl.split('_')[0]     # yellow / green / fhv
    year = tbl.split('_')[2]
    month = tbl.split('_')[3]
    ingestion_month = f"{year}_{month}"

    if service == "yellow":
        insert_sql = f"""
            INSERT INTO l1.fact_yellow_trips
            SELECT
                CAST(VendorID AS INTEGER),
                NULL,
                tpep_pickup_datetime,
                tpep_dropoff_datetime,
                CAST(passenger_count AS INTEGER),
                CAST(trip_distance AS DOUBLE),
                CAST(RatecodeID AS INTEGER),
                NULL,
                store_and_fwd_flag,
                CAST(PULocationID AS INTEGER),
                CAST(DOLocationID AS INTEGER),
                CAST(payment_type AS INTEGER),
                fare_amount,
                extra,
                mta_tax,
                tip_amount,
                tolls_amount,
                total_amount,
                improvement_surcharge,
                congestion_surcharge,
                cbd_congestion_fee,
                airport_fee,
                NULL,
                NULL,
                NULL,

                '{ingestion_month}',
                CURRENT_TIMESTAMP,
                passenger_count IS NULL,
                fare_amount < 0,
                trip_distance < 0
            FROM l0.{tbl};
        """

    # elif service == "green":
    #     insert_sql = f"""
    #         INSERT INTO l1.fact_green_trips
    #         SELECT
    #             CAST(VendorID AS INTEGER),
    #             NULL,
    #             lpep_pickup_datetime,
    #             lpep_dropoff_datetime,
    #             CAST(passenger_count AS INTEGER),
    #             CAST(trip_distance AS DOUBLE),
    #             CAST(RatecodeID AS INTEGER),
    #             NULL,
    #             store_and_fwd_flag,
    #             CAST(PULocationID AS INTEGER),
    #             CAST(DOLocationID AS INTEGER),
    #             CAST(payment_type AS INTEGER),
    #             fare_amount,
    #             extra,
    #             mta_tax,
    #             tip_amount,
    #             tolls_amount,
    #             total_amount,
    #             improvement_surcharge,
    #             congestion_surcharge,
    #             cbd_congestion_fee,
    #             airport_fee,
    #             NULL,
    #             NULL,
    #             CAST(trip_type AS INTEGER),

    #             '{ingestion_month}',
    #             CURRENT_TIMESTAMP,
    #             passenger_count IS NULL,
    #             fare_amount < 0,
    #             trip_distance < 0
    #         FROM l0.{tbl};
    #     """

    # elif service == "fhv":
    #     insert_sql = f"""
    #         INSERT INTO l1.fact_fhv_trips
    #         SELECT
    #             NULL,
    #             affiliated_base_number,
    #             pickup_datetime,
    #             dropoff_datetime,
    #             NULL,
    #             NULL,
    #             NULL,
    #             NULL,
    #             NULL,
    #             CAST(PULocationID AS INTEGER),
    #             CAST(DOLocationID AS INTEGER),
    #             NULL,
    #             NULL,
    #             NULL,
    #             NULL,
    #             NULL,
    #             NULL,
    #             NULL,
    #             NULL,
    #             NULL,
    #             NULL,
    #             dispatching_base_num,
    #             CAST(ehail_fee AS DOUBLE),
    #             NULL,

    #             '{ingestion_month}',
    #             CURRENT_TIMESTAMP,
    #             NULL,
    #             NULL,
    #             NULL
    #         FROM l0.{tbl};
    #     """

    else:
        continue

    print(f"Loading {tbl}...")
    con.execute(insert_sql)

print("✅ Load Complete!")
