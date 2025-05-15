import sys

nums = sys.stdin.readline().rstrip().split(',')

print(sum([num.isdigit() for num in nums]))