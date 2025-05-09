n = int(input())

'''
목표: 2xn 크기의 직사각형을 채우기

타일
1. 1x2
2. 2x1
'''
N = 1001 # max(n) = 1000

dp = [0] * N

dp[1] = 1
dp[2] = 2

for i in range(3, N):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[n] % 10007)

# DP라는 느낌은 왔으나, 힌트 없이 이렇게 생각할 수 있을까 싶다