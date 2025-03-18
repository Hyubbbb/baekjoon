import sys

n, m = map(int, sys.stdin.readline().split(' '))


bucket = list(range(1, n+1))

for i in range(m):
    i, j = map(int, sys.stdin.readline().split(' '))
    
    bucket[i-1:j], bucket[i-1:j][::-1] = bucket[i-1:j][::-1], bucket[i-1:j]
    # print(bucket[1-1:2])

print(*bucket)