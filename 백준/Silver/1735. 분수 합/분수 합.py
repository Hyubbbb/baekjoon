import sys, math
input = sys.stdin.readline

a, b = map(int, input().split())
c, d = map(int, input().split())

tmp1 = a*d + b*c
tmp2 = b*d
gcd = math.gcd(tmp1, tmp2)

tmp1, tmp2 = map(int, [tmp1/gcd, tmp2/gcd])
print(tmp1, tmp2)