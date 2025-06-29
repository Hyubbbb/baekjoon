import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

N, M = map(int, input().split()) # N: 정점의 개수, M: 간선의 개수

# 초기 그래프 세팅
graph = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False]*(N+1)

# DFS
def dfs(x):
    visited[x] = True
    for v in graph[x]:
        if not visited[v]:
            dfs(v)

cnt = 0
for i in range(1, N+1):
    if not visited[i]:
        dfs(i)
        cnt += 1

print(cnt)