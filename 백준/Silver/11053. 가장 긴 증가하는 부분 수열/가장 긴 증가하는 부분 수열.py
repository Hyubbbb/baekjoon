import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

dp = [1] * n

for i in range(1, n):
    for j in range(0, i): # 본인 이전까지의 숫자들만 본다
        if nums[j] < nums[i]:
            dp[i] = max(dp[j]+1, dp[i])

print(max(dp))