import sys
input = sys.stdin.readline

n = int(input())

chars = []
for _ in range(n):
    char = input().rstrip()
    if [len(char), char] not in chars:
        chars.append([len(char), char])

for char in sorted(chars):
    print(char[1])