--Problems URL(https://leetcode.com/problems/immediate-food-delivery-ii/description/)
WITH FirstOrders AS (
    SELECT
        customer_id,
        MIN(order_date) AS first_order_date
    FROM
        Delivery
    GROUP BY
        customer_id
)

SELECT
    ROUND(
        AVG(
            CASE
                WHEN d.order_date = fo.first_order_date 
                     AND d.customer_pref_delivery_date = d.order_date 
                THEN 1
                ELSE 0
            END
        ) * 100,
        2
    ) AS immediate_percentage
FROM
    FirstOrders fo
JOIN
    Delivery d ON fo.customer_id = d.customer_id
WHERE
    d.order_date = fo.first_order_date;
