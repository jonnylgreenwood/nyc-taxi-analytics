CREATE SCHEMA IF NOT EXISTS l0;

CREATE OR REPLACE TABLE l0.taxi_zone_lookup AS
SELECT *
FROM read_dbf('data/taxi_zones/taxi_zones.dbf');

DESCRIBE l0.taxi_zone_lookup;
SELECT * FROM l0.taxi_zone_lookup LIMIT 10;