import sys
a, b, c, d, e = map(int, sys.stdin.readline().split(' '))

def func_val(a, b, c, d, e):
    val = (a**2 + b**2 + c**2 + d**2 + e**2) % 10
    return val

print(func_val(a, b, c, d, e))