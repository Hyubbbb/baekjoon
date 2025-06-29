import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())

graph = [list(input().rstrip()) for _ in range(N)]
# print(graph)
visited = [[False] * M for _ in range(N)]

# 도연이 찾기
position = [[i, j] for i, row in enumerate(graph)
                   for j, value in enumerate(row)
                   if value == 'I']

def dfs(x, y):
    global cnt
    visited[x][y] = True
    
    if graph[x][y] == 'P':
        cnt += 1
    
    # 상하좌우
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if (0 <= nx < N) and (0 <= ny < M) and visited[nx][ny] == False:
            if graph[nx][ny] != 'X':
                dfs(nx, ny)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
cnt = 0

dfs(position[0][0], position[0][1])
if cnt == 0:
    print('TT')
else:
    print(cnt)

"""
1. 상하좌우는 dx, dy 리스트로 쉽게 바꿀 수 있다
"""