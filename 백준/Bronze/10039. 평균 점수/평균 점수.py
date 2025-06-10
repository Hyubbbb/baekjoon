sums = 0
for _ in range(5):
    num = int(input())
    sums +=  num if num >= 40 else 40
print(sums//5)