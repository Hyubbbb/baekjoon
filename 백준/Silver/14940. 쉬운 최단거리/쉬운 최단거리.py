from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split()) # n: 세로, m: 가로

graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
steps = [[0] * m for _ in range(n)]

# 시작점 찾기
for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            sx = i
            sy = j

# BFS
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

queue = deque([])

def bfs(start_x, start_y):
    queue.append((start_x, start_y))
    visited[start_x][start_y] = True
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 범위 체크
            if 0 <= nx < n and 0 <= ny < m:
                # 갈 수 있는 곳인지, 간 적 있는지 체크
                if not visited[nx][ny] and graph[nx][ny] == 1:
                    visited[nx][ny] = True
                    steps[nx][ny] = steps[x][y] + 1
                    queue.append((nx, ny))
    
    # 갈 수 있는데, 도달하지 못한 곳 체크
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and graph[i][j] == 1:
                steps[i][j] = -1

bfs(sx, sy)
for step in steps:
    print(*step)