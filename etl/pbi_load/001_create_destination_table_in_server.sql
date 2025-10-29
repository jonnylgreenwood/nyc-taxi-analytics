INSTALL postgres_scanner;
LOAD postgres_scanner;

SELECT *
FROM postgres_scan(
    'host=localhost port=5433 user=userpg password=passpg dbname=nyc_pg',
    'SELECT 1',
    'public'
);
