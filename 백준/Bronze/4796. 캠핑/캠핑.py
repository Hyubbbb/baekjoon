import sys
input = sys.stdin.readline

i = 0
while True:
    L, P, V = map(int, input().split())
    if L == P == V == 0:
        break
    
    else:
        i += 1
        times, remainder = divmod(V, P)
        remainder = L if remainder > L else remainder
        print(f'Case {i}: {times*L + remainder}')