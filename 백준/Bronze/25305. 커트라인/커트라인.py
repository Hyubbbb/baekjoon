import sys

n, k = map(int, sys.stdin.readline().split())
scores = sorted(list(map(int, sys.stdin.readline().split())))

print(scores[-k])