import sys
input = sys.stdin.readline

n, m = map(int, input().split()) # n: 수의 개수, m: 합을 구해야 하는 횟수

nums = list(map(int, input().split())) # n개의 수

'''
# Sol 1: 구간 합 계산 -> TIME OUT
for _ in range(m):
    i, j = map(int, input().split())
    i -= 1
    j -= 1
    
    print(sum(nums[i:j+1]))
'''

# Sol 2: 누적합을 미리 계산해 놓기
sums = []
sums.append(0)

sum_tmp = 0
for num in nums:
    sum_tmp += num
    sums.append(sum_tmp)

# 누적합 출력
for _ in range(m):
    i, j = map(int, input().split())
    
    print(sums[j] - sums[i-1])