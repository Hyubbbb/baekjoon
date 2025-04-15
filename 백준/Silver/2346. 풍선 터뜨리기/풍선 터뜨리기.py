import sys
from collections import deque

input = sys.stdin.readline
n = int(input())

dq = deque(enumerate(map(int, input().split())))

result = []
while dq:
    idx, val = dq.popleft()
    result.append(idx+1) # 터진 풍선 저장
    
    if val>0:
        dq.rotate(-val+1)
    else:
        dq.rotate(-val)

print(*result)


# 큐에도 enumerate를 쓸 수 있다