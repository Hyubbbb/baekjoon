import sys
n = int(input())

min_x = 10000
max_x = -10000
min_y = 10000
max_y = -10000

for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    
    if min_x >= x:
        min_x = x
    if min_y >= y:
        min_y = y
    if max_x <= x:
        max_x = x
    if max_y <= y:
        max_y = y

print((max_x-min_x) * (max_y-min_y))