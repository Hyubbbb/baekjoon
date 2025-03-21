import sys

n = int(input())

stack = []

for i in range(n):
    # prompt = input().split(' ')
    prompt = sys.stdin.readline().strip().split()
    # print(f'prompt: {prompt}')
    
    if prompt[0] == 'push':
        stack.append(int(prompt[1]))
        
    elif prompt[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else: 
            print(stack.pop())
            
    elif prompt[0] == 'size':
        print(len(stack))
        
    elif prompt[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
            
    elif prompt[0] == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
    
    
    # print(f'stack: {stack}')