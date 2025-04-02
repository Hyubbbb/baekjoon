import sys

# 완전수 판단
while True:
    n =  int(sys.stdin.readline().strip())
    if n == -1:
        break
    
    nums = []
    for i in range(1, n):
        if n%i==0:
            nums.append(i)
    
    # 완전수 출력
    if n == sum(nums):
        print(f'{n} = ', end='')
        print(*nums, sep = ' + ')
    else:
        print(f'{n} is NOT perfect.')