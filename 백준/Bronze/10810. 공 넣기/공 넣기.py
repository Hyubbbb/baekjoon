import sys

n, m = map(int, input().split(' '))

bucket = [0] * n
# bucket = [1, 2, 3, 4, 5]

for i in range(m):
    i, j, k = map(int, sys.stdin.readline().split(' '))
    # print(i, j ,k)
    # print(bucket[i-1:j])
    bucket[i-1:j] = [k] * (j-i+1)
    # print(bucket[i-1:j])

# for j in bucket:
#     print(j, end=' ')

print(*bucket)