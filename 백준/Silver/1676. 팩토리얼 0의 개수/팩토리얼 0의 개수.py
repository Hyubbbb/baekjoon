import math

n = int(input())
words = str(math.factorial(n))

result = 0
for word in words[::-1]:
    if word == '0':
        result+=1
    else:
        break
print(result)