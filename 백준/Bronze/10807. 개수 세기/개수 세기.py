import sys

N = int(sys.stdin.readline())
# print(N)

l = list(map(int, sys.stdin.readline().split(' ')))
# print(l)

v = int(sys.stdin.readline())
# print(v)

cnt = 0
for i in l:
    if i == v:
        cnt += 1
print(cnt)