"""
M: 상자의 가로 칸의 수
N: 상자의 세로 칸의 수
H: 상자의 수
"""

import sys
from collections import deque
input = sys.stdin.readline

M, N, H = map(int, input().split())

graph = []
for h in range(H):
    graph.append([list(map(int, input().split())) for _ in range(N)])

# 익은 토마토 좌표 저장
ripen = deque([])
for h in range(H):
    for i in range(N):
        for j in range(M):
            if graph[h][i][j] == 1:
                ripen.append((h, i, j))

# Define BFS
def bfs(start_h, start_x, start_y):
    # 위, 아래, 왼쪽, 오른쪽, 앞, 뒤
    dh = [-1, 1, 0, 0, 0, 0]
    dx = [0, 0, 0, 0, -1, 1]
    dy = [0, 0, -1, 1, 0, 0]
    
    for i in range(6):
        nh = start_h + dh[i]
        nx = start_x + dx[i]
        ny = start_y + dy[i]
    
        if 0 <= nh < H and 0 <= nx < N and 0 <= ny < M and graph[nh][nx][ny] == 0:
            graph[nh][nx][ny] = graph[start_h][start_x][start_y] + 1
            ripen.append((nh, nx, ny))

# Run BFS
while ripen:
    start_h, start_x, start_y = ripen.popleft()
    bfs(start_h, start_x, start_y)

# Print Result
result_date = 0
failed_flag = False

for h in range(H):
    for i in range(N):
        for j in range(M):
            if graph[h][i][j] == 0:
                failed_flag = True
                result_date = 0
                break
            else:
                result_date = max(result_date, graph[h][i][j])
        if failed_flag:
            break
    if failed_flag:
        break
print(result_date - 1)