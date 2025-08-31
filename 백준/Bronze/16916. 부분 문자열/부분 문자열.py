import sys
input = sys.stdin.readline

S = input().rstrip()
P = input().rstrip()

print(1 if P in S else 0)