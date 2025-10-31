INSTALL spatial;
LOAD spatial;

CREATE OR REPLACE TABLE l1.dim_location AS
SELECT
    LocationID AS location_key,
    borough AS borough_name,
    zone AS zone_name,
    ST_Y(ST_Centroid(geom)) AS latitude,
    ST_X(ST_Centroid(geom)) AS longitude,
    ST_AsText(geom) AS wkt
FROM l0.taxi_zone_lookup;