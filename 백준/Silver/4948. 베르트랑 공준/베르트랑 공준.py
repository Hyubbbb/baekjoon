import sys
input = sys.stdin.readline

def is_prime(x):
    if x <= 1:
        return False
    if x <= 3:
        return True
    if x%2==0 or x%3==0:
        return False
    
    i = 5
    while i**2 <= x:
        if x%i==0 or x%(i+2)==0:
            return False
        i+=6
    return True

while True:
    n = int(input())
    # 종료 조건
    if n==0: 
        break
    
    # 소수 판별
    print(sum([is_prime(i) for i in range(n+1, 2*n+1)]))
        