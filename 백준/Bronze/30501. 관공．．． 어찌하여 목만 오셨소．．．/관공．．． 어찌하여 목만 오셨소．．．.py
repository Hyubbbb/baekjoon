import sys
input = sys.stdin.readline

N = int(input())

for _ in range(N):
    name = input()
    if 'S' in name:
        print(name)