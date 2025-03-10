import sys
a, b = map(int, sys.stdin.readline().split(' '))

def func_hyojin(a, b):
    val = a**2 - b**2
    return val

print(func_hyojin(a, b))