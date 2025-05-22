from itertools import combinations_with_replacement

n, m = map(int, input().split())

combo_list = list(combinations_with_replacement(range(1, n+1), m))

for combo in combo_list:
    print(*combo)