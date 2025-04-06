import sys

input = sys.stdin.readline

n = int(input())
nums = set(map(int, input().split())) # 중복 없음

m = int(input())
valid_nums = list(map(int, input().split()))

for valid_num in valid_nums:
    if valid_num in nums:
        print(1, end=' ')
    else:
        print(0, end=' ')
        
# in을 할 때, 순서를 고려할 필요 없을 땐 list 말고 set !