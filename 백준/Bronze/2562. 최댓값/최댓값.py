import sys

l = list(map(int, sys.stdin.read().splitlines()))

print(max(l))
print(l.index(max(l))+1)