SELECT NAME
FROM (
    SELECT c.NAME, COUNT(o.ROW_ID) AS order_count
    FROM public."CLIENTS" c
    LEFT JOIN public."SALES" o ON c.CLIENTS_ID = o.ROW_ID
    GROUP BY c.CLIENTS_ID
) AS customer_orders
ORDER BY order_count ASC
LIMIT 1;