/*1. You're working for an e-commerce company that wants to understand customer spending behaviour 
over time
2. Problem statement : For weach customer, calculate the cumulative amount spent across all the orders,
ordered by date of purchase.
3. Can we see how much each customer has spent over time, with a running total that grows with each
order they make
*/
SELECT customer_id, order_date, amount,
    SUM(amount) OVER (
        PARTITION BY customer_id
        ORDER BY order_date
    ) AS running_total
FROM orders;

