import sys

a = list(map(int, sys.stdin.read().splitlines()))

tmp = []
for i in a:
    tmp.append(i % 42)
    
print(len(set(tmp)))