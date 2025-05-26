import sys, math
input = sys.stdin.readline

while True:
    fact_num = input().rstrip()
    if fact_num == '0':
        break
    else:
        result = 0
        n = len(fact_num) # 숫자의 길이
        for i in range(len(fact_num)):
            result += int(fact_num[i]) * math.factorial(n-i)
        print(result)