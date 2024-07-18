SELECT
    to_char(DATE, 'YYYY-MM') AS month,
    SUM(AMOUNT) OVER (ORDER BY DATE) AS cumulative_units
FROM public."SALES"
WHERE STATUS = 'Оплачено'
ORDER BY month;