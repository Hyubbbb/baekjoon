import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
orig = deque(range(1, n+1)) # 1부터 n까지의 수
nums = list(map(int, sys.stdin.read().splitlines())) # 만들어야 하는 수열

stack = []
stack_sign = []

for i in nums:
    while stack or orig:
        if stack and stack[-1] == i:
            stack.pop()
            stack_sign.append('-')
            break
        else:
            if not orig:
                break
            tmp = orig.popleft()
            stack.append(tmp)
            stack_sign.append('+')
if stack:
    print('NO')
else:
    print('\n'.join(stack_sign))