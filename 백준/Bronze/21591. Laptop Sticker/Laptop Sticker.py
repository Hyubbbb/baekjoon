import sys

w_c, h_c, w_s, h_s = map(int, sys.stdin.readline().split(' '))

cond1 = (w_c - w_s)/2 >= 1
cond2 = (h_c - h_s)/2 >= 1

if cond1 & cond2:
    print(1)
else:
    print(0)