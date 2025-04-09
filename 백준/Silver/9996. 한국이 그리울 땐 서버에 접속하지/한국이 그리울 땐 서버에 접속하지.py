import sys
input = sys.stdin.readline

n = int(input())

pattern = input().rstrip().split('*')
length = len(pattern[0]) + len(pattern[1])

for _ in range(n):
    test = input().rstrip()
    if len(test) >= length and test.startswith(pattern[0]) and test.endswith(pattern[1]):
        print('DA')
    else:
        print('NE')