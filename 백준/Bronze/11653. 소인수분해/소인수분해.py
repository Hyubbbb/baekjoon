n = int(input())

i = 2
while i**2 <= n:
# for i in range(2, n+1):
    while n%i == 0:
        print(i)
        n = n//i
    i += 1

if n > 1:
    print(n)