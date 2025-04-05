import sys
input = sys.stdin.readline

n = int(input())

nums = []
for _ in range(n):
    nums.append(list(map(int, input().split())))

for num in sorted(nums):
    print(*num)