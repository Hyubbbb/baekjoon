import sys
input = sys.stdin.readline

def is_balance(setence):
    stack = []
    for i in range(len(setence)):
        if setence[i] not in ['(', ')', '[', ']']:
            pass
        else:
            if setence[i]=='(' or setence[i]=='[':
                stack.append(setence[i])
            elif setence[i]==')':
                if i==0 or len(stack)==0 or stack[-1] != '(':
                    return 'no'
                else:
                    stack.pop()
            elif setence[i]==']':
                if i==0 or len(stack)==0 or stack[-1] != '[':
                    return 'no'
                else:
                    stack.pop()
    if len(stack)==0:
        return 'yes'
    else:
        return 'no'

while True:
    sentence = input().rstrip()
    if sentence == '.':
        break
    
    print(is_balance(sentence))