--Problem: The Operation team wants to knonw which dates in january 2025 has no orders
WITH dates AS(
    SELECT generate_series('2025-01-01'::date, '2025-01-31'::date, interval '1 day') AS day
)
SELECT day
FROM dates
WHERE NOT EXISTS(
    SELECT 1
    FROM orders
    WHERE order_date=day
)