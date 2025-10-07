# 자식이 없다면 자식 수는 0으로 출력
WITH t_child_cnt AS (
    SELECT
        parent_id,
        COUNT(*) AS tmp_child_count
    FROM ecoli_data
    WHERE 1=1 
        AND parent_id IS NOT NULL
    GROUP BY parent_id
)
SELECT 
    ed.id AS id,
    COALESCE(tcc.tmp_child_count, 0) AS child_count
FROM ecoli_data AS ed
    LEFT JOIN t_child_cnt AS tcc
        ON ed.id = tcc.parent_id
ORDER BY id