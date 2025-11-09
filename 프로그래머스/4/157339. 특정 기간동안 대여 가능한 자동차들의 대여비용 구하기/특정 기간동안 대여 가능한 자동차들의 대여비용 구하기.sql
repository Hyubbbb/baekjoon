-- 2022년 11월 1일부터 2022년 11월 30일까지 대여 불가능 찾기
WITH impossible_rental AS (
    SELECT DISTINCT
        car_id
    # *

    FROM car_rental_company_rental_history
    WHERE 1=1
        AND 
            -- Case 1
            ((start_date BETWEEN '2022-11-01' AND '2022-11-30') OR (end_date BETWEEN '2022-11-01' AND '2022-11-30'))
            -- Case 2
            OR 
            ((start_date <= '2022-11-01') AND (end_date >= '2022-11-01'))
)
SELECT
    crcc.car_id,
    crcc.car_type,
    ROUND(crcc.daily_fee * 30 * (1 - crcdp.discount_rate/100), 0) AS fee
FROM car_rental_company_car AS crcc
    JOIN car_rental_company_discount_plan AS crcdp
        ON crcc.car_type = crcdp.car_type
            AND crcdp.duration_type = '30일 이상'
WHERE 1=1
    AND crcc.car_type IN ('세단', 'SUV')
    AND crcc.car_id NOT IN (SELECT car_id FROM impossible_rental) -- 해당 기간 대여 가능 차량 필터링
    AND (ROUND(crcc.daily_fee * 30 * (1 - crcdp.discount_rate/100), 0) >= 500000) 
        AND (ROUND(crcc.daily_fee * 30 * (1 - crcdp.discount_rate/100), 0) < 2000000)
ORDER BY 
    fee DESC,
    car_type,
    car_id DESC