import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

graph = [list(map(int, list(input().rstrip()))) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
cnts = [] # 각 단지 내 아파트 수 카운트 용

# Define BFS
def bfs(start_x, start_y):
    queue = deque([])
    queue.append((start_x, start_y))
    visited[start_x][start_y] = True
    cnt = 1 # 단지 내 아파트 수
    
    # 상 하 좌 우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<=nx<N and 0<=ny<N:
                if graph[nx][ny] and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                    cnt += 1
    cnts.append(cnt)

# Run BFS
for i in range(N):
    for j in range(N):
        if graph[i][j] and not visited[i][j]:
            bfs(i, j)

# Print
cnts = sorted(cnts) # 오름차순 정렬

# 1. 총 단지수
print(len(cnts)) 

# 2. 단지 별 아파트 수
for cnt in cnts:
    print(cnt)