CREATE OR REPLACE TABLE l2.dim_rate_code AS
SELECT *
FROM (VALUES
    (1, 'Standard Rate'),
    (2, 'JFK'),
    (3, 'Newark'),
    (4, 'Nassau or Westchester'),
    (5, 'Negotiated Fare'),
    (6, 'Group Ride')
) AS t(rate_code_id, rate_code_desc);
