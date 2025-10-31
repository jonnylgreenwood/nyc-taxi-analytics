CREATE OR REPLACE TABLE l2.fact_trips AS with nfhv AS (
        SELECT *
        FROM l2.fact_trips
        WHERE source_type != 'fhv'
    ),
    fhv AS (
        SELECT *
        FROM l2.fact_trips
        WHERE source_type = 'fhv'
    ),
    ---    Quality filter
    d AS (
        SELECT *
        FROM fhv
        UNION ALL
        SELECT *
        FROM nfhv
        WHERE (
                passenger_count > 1
                AND passenger_count <= 6
            )
            AND (
                trip_distance_mi > 0
                AND trip_distance_mi < 500
            )
            AND (
                (
                    trip_duration_minutes > 0
                    AND trip_duration_minutes < 1440
                )
            )
            AND (speed_mph < 100)
    )
SELECT *
FROM d;
CREATE OR REPLACE TABLE l2.fact_trips_rejected AS (
        SELECT *
        FROM l2.fact_trips
        WHERE NOT (
                passenger_count > 1
                AND passenger_count <= 6
            )
            AND (
                trip_distance_mi > 0
                AND trip_distance_mi < 500
            )
            AND (
                (
                    trip_duration_minutes > 0
                    AND trip_duration_minutes < 1440
                )
            )
            AND (speed_mph < 100)
    )