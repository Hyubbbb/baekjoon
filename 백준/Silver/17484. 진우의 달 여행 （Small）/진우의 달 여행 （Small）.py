import sys
input = sys.stdin.readline

N, M = map(int, input().split())
INF = float('inf')

map = [list(map(int, input().split())) for _ in range(N)]

dp = [[[INF] * 3 for _ in range(M)] for _ in range(N)] # dp[i][j][d]: i행 j열에 d 방향으로 도착했을 때 최소 연료의 합 
'''
d=0: 좌
d=1: 중
d=2: 우
'''

# 출발점
for j in range(M):
    dp[0][j] = [map[0][j]]*3

# 이동해보자
for i in range(1, N):
    for j in range(0, M):
        for d in range(3):
            # d: 0(좌), 1(중), 2(우)
            nj = j+(d-1)
            if 0 <= nj < M:
                for prev_d in range(3):
                    if prev_d != d:
                        # 현재 지점 비용 + 이전 경로까지 비용
                        dp[i][j][d] = min(dp[i][j][d], 
                                          dp[i-1][nj][prev_d] + map[i][j]) # prev_d에 따른 최솟값 저장

print(min(min(dp[N-1][j]) for j in range(M)))