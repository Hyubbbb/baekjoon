# push X: 정수 X를 큐에 넣는 연산이다.
# pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 큐에 들어있는 정수의 개수를 출력한다.
# empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
# front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.

import sys
from collections import deque

input = sys.stdin.readline
n = int(input())

def run_prompt(x, queue):
    if x[0] == 'push':
        queue.append(x[1])
    if x[0] == 'pop':
        if len(queue)==0:
            return print(-1)
        else:
            return print(queue.popleft())
    if x[0] == 'size':
        return print(len(queue))
    if x[0] == 'empty':
        if len(queue)==0:
            return print(1)
        else:
            return print(0)
    if x[0] == 'front':
        if len(queue)==0:
            return print(-1)
        else:
            return print(queue[0])
    if x[0] == 'back':
        if len(queue)==0:
            return print(-1)
        else:
            return print(queue[-1])

queue = deque([])

for _ in range(n):
    prompt = list(input().split())
    run_prompt(prompt, queue)