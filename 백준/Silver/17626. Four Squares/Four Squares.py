import math
n = int(input())

# DP인가?
N = 50000
dp = [0] * (N+1)
dp[0] = 0

for i in range(1, n+1):
    dp[i] = min([dp[i - j**2] + 1 for j in range(1, math.isqrt(i)+1)])

print(dp[n])