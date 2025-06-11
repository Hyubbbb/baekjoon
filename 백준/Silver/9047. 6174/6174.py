import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    nums_4 = input().rstrip()
    
    cnt = 0
    
    while nums_4 != '6174':
        cnt += 1
        nums_4_des = int(''.join(sorted(nums_4, reverse = True))) # 가장 큰 수 
        nums_4_asc = int(''.join(sorted(nums_4, reverse = False))) # 가장 작은 수
        
        # nums_4 = str(nums_4_des - nums_4_asc) # 패착
        nums_4 = str(nums_4_des - nums_4_asc).zfill(4)
    print(cnt)