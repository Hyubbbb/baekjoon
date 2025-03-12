n = int(input())

total = 1

if n == 0:
    total = 1
else:    
    for i in range(n, 0, -1):
        total *= i
print(total)