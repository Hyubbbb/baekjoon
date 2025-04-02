import math

m = int(input())
n = int(input())

def is_prime(num):
    if num <= 1:
        return False
    
    for i in range(2, math.isqrt(num)+1):
        if num % i == 0:
            return False
        
    return True

prime_set = set()
for k in range(m, n+1):
    if is_prime(k):
        prime_set.add(k)

if len(prime_set) == 0:
    print(-1)
else:
    print(sum(prime_set))
    print(min(prime_set))