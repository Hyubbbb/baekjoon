import sys
input = sys.stdin.readline

N, M, B = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]

ans_time = sys.maxsize
ans_floor = 0

for floor in range(257):
    exceed_block = 0
    lacked_block = 0
    time = 0
    inventory = B
    
    # 목표까지의 블럭 개수 세기
    for i in range(N): # 세로
        for j in range(M): # 가로
            gap = floor - board[i][j] # 목표 높이 - 현재 높이
            if gap > 0:
                lacked_block += gap
            else:
                exceed_block += abs(gap)
    
    # 블럭 초과분 제거 후, 인벤토리에 저장
    time += exceed_block * 2
    inventory += exceed_block
    
    # 블럭 부족분 쌓을 준비
    if lacked_block > inventory:
        break
    else:
        time += lacked_block
    
    if ans_time >= time:
        ans_floor = floor
        ans_time = min(ans_time, time)
        
print(ans_time, ans_floor)