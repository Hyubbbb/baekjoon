WITH total_order AS (
    SELECT
        flavor,
        total_order
    FROM first_half

    UNION ALL 

    SELECT
        flavor,
        total_order
    FROM july
)

SELECT 
    flavor
    # SUM(total_order)
FROM total_order
GROUP BY flavor
ORDER BY SUM(total_order) DESC
LIMIT 3




#     FULL OUTER JOIN july AS j
#         ON fh.shipment_id = j.shipment_id
# ORDER BY (fh.total_order + j.total_order) DESC
# LIMIT 3