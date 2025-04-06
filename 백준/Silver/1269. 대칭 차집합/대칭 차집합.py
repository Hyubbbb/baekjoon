import sys
input = sys.stdin.readline

a, b = map(int, input().split())

set_a = set(map(int, input().split()))
set_b = set(map(int, input().split()))

common = (set_a-set_b)|(set_b-set_a)
print(len(common))