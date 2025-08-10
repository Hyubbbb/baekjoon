import sys
input = sys.stdin.readline

N = int(input())

triangle = [list(map(int, input().split())) for _ in range(N)]

dp = [[0]*N for _ in range(N)]
dp[0][0] = triangle[0][0]

for i in range(1, N):
    for j in range(i+1):
        # 맨 왼쪽으로 내려온 경우
        if j == 0:
            dp[i][0] = dp[i-1][0] + triangle[i][0]
        # 맨 오른쪽으로 내려온 경우
        elif j == i:
            dp[i][j] = dp[i-1][j-1] + triangle[i][j]
        # 그 외 경우: max(대각선 오른쪽 아래로 내려온 경우, 대각선 왼쪽 아래로 내려온 경우)
        else:
            dp[i][j] = max(dp[i-1][j-1] + triangle[i][j],
                           dp[i-1][j] + triangle[i][j])
print(max(dp[N-1]))