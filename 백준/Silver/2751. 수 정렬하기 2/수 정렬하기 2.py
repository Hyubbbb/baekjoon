import sys

n = int(sys.stdin.readline())

nums = sorted([int(sys.stdin.readline()) for _ in range(n)])

sys.stdout.write('\n'.join(map(str, nums)))