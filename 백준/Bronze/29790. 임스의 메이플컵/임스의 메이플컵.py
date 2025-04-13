import sys
n, u, l = map(int, sys.stdin.readline().split())

cond_1 = n>=1000  
cond_2 = (u>=8000 or l>=260)

if cond_1 and cond_2:
    print('Very Good')
elif cond_1:
    print('Good')
else:
    print('Bad')