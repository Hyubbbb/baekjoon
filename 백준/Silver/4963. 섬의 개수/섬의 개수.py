import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(x, y):
    # visited[x][y] = True
    board[x][y] = False
    
    for dx, dy in [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]:
        nx, ny = x+dx, y+dy
        
        if 0<=nx<h and 0<=ny<w:
            if board[nx][ny]:
                dfs(nx, ny)

while True:
    w, h = map(int, input().split())
    if w==0 and h==0:
        break
    
    # 1. 지도 파악
    board = []
    for _ in range(h):
        board.append(list(map(int, input().split())))
    
    # # 2. visited 세팅
    # visited = [[False]*w]*h
    
    # 3. DFS
    cnt = 0
    for i in range(h):
        for j in range(w):
            if board[i][j]:
                dfs(i, j)
                cnt += 1        

    print(cnt)