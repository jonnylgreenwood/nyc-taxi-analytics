INSTALL spatial;
LOAD spatial;

CREATE OR REPLACE TABLE l0.taxi_zone_lookup AS
SELECT * 
FROM ST_Read('data/taxi_zones/taxi_zones.shp');
