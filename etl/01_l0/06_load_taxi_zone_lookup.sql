----------------------------------------------------
-- Load New York TLC Taxi Zone Shapefile → L0
----------------------------------------------------

INSTALL spatial;
LOAD spatial;

CREATE SCHEMA IF NOT EXISTS l0;

CREATE OR REPLACE TABLE l0.taxi_zone_lookup AS
SELECT
    CAST(LocationID AS INTEGER) AS location_id,
    TRIM(borough) AS borough,
    TRIM(zone) AS zone,
    ST_AsText(geom) AS wkt  -- ✅ st_astext is alias for st_aswkt in DuckDB
FROM st_read('data/taxi_zones/taxi_zones.shp');
