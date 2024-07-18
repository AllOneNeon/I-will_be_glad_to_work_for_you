SELECT DATE_TRUNC('month', DATE) AS month,
       STATUS,
       COUNT(*) AS order_count
FROM public."SALES"
GROUP BY month, STATUS
ORDER BY month, STATUS;