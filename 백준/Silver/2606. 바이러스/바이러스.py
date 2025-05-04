import sys
input = sys.stdin.readline

n = int(input()) # n: 컴퓨터 수 (100 이하의 양의 정수)
k = int(input()) # k: 네트워크 상에 '직접' 연결되어 있는 컴퓨터 쌍의 수

graph = [[] for _ in range(n+1)]
for _ in range(k):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (n+1)
visited[1] = True # 1번째 컴퓨터 감염

# Define dfs 
def dfs(x):
    if graph[x]:
        for i in graph[x]:
            if visited[i] == False:
                visited[i] = True
                dfs(i)

dfs(1)
print(sum(visited)-1) # 1번 컴퓨터는 제외한 값