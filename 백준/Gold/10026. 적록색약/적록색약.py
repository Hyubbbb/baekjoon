import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
raw_graph = [list(input().rstrip()) for _ in range(N)]

graph = [row[:] for row in raw_graph]
graph_rg = [list(''.join(row).replace('R', 'G')) for row in raw_graph]

visited = [[False] * N for _ in range(N)]
visited_rg = [[False] * N for _ in range(N)]

def bfs(start_x, start_y, graph_, visited_):
    graph = graph_
    visited = visited_
    
    if visited[start_x][start_y]:
        return 0

    queue = deque([(start_x, start_y)])
    visited[start_x][start_y] = True
    cur = graph[start_x][start_y] # 현재 컬러
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < N and 0 <= ny < N:
                if not visited[nx][ny] and graph[nx][ny] == cur:
                    queue.append((nx, ny))
                    visited[nx][ny] = True
                    
    return(1)

# BFS 1: 적록색약 X
cnt = 0
for i in range(N):
    for j in range(N):
        cnt += bfs(i, j, graph, visited)
        
# BFS 2: 적록색약 O
cnt_rg = 0
for i in range(N):
    for j in range(N):
        cnt_rg += bfs(i, j, graph_rg, visited_rg)

print(cnt, cnt_rg)