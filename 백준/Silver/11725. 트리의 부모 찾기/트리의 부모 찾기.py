import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n = int(input())

# adj 생성
adj = [[] for _ in range(n+1)]
parents = [0] * (n+1)
for _ in range(n-1):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

# DFS
def dfs(curr):
    for next_node in adj[curr]:
        if parents[next_node] == 0:
            parents[next_node] = curr
            dfs(next_node)

parents[1] = -1
dfs(1)

print('\n'.join(map(str, parents[2:])))