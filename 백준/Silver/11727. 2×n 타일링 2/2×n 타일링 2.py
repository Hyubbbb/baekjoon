n = int(input()) # n은 1이상 1000이하

# 1. DP 초기값 설정
dp = [0] * 1001
dp[1] = 1
dp[2] = 3

# 2. DP
for i in range(3, 1001):
    dp[i] = dp[i-1] + 2 * dp[i-2]

# 2. 10007로 나눈 나머지 출력
print(dp[n]%10007)