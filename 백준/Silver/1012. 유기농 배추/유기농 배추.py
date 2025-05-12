import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

T = int(input())

def dfs(x, y):
    # 범위를 벗어나는 경우 return
    if x < 0 or x > M-1 or y < 0 or y > N-1:
        return
    if not graph[y][x]:
        return
    graph[y][x] = False
    dfs(x, y-1) # 상
    dfs(x, y+1) # 하
    dfs(x-1, y) # 좌
    dfs(x+1, y) # 우
    

for _ in range(T):
    M, N, K = map(int, input().split()) # M: 가로 길이, N: 세로 길이, K: 배추 개수(최소 1개는 있다)
    graph = [[False]*M for _ in range(N)]
    for _ in range(K):
        x, y = map(int, input().split())
        graph[y][x] = True
    
    # dfs
    cnt = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j]:
                dfs(j, i)
                cnt += 1
        
    print(cnt)