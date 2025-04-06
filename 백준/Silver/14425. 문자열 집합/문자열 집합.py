import sys
input = sys.stdin.readline

n, m = map(int, input().split())

valid_set = set(input().rstrip() for _ in range(n))

cnt = 0
for _ in range(m):
    if input().rstrip() in valid_set:
        cnt += 1
print(cnt)