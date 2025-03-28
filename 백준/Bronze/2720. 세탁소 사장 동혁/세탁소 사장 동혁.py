import sys

t = int(input())

# c = int(input())

cents = [25, 10, 5, 1]

for _ in range(t):
    result = []
    c = int(sys.stdin.readline().strip())
    
    for cent in cents:
        a, b = divmod(c, cent)
        
        result.append(a) # 거스름 개수
        c = b
    print(*result)