import math

n, m = map(int, input().split()) # n: 전체 시간

k = n // m

result = 0
for b in range(k+1): # b: B 등장 횟수
    sec = n - b*m

    if sec+b == 0:
        result += 1
    else:
        result += math.factorial(sec+b) // (math.factorial(sec) * math.factorial(b))
    

# 가능한 조합의 수를 1,000,000,007로 나눈 나머지 값을 출력
print(result % 1000000007)