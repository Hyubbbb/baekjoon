import sys
input = sys.stdin.readline

n = int(input()) # n: 계단의 총 개수

scores = [0]
scores += [int(input()) for _ in range(n)]
# print(scores)

dp = [0]* (n+1)
dp[0] = 0 # 0번째: 출발점
dp[1] = scores[1] # 1번째는 출발점에서 오는 방법 뿐

for i in range(2, n+1):
    dp[i] = max(
        dp[i-3] + scores[i-1] + scores[i], # 1) 한 칸 오르기
        dp[i-2] + scores[i] # 2) 두 칸 오르기
    )

print(dp[-1])