a, d, k = map(int, input().split())

n, m = divmod(k-a, d)

if (m != 0) or (n+1 < 1):
    print('X')
else:
    print(1 + n)