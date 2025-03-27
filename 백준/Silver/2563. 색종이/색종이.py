import sys

n = int(input())


array = [[0] * 100 for _ in range(100)]

for _ in range(n):
    x1, y1 = map(int, sys.stdin.readline().strip().split())
    # print(x1, y1)
    
    for x in range(x1, x1+10):
        for y in range(y1, y1+10):
            array[x][y] = 1

result = 0
for k in array:
    result += sum(k)
print(result)