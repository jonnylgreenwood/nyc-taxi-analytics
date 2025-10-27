SELECT * FROM l2.fact_trips LIMIT 100;

SELECT _ingestion_month, COUNT(*) AS rows
FROM l2.fact_trips
GROUP BY 1
ORDER BY 1;