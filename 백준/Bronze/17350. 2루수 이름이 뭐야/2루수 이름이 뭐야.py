import sys

n = int(input())

names = sys.stdin.read().splitlines()

print('뭐야;' if 'anj' in names else '뭐야?')