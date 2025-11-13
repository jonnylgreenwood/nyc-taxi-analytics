-- Confirm tables exist
SELECT table_schema, table_name
FROM information_schema.tables
WHERE table_schema = 'l0'
ORDER BY table_name;

-- Profile example table

SELECT *
FROM l0.yellow_trip_2025_09
LIMIT 100;