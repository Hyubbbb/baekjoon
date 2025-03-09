import sys

N, M = map(int, sys.stdin.readline().split(' '))

data = sys.stdin.read().splitlines()

for i in range(N):
    tmp = [x + y for x,y in zip(list(map(int, data[i].split(' '))), list(map(int, data[N+i].split(' '))))]
    for j in range(M):
        print(tmp[j], end=' ')
    print()