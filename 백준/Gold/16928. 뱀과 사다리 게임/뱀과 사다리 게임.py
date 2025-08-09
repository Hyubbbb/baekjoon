import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split()) # 사다리의 수 N(1 ≤ N ≤ 15) / 뱀의 수 M(1 ≤ M ≤ 15)

jump = {}
# 사다리 & 뱀 정보
for _ in range(N+M):
    x, y = map(int, input().split())
    jump[x] = y

# 맵
visited = [-1] * 101

def bfs():
    # 시작점 설정
    queue = deque([1])
    visited[1] = 0
    
    while queue:
        u = queue.popleft()
    
        # 주사위 1~6
        for i in range(1, 7):
            nu = u + i
            nu = jump.get(nu, nu)
            
            if visited[nu] < 0: # 방문한 적 없으면
                visited[nu] = visited[u] + 1
                queue.append(nu)
                
                if nu == 100:
                    return(visited[nu])

print(bfs())