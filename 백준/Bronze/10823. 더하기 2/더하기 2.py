import sys
nums = list(map(int, sys.stdin.read().replace('\n', '').split(',')))
print(sum(nums))