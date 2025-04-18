import sys, math

a, b = map(int, sys.stdin.readline().split())

# 1. 최대공약수(Greatest Common Divisor)
print(math.gcd(a, b))

# 2. 최소공배수(Lowest Common Multiple)
print(math.lcm(a, b))