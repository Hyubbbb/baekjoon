import sys
input = sys.stdin.readline

n = int(input())

# 의견이 없는 경우
if n == 0:
    print(0)
# 일반적인 경우
else:
    scores = list(map(int, sys.stdin.read().splitlines()))

    # 오름차순 정렬
    scores = sorted(scores)

    # 제외할 사람 수
    n_trim = int(n * 0.15 + 0.5) # round를 쓰면 틀린다.. (오사오입 VS 사사오입)

    # 절사 평균 계산
    print(int(sum(scores[n_trim:(n-n_trim)]) / (n-2*n_trim) + 0.5))