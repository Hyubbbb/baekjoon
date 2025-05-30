import itertools

n, m = map(int, input().split())
arr = list(map(int, input().split()))

# 중복제거 + 정렬
arr = sorted(set(arr))

# 중복 순열, 오름차순, 중복은 안 된다
for comb in list(itertools.combinations_with_replacement(arr, m)):
    print(*comb)