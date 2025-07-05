from collections import deque
import sys

sys.setrecursionlimit(10**6)

N, K = map(int, input().split())

max_num = 10 ** 5
visited = [False] * (max_num+1)
dist = [0] * (max_num+1)

def bfs(start):
    q = deque([start])
    
    while q:
        cur = q.popleft()
        
        # 정답인 경우, 거리를 반환
        if cur == K:
            return(dist[cur])
        
        # 정답이 아닌 경우, 경로 탐색
        for neighbor in (cur-1, cur+1, 2*cur):
            if 0 <= neighbor <= max_num and not visited[neighbor]:
                visited[neighbor] = True
                dist[neighbor] = dist[cur] + 1
                q.append(neighbor)
print(bfs(N))