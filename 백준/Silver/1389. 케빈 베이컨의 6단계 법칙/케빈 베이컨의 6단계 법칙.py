import sys
from collections import defaultdict, deque

input = sys.stdin.readline

N, M = map(int, input().split())

# 친구 그래프 만들기
friends = defaultdict(list)
for _ in range(M):
    u, v = map(int, input().split())
    friends[u].append(v)
    friends[v].append(u)

# BFS 함수 정의
def bfs(start):
    visited = [False] * (N+1)
    dist = [0] * (N+1)
    q = deque([start])
    visited[start] = True
    
    while q:
        cur = q.popleft()
        for neighbor in friends[cur]:
            if not visited[neighbor]:
                visited[neighbor] = True
                dist[neighbor] = dist[cur] + 1
                q.append(neighbor)
    return(sum(dist))

min_sum = float('inf')
ans = 0
for i in range(N, 0, -1):
    if bfs(i) <= min_sum:
        min_sum = bfs(i)
        ans = i

print(ans)