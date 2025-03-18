import sys

a, b, c = map(int, sys.stdin.read().splitlines())

val = a * b * c
val = str(val)


for i in range(10):
    print(val.count(f'{i}'))