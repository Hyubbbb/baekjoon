import sys
input = sys.stdin.readline

n = int(input())

def is_prime(x):
    if x <= 1:
        return False
    if x <= 3:
        return True
    if x%2 == 0 or x%3 == 0:
        return False
    
    i = 5
    while i**2 <= x:
        if x%i==0 or x%(i+2)==0:
            return False
        i+=6
    return True

for _ in range(n):
    num = int(input())
    while True:
        if is_prime(num):
            print(num)
            break
        num+=1