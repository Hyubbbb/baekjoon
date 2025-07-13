from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int,input().split())
graph = []

for _ in range(N):
    graph.append(list(map(int, list(input().rstrip()))))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS
def bfs(x, y):
    queue = deque()
    queue.append((x, y)) # 시작 위치
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 범위 확인
            if 0 <= nx < N and 0 <= ny < M:
                if graph[nx][ny] == 1:
                    graph[nx][ny] = graph[x][y] + 1
                    queue.append((nx, ny))
    return graph[N-1][M-1]

print(bfs(0, 0))