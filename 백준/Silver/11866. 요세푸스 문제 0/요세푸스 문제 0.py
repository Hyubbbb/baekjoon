import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())

deque = deque([i for i in range(1, n+1)])

stack = []
while deque:
    for _ in range(k-1):
        tmp = deque.popleft()
        deque.append(tmp)
    stack.append(deque.popleft())

print('<', ', '.join(map(str, stack)), '>', sep='')