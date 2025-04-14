import sys
input = sys.stdin.readline

t = int(input())

def is_vps(x):
    stack=[]
    for i in range(len(x)):
        if x[i] == ')': # 닫는 괄호일 때
            if i==0:
                return 'NO'
            elif len(stack) == 0:
                return 'NO'
            else:
                stack.pop()
        else: # 여는 괄호일 때
            stack.append(x[i])
    if len(stack)==0:
        return 'YES'
    else:
        return 'NO'

for _ in range(t):
    print(is_vps(input().rstrip()))