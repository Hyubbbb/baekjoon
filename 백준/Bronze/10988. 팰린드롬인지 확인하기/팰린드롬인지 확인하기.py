words = input()
n = len(words)

tmp = True
for i in range(n):
    if words[i] != words[n-1-i]:
        tmp = False
        break

print(1 if tmp else 0)