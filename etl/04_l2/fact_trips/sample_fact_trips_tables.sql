SELECT * FROM l2.fact_trips LIMIT 100;

SELECT source_type, _ingestion_month, COUNT(*) AS rows
FROM l2.fact_trips
GROUP BY 1, 2
ORDER BY 1, 2;