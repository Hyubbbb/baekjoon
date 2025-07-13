from collections import Counter
import sys
input = sys.stdin.readline

N = int(input())

for i in range(N):
    a = input().rstrip()
    b = input().rstrip()
    
    counter1 = Counter(a)
    counter2 = Counter(b)
    
    common = counter1 & counter2
    total = counter1 | counter2
    
    print(f'Case #{i+1}: {sum(total.values())- sum(common.values())}')