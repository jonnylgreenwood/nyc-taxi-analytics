CREATE OR REPLACE TABLE l2.dim_payment_type AS
SELECT *
FROM (VALUES
    (1, 'Credit Card'),
    (2, 'Cash'),
    (3, 'No Charge'),
    (4, 'Dispute'),
    (5, 'Unknown'),
    (6, 'Voided Trip')
) AS t(payment_type, payment_desc);
