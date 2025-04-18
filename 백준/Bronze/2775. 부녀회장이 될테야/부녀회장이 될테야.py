import sys

input = sys.stdin.readline

t = int(input())


all_k = []
all_n = []
for _ in range(t):
    all_k.append(int(input())) # 층
    all_n.append(int(input())) # 호
    
# dp[k][n] # k층 n호에 사는 사람 수
max_k = max(all_k)
max_n = max(all_n)
dp = [[0]*(max_n+1) for _ in range(max_k+1)]

# 0층은 모두 1명 거주
for n in range(1, max_n+1):
    dp[0][n] = n

# 전층 1호는 모두 1명 거주
for k in range(0, max_k+1):
    dp[k][1] = 1


# Let's dp (1층부터 DP해도 되지 않나?)
for k in range(1, max_k+1):
    for n in range(2, max_n+1):
        dp[k][n] = dp[k][n-1] + dp[k-1][n]

# 결과 출력
for i in range(t):
    print(dp[all_k[i]][all_n[i]])