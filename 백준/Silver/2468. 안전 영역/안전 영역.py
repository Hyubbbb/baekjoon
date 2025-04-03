import sys
sys.setrecursionlimit(10**6)

n = int(input())

board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

# Define dfs()
def dfs(x, y, rain):
    visited[x][y] = True
    
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x+dx, y+dy
        
        if 0 <= nx < n and 0 <= ny < n:
            if not visited[nx][ny] and board[nx][ny] > rain:
                dfs(nx, ny, rain)


max_safe = 0
max_height = max(max(row) for row in board)

for rain in range(0, max_height+1):
    visited = [[False]*n for _ in range(n)]
    safe_cnt = 0
    
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and board[i][j] > rain:
                dfs(i, j, rain)
                safe_cnt += 1
    max_safe = max(max_safe, safe_cnt)
    
print(max_safe)