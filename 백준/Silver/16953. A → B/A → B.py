import sys
from collections import deque

input = sys.stdin.readline

A, B = map(int, input().split())

def bfs():
    queue = deque([])
    
    cnt = 0
    queue.append((A, cnt))
    
    while queue:
        num, cnt = queue.popleft()
        
        if num == B:
            return cnt+1
            
        # 연산 1
        if num * 2 <= B:
            queue.append((num * 2, cnt + 1))
        
        # 연산 2
        if num * 10 <= B:
            queue.append((num * 10 + 1, cnt + 1))
            
    return -1

print(bfs())