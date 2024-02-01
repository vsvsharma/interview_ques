--Problems URL(https://leetcode.com/problems/product-sales-analysis-iii/description/)
SELECT
    s.product_id,
    MIN(s.year) AS first_year,
    s.quantity,
    s.price
FROM
    Sales s
JOIN
    Product p ON s.product_id = p.product_id
WHERE
    (s.product_id, s.year) IN (
        SELECT
            product_id,
            MIN(year) AS first_year
        FROM
            Sales
        GROUP BY
            product_id
    )
GROUP BY
    s.product_id, s.year, s.quantity, s.price;