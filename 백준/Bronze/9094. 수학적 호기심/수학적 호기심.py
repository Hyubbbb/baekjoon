import sys

t = int(input())

for i in range(t):
    n, m = map(int, sys.stdin.readline().split(' '))
    
    cnt = 0
    for b in range(2, n):
        # print('b')
        # print(b)
        for a in range(1, b):
            # print('a')  
            # print(a)
            
            if (a**2 + b**2 + m) % (a*b) == 0:
                cnt += 1
    print(cnt)