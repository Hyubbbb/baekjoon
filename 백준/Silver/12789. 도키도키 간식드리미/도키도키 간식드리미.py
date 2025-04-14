import sys
input = sys.stdin.readline

n = int(input())

nums = list(map(int, input().split()))

stack = []
order = 1
for num in nums:
    stack.append(num)
    
    while stack and stack[-1]==order:
        stack.pop()
        order+=1

if stack:
    print('Sad')
else:
    print('Nice')
    

# 자료구조를 더 이해해보자