import sys
input = sys.stdin.readline

N, M, A, B = map(int, input().split())
INF = float('inf')

# DP 초기 세팅
dp = [INF] * (N+1)
dp[0] = 0

bound_set = set()
for _ in range(M):
    a, b = map(int, input().split())
    for i in range(a, b+1):
        bound_set.add(i)

# 닫힌 구간 설정
for i in bound_set:
    dp[i] = -1

# 점화식
for i in range(1, N+1):
    best = INF
    if dp[i] == -1:
        continue
    
    if i-A >= 0 and dp[i-A] != -1:
        best = min(best, dp[i-A] +1)
    if i-B >= 0 and dp[i-B] != -1:
        best = min(best, dp[i-B] +1)
    
    dp[i] = best if best != INF else -1
    
# print(dp)
print(dp[N])