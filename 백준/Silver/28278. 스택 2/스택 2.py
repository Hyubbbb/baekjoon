import sys
input = sys.stdin.readline

# 명령 개수 n
n = int(input())

stack = []

# 명령 입력
for _ in range(n):
    prompt = list(map(int, input().split()))
    
    if prompt[0] == 1:
        stack.append(prompt[1])
    if prompt[0] == 2:
        if len(stack) > 0:
            print(stack.pop())
        else:
            print(-1)
    if prompt[0] == 3:
        print(len(stack))
    if prompt[0] == 4:
        if len(stack)==0:
            print(1)
        else:
            print(0)
    if prompt[0] == 5:
        if len(stack)==0:
            print(-1)
        else:
            print(stack[-1])