import math

n = int(input())

# 1이면 컷
num_list = list(map(int, input().split(' ')))


# 소수 판단 함수
def classify_prime(x):
    is_prime = True
    
    if x == 1:
        is_prime = False
    else:    
        for i in range(2, int(math.sqrt(x)) + 1):
            if x%i == 0:
                is_prime = False
                break
    return is_prime
            
# 반복문 실행 (소수 판단)
cnt = 0
for num in num_list:
    if classify_prime(num) == True:
        cnt += 1

print(cnt)