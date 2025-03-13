import sys

X = int(input())
N = int(input())


check = 0
for i in range(N):
    a, b = map(int, sys.stdin.readline().split(' '))
    check += a*b

if check == X:
    print('Yes')
else:
    print('No')