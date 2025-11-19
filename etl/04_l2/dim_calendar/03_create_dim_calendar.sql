CREATE SCHEMA IF NOT EXISTS l2;

CREATE OR REPLACE TABLE l2.dim_calendar AS
WITH bounds AS (
    SELECT 
        MIN(pickup_date) AS min_date,
        MAX(pickup_date) AS max_date
    FROM l2.fact_trips
),
dates AS (
    SELECT d
    FROM bounds,
    UNNEST(generate_series(min_date, max_date, INTERVAL 1 DAY)) AS d(unnest)
)
SELECT
    d.unnest::DATE AS date,
    year(d.unnest) AS year,
    quarter(d.unnest) AS quarter,
    month(d.unnest) AS month,
    day(d.unnest) AS day,
    dayofweek(d.unnest) AS day_of_week,
    dayname(d.unnest) AS day_name,
    monthname(d.unnest) AS month_name,
    week(d.unnest) AS week_number,
    CASE WHEN dayofweek(d.unnest) IN (6, 7) THEN TRUE ELSE FALSE END AS is_weekend
FROM dates
ORDER BY date;
