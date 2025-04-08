bar = input()

stack = []
answer = 0

for i in range(len(bar)):
    if bar[i] == '(': # 여는 괄호
        stack.append(bar[i])
    else: # 닫는 괄호
        stack.pop()
        if bar[i-1]=='(': # 레이저인 경우
            answer += len(stack)
        else: # 막대 끝인 경우
            answer += 1
print(answer)