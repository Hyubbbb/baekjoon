import sys

input = sys.stdin.readline

T = int(input()) # 테스트 케이스 개수

# DP
dp = [0] * 101 # N은 최대 100
dp[1], dp[2], dp[3] = 1, 1, 1

for i in range(4, 101):
    dp[i] = dp[i-3] + dp[i-2]

for _ in range(T):
    N = int(input())
    print(dp[N])