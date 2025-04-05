import sys

a = sorted([int(sys.stdin.readline()) for _ in range(5)])

print(int(sum(a)/len(a)))
print(a[2])