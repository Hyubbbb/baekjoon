import sys

a, b = sys.stdin.readline().split(' ')


a_new, b_new = map(int, [a[::-1], b[::-1]])


if a_new > b_new:
    print(a_new)
elif a_new < b_new:
    print(b_new)