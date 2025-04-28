/* Find the top 2 selling products in each category
Approach: We need to rank products within each category, bases on total_sales. Then filter only top 
two ranks.
*/
WITH ranked_products AS(
    SELECT *, 
        DENSE_RANK() OVER(PARTITION BY category ORDER BY total_sales DESC) AS rnk
    FROM product_sales
)
SELECT category, product, total_sales
FROM ranked_products
WHERE rnk <=2;