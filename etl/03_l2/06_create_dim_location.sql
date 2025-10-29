CREATE SCHEMA IF NOT EXISTS l2;

CREATE OR REPLACE TABLE l2.dim_location AS
SELECT 
    location_id,
    borough,
    zone,
    wkt
FROM l0.taxi_zone_lookup;
