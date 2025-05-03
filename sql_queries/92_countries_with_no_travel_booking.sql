/*
Find the countries with no bookings in a month
There are 2 tables: countries, bookings. So i'm using left join to check the countries with 
no match in the booking table.
*/
SELECT c.country_name
FROM countries
LEFT JOIN bookings b 
ON c.country_id=b.country_id
AND b.booking_date BETWEEN '2025-01-01' AND '2025-01-31'
WHERE b.booking_id IS NULL;