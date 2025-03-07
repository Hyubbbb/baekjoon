x = int(input())

tmp = 1

if x == 0:
    print(tmp)
else:
    for i in range(x, 0, -1):
        tmp *= i
    print(tmp)