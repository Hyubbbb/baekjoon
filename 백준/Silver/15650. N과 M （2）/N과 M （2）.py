from itertools import combinations

n, m = map(int, input().split())

_list = list(range(1, n+1))

comb_list = list(combinations(_list, m))
for num in comb_list:
    print(*num)