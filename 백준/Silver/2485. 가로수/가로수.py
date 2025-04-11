import sys, math

input = sys.stdin.readline

n = int(input())

garosoos = list(map(int, [input() for _ in range(n)]))

garo_diff = []
for i in range(1, len(garosoos)):
    garo_diff.append(garosoos[i] - garosoos[i-1])

gcd = math.gcd(*garo_diff)

cnt = 0
for k in garo_diff:
    cnt += int((k/gcd)-1)
print(cnt)