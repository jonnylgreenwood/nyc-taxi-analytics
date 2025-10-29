COPY (SELECT * FROM l2.dim_calendar)
  TO 'data/pbi_data/dim_calendar.parquet' (FORMAT PARQUET);

COPY (SELECT * FROM l2.dim_payment_type)
  TO 'data/pbi_data/dim_payment_type.parquet' (FORMAT PARQUET);

COPY (SELECT * FROM l2.dim_rate_code)
  TO 'data/pbi_data/dim_rate_code.parquet' (FORMAT PARQUET);

COPY (SELECT * FROM l2.dim_location)
  TO 'data/pbi_data/dim_location.parquet' (FORMAT PARQUET);

-- COPY (
--     SELECT *
--     FROM l2.fact_trips
-- )
-- TO 'data/pbi_data/fact_trips'
-- (
--     FORMAT PARQUET,
--     PARTITION_BY (pickup_date),
--     COMPRESSION 'ZSTD'
-- );
