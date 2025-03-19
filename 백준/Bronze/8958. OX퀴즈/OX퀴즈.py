import sys

n = int(input())

for i in range(n):
    data = sys.stdin.readline().strip().split('X')
    
    score = 0
    for j in data:
        tmp = len(j)
        score += tmp * (tmp+1) / 2

    print(int(score))