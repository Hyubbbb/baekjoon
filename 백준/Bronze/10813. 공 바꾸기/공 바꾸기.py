import sys

n, m = map(int, sys.stdin.readline().split(' '))

bucket = list(range(1, n+1))

for k in range(m):
    i, j = map(int, sys.stdin.readline().split(' '))
    bucket[i-1], bucket[j-1] = bucket[j-1], bucket[i-1]

print(*bucket)