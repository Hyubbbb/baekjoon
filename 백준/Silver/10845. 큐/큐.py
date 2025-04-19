import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

dq = deque()
for _ in range(n):
    prompt = input().split()

    if prompt[0] == 'push':
        dq.append(prompt[1])

    if prompt[0] == 'pop':
        print(dq.popleft() if dq else -1)

    if prompt[0] == 'size':
        print(len(dq))

    if prompt[0] == 'empty':
        print(0 if dq else 1)

    if prompt[0] == 'front':
        print(dq[0] if dq else -1)

    if prompt[0] == 'back':
        print(dq[-1] if dq else -1)