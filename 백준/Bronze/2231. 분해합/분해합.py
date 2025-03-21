n = int(input())

gen = 0
for num in range(n):
    tmp = num
    for i in list(str(num)):
        tmp += int(i)
    if tmp == n:
        gen = num
        break

print(gen)