SELECT * FROM l1.fact_yellow_trips LIMIT 100;
SELECT * FROM l1.fact_green_trips LIMIT 100;
SELECT * FROM l1.fact_fhv_trips LIMIT 100;
SELECT _ingestion_month, COUNT(*) AS rows
FROM l1.fact_yellow_trips
GROUP BY 1
ORDER BY 1;