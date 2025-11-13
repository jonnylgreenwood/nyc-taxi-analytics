INSTALL spatial;
LOAD spatial;

CREATE OR REPLACE TABLE l1.dim_location AS
SELECT
    LocationID AS location_key,
    FIRST(borough) AS borough_name,
    FIRST(zone) AS zone_name,
    ST_Y(ST_Centroid(ST_Union_Agg(geom))) AS latitude,
    ST_X(ST_Centroid(ST_Union_Agg(geom))) AS longitude,
    ST_AsText(ST_Union_Agg(geom)) AS wkt
FROM l0.taxi_zone_lookup
GROUP BY LocationID;
