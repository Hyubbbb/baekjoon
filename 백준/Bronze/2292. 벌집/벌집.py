n = int(input())

cnt = 0
power = 1

if n==1:
    print(1)
else:
    n -= 1
    while n > 0:
        n -= 6*power
        power += 1
    print(power)