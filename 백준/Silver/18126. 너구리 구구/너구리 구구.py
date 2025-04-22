import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(u, dist):
    global ans
    visited[u] = True
    # 최대 거리 갱신
    if dist > ans:
        ans = dist
    # 인접 노드로 재귀 탐색
    for v, w in graph[u]:
        if not visited[v]:
            dfs(v, dist + w)

# 입력 및 그래프 구성
N = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

# 탐색 준비
visited = [False] * (N+1)
ans = 0

# 1번 노드(입구)에서 시작
dfs(1, 0)

# 결과 출력
print(ans)
