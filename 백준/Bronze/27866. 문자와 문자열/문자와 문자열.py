import sys

lines = sys.stdin.readlines()
lines = [line.strip() for line in lines]

i = int(lines[1])

print(lines[0][i-1])