word, b = input().split()
b = int(b)

result = 0
for i in range(len(word)):
    alpha = word[::-1][i]
    if ord(alpha) <= 57:
        val = ord(alpha)-48
    else:
        val = ord(alpha)-55
        
    result += b**i * val

print(result)