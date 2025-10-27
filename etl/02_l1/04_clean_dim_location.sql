CREATE SCHEMA IF NOT EXISTS l2;

CREATE OR REPLACE TABLE l2.dim_location AS
SELECT
    CAST(LocationID AS INTEGER) AS location_id,
    TRIM(Borough) AS borough,
    TRIM(Zone) AS zone,
    TRIM(service_zone) AS service_zone
FROM l0.taxi_zone_lookup;