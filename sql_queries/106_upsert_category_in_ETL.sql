-- We have staging table with updated product prices. Now we have to upsert into the products table

-- Deleting any matching records
DELETE FROM products
WHERE product_id IN (SELECT product_id FROM staging_products);

--updating the record
INSERT INTO products
SELECT * FROM staging_products