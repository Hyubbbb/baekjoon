import sys
input = sys.stdin.readline

n, m = map(int, input().split())

# 1. 듣못
set_hear = set()
set_see = set()
for _ in range(n):
    set_hear.add(input().rstrip())
# 2. 보못
for _ in range(m):
    set_see.add(input().rstrip())

set_hs = set_hear.intersection(set_see)
print(len(set_hs))
print('\n'.join(sorted(set_hs)))