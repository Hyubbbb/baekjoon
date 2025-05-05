import sys, math
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    num = int(input())
    cnt = 0
    
    three = num // 3 # 최대로 가질 수 있는 3의 개수
    for cur_three in range(three+1): # 최대 3의 개수까지
        remainder = (num - 3*cur_three) if cur_three > 0 else num
        
        two = remainder // 2 # 최대로 가질 수 있는 2의 개수
        for cur_two in range(two+1): # 최대 2의 개수까지
            cur_one = (remainder - 2*cur_two) if cur_two > 0 else remainder
            
            cnt += math.factorial(cur_three + cur_two + cur_one) // (math.factorial(cur_three)*math.factorial(cur_two)*math.factorial(cur_one))
    print(cnt)