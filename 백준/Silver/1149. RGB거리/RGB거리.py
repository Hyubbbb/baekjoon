import sys
input = sys.stdin.readline

n = int(input())

dp = [[0, 0, 0] for _ in range(n+1)]
# print(dp)

# 초기값 세팅
cost = list(map(int, input().split()))
dp[1] = [cost[0], cost[1], cost[2]]

# DP
for i in range(2, n+1):
    cost = list(map(int, input().split())) # cost[0], cost[1], cost[2]: R, G, B
    
    # Red
    dp[i][0] = min(
        dp[i-1][1] + cost[0], # 이전 색이 G인 경우
        dp[i-1][2] + cost[0]  # 이전 색이 B인 경우
    )
    # Green
    dp[i][1] = min(
        dp[i-1][0] + cost[1], # 이전 색이 R인 경우
        dp[i-1][2] + cost[1]  # 이전 색이 B인 경우
    )
    # Blue
    dp[i][2] = min(
        dp[i-1][0] + cost[2], # 이전 색이 R인 경우
        dp[i-1][1] + cost[2]  # 이전 색이 G인 경우
    )

print(min(dp[n]))