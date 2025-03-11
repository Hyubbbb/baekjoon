import sys


lines = sys.stdin.read().splitlines()

for line in lines:
    N, S = map(int, line.split(' '))
    
    print(S // (N+1))