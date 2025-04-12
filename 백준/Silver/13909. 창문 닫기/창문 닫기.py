n = int(input())

max_n = int(n**0.5)
cnt = 0
for i in range(1, max_n+1):
    if i**2 == int(i**2):
        cnt+=1

print(cnt)