import sys

n = int(input())

nums = []
for _ in range(n):
    nums.append(int(sys.stdin.readline()))
nums = sorted(nums)

for i in range(n):
    print(nums[i])