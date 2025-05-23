from itertools import permutations

n, m = map(int, input().split())

n_list = list(map(int, input().split()))
n_list = sorted(n_list)
# 수열 순차 출력
for perm in list(permutations(n_list, m)):
    print(*perm)