import sys
input = sys.stdin.readline

n = int(input())

nums = []
for _ in range(n):
    nums.append(list(map(int, input().split()))[::-1])

for num in sorted(nums):
    print(num[1], num[0])