# 식당 ID, 식당 이름, 음식 종류, 즐겨찾기수, 주소, 리뷰 평균 점수


# WITH avg_rating AS (
#     SELECT 
#         rest_id,
#         ROUNT(AVG(REVIEW_SCORE), 2) AS score
#     FROM rest_review
#     GROUP BY rest_id
# )

# 1. GROUP BY 될지 보자
# SELECT
#     rest_id,
#     rest_name,
#     food_type,
#     favorites,
#     address

SELECT 
    ri.rest_id,
    ri.rest_name,
    ri.food_type,
    ri.favorites,
    ri.address,
    ROUND(AVG(rr.review_score), 2) AS score
FROM rest_info AS ri
JOIN rest_review AS rr
    ON ri.rest_id = rr.rest_id
WHERE address LIKE '서울%'
GROUP BY ri.rest_id, ri.rest_name, ri.food_type, ri.favorites, ri.address
ORDER BY score DESC, favorites DESC