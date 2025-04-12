import sys
input = sys.stdin.readline

t = int(input())

# Sol1: 시간 초과
# def is_prime(x):
#     if x <= 1:
#         return False
#     if x <= 3:
#         return True
#     if x%2==0 or x%3==0:
#         return False
    
#     i = 5
#     while i**2 <= x:
#         if x%i==0 or x%(i+2)==0:
#             return False
#         i+=6
#     return True

# for _ in range(t):
#     n = int(input())
#     cnt = 0
#     for i in range(2, n//2 + 1):
#         if is_prime(i) and is_prime(n-i):
#            cnt+=1
#     print(cnt)

nums = [int(input()) for _ in range(t)]
max_num = max(nums)

sieve = [True]*(max_num+1)
sieve[0] = sieve[1] = False # 0, 1은 소수가 아님

# sieve of Eratosthenes
for i in range(2, int(max_num**0.5)+1):
    if sieve[i]:
        for j in range(i**2, max_num+1, i):
            sieve[j] = False

# 테스트 케이스 출력
for num in nums:
    cnt = 0
    for i in range(2, num//2 + 1):
        if sieve[i] and sieve[num-i]:
            cnt+=1
    print(cnt)