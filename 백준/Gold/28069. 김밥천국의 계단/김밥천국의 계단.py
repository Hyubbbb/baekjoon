import sys
N, K = map(int, sys.stdin.readline().split())

# N <= K이면 무조건 가능

# N > K인 경우:
# 첫 번째 액션에서 순간이동을 택하면 '제자리 걸음' -> 즉, 최단거리 문제로 생각할 수 있다

dp = list(range(0, N+1)) # dp: 최단 이동 수 (일단 i+1로 이동한 것으로 세팅)

for i in range(1, N+1):
    # 액션 1: 한 걸음
    dp[i] = min(
        dp[i],
        dp[i-1]+1
    )
    
    # 액션 2: 순간이동
    if (i + i//2) <= N:
        dp[i + i//2] = min(
            dp[i + i//2],
            dp[i]+1
        )

print('minigimbob' if dp[N]<=K else 'water')