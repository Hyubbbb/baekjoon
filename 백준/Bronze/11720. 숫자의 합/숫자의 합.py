import sys

n = int(sys.stdin.readline())

vals = sys.stdin.readline()

tmp = 0
for i in range(n):
    tmp += int(vals[i])

print(tmp)