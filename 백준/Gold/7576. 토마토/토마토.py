import sys
from collections import deque

input = sys.stdin.readline

M, N = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(N)]

"""
1: 익은 토마토
0: 익지 않은 토마토
-1: 은 토마토가 들어있지 않은 칸
"""

# 익은 토마토 좌표
ripen = deque([])
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            ripen.append((i, j))

# BFS
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(start_x, start_y):
    for i in range(4):
        nx = start_x + dx[i]
        ny = start_y + dy[i]
        if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 0:
            graph[nx][ny] = graph[start_x][start_y] + 1
            ripen.append((nx, ny))

while ripen:    
    start_x, start_y = ripen.popleft()
    bfs(start_x, start_y)

ans = 0
found = False
for row in graph:
    for r in row:
        if r == 0:
            ans = 0
            found = True
            break
        else:
            ans = max(ans, r)
    if found:
        break
print(ans - 1)