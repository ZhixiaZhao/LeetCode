# Write your MySQL query statement below
SELECT product_name, SUM(o.unit) as unit
FROM Products p
LEFT JOIN Orders o on p.product_id = o.product_id
WHERE LEFT(o.order_date, 7) = "2020-02"
GROUP BY p.product_id
HAVING SUM(o.unit) >= 100