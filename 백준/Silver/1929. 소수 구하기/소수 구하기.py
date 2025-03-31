import math 

m, n = map(int, input().split())

def is_prime(x):
    if x == 1:
        return 0
    
    for i in range(2, int(math.sqrt(x)) + 1):
        if x%i == 0:
            return 0
    
    return 1

for k in range(m, n+1):
    if is_prime(k) == 1:
        print(k)
