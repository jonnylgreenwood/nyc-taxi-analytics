----------------------------------------------------
-- ✅ Add new cleaning/quality flags (Yellow)
----------------------------------------------------
ALTER TABLE l1.fact_yellow_trips
    ADD COLUMN IF NOT EXISTS _flag_impossible_distance BOOLEAN DEFAULT FALSE;

ALTER TABLE l1.fact_yellow_trips
    ADD COLUMN IF NOT EXISTS _flag_impossible_time BOOLEAN DEFAULT FALSE;

ALTER TABLE l1.fact_yellow_trips
    ADD COLUMN IF NOT EXISTS _flag_unreal_fare BOOLEAN DEFAULT FALSE;

----------------------------------------------------
-- ✅ Compute flag values (Yellow)
----------------------------------------------------
UPDATE l1.fact_yellow_trips
SET
    _flag_impossible_distance =
        (trip_distance_mi <= 0 OR trip_distance_mi > 100),

    _flag_impossible_time =
        (pickup_ts IS NULL OR dropoff_ts IS NULL OR pickup_ts >= dropoff_ts),

    _flag_unreal_fare =
        (fare_amount < 0 OR fare_amount > 1000);


----------------------------------------------------
-- ✅ Trim + normalize strings (Yellow)
----------------------------------------------------
UPDATE l1.fact_yellow_trips
SET
    store_and_fwd_flag = CASE
        WHEN store_and_fwd_flag IS NOT NULL
        THEN UPPER(TRIM(store_and_fwd_flag))
        ELSE NULL END,

    dispatch_base_id = NULLIF(UPPER(TRIM(dispatch_base_id)), ''),

    affiliated_base_id = NULLIF(UPPER(TRIM(affiliated_base_id)), '');


----------------------------------------------------
-- ✅ Standardize domain values (Yellow)
----------------------------------------------------
UPDATE l1.fact_yellow_trips
SET
    payment_type =
        CASE WHEN payment_type BETWEEN 1 AND 6 THEN payment_type ELSE NULL END,

    rate_code_id =
        CASE WHEN rate_code_id BETWEEN 1 AND 99 THEN rate_code_id ELSE NULL END;



----------------------------------------------------
-- ✅ Repeat for GREEN (same rules where applicable)
----------------------------------------------------
ALTER TABLE l1.fact_green_trips
    ADD COLUMN IF NOT EXISTS _flag_impossible_distance BOOLEAN DEFAULT FALSE;

ALTER TABLE l1.fact_green_trips
    ADD COLUMN IF NOT EXISTS _flag_impossible_time BOOLEAN DEFAULT FALSE;

ALTER TABLE l1.fact_green_trips
    ADD COLUMN IF NOT EXISTS _flag_unreal_fare BOOLEAN DEFAULT FALSE;

UPDATE l1.fact_green_trips
SET
    _flag_impossible_distance =
        (trip_distance_mi <= 0 OR trip_distance_mi > 100),
    _flag_impossible_time =
        (pickup_ts IS NULL OR dropoff_ts IS NULL OR pickup_ts >= dropoff_ts),
    _flag_unreal_fare =
        (fare_amount < 0 OR fare_amount > 1000),

    store_and_fwd_flag = CASE
        WHEN store_and_fwd_flag IS NOT NULL
        THEN UPPER(TRIM(store_and_fwd_flag))
        ELSE NULL END;



----------------------------------------------------
-- ✅ FHV (different rules — no fare or passenger metrics)
----------------------------------------------------
ALTER TABLE l1.fact_fhv_trips
    ADD COLUMN IF NOT EXISTS _flag_impossible_time BOOLEAN DEFAULT FALSE;

UPDATE l1.fact_fhv_trips
SET
    _flag_impossible_time =
        (pickup_ts IS NULL OR dropoff_ts IS NULL OR pickup_ts >= dropoff_ts),

    dispatch_base_id = NULLIF(UPPER(TRIM(dispatch_base_id)), ''),
    affiliated_base_id = NULLIF(UPPER(TRIM(affiliated_base_id)), '');

----------------------------------------------------
-- ✅ Done!
----------------------------------------------------
