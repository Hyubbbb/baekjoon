import sys

s = set(range(1, 31))
# print(s)

data = set(map(int, sys.stdin.read().splitlines()))
# print(data)

s_sorted = sorted(s - data)
# print(s_sorted)

for i in s_sorted:
    print(i)