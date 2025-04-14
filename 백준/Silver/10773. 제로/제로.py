import sys
input = sys.stdin.readline

k = int(input())

stack = []
for _ in range(k):
    val = int(input())
    if val == 0:
        stack.pop()
    else:
        stack.append(val)

print(sum(stack))