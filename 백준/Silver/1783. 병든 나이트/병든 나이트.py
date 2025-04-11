import sys
input = sys.stdin.readline
n, m = map(int, input().split())

if n==1:
    print(1)
elif n==2:
    print(min((m+1)//2, 4))
else: # n>=3인 경우
    if 4<=m<=6:
        print(4)
    elif 1<=m<=3:
        print(m)
    elif m>=7:
        print(m-2)