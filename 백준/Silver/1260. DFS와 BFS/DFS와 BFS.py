import sys
input = sys.stdin.readline
N, M, V = map(int, input().split()) # N: 정점의 개수, M: 간선의 개수, V: 탐색을 시작할 정점의 번호


# Graph
graph = [[] for _ in range(N+1)]
graph2 = [[] for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
    graph2[u].append(v)
    graph2[v].append(u)

# 내부 배열 오름차순 정렬
for adj in graph:
    adj.sort()

# 1. DFS
visited = [False]*(N+1)
result = []
def dfs(x):
    if x<1 or x>N:
        return
    if not visited[x]:
        visited[x] = True
        result.append(x) # 결과 순서 저장
    
        for w in graph[x]:
            if not visited[w]:
                dfs(w)

dfs(V)
print(*result)

# 2. BFS
from collections import deque

visited = [False]*(N+1)
result = []

# 내부 배열 오름차순 정렬
for adj in graph2:
    adj.sort()

def bfs(start):
    q = deque([start])
    visited[start] = True
    while q:
        x = q.popleft()
        print(x, end=' ')
        for w in graph2[x]:
            if not visited[w]:
                visited[w] = True
                q.append(w)

bfs(V)
print(*result)