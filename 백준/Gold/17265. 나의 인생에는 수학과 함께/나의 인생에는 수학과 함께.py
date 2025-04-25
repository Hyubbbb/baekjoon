import sys
input = sys.stdin.readline

n = int(input())

# 이동할 수 있는 경로
dy, dx = (1, 0), (0, 1)

def dfs(x, y, cur, op):
    '''
    x, y: 좌표
    cur: 지금까지 계산된 누적값
    op: 직전에 만난 연산자
    '''
    global max_ans, min_ans
    
    # 종료 조건
    if x == n-1 and y == n-1:
        max_ans = max(
            max_ans,
            int(cur)
        )
        min_ans = min(
            min_ans,
            int(cur)
        )
    
    # 아래 방향, 오른쪽 방향 탐색
    for k in range(2):
        nx = x + dx[k]
        ny = y + dy[k]

        # 0. 범위
        if nx < 0 or nx > n-1 or ny < 0 or ny > n-1:
            pass
        else:
            # 1. 다음칸이 숫자인 경우
            if graph[ny][nx].isdigit():
                dfs(nx, ny,
                    str(eval(cur + op + graph[ny][nx])),
                    '')
            # 2. 다음칸이 연산자인 경우
            else:
                dfs(nx, ny, 
                    cur, 
                    graph[ny][nx])
    

graph = [input().split() for _ in range(n)]

max_ans = -float('Inf')
min_ans = float('Inf')

dfs(0, 0, graph[0][0], '')
print(max_ans, min_ans)