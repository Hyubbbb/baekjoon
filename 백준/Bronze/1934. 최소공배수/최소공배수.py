import sys
input = sys.stdin.readline

n = int(input())


# # Sol1: 시간 초과
# for _ in range(n):
#     a, b = map(int, input().split())
    
#     for i in range(1, a+1):
#         num = b*i
#         if (num%a == 0) and (num%b == 0):
#             print(num)
#             break

# Sol2: GCD 이용
import math

for _ in range(n):
    a, b = map(int, input().split())
    
    gcd = math.gcd(a, b)
    lcm = int(a*b / gcd)
    print(lcm)