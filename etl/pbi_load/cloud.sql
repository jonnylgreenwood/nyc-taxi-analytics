INSTALL postgres_scanner;
LOAD postgres_scanner;

CALL postgres_attach(
  'host=localhost port=5432 user=postgres password=postgres dbname=nyc_pg',
  FALSE,
  'public',
  TRUE,
  'pg',
  ''
);
