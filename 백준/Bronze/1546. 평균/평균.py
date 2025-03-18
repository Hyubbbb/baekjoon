import sys

n = int(sys.stdin.readline())

scores = list(map(int, sys.stdin.readline().split(' ')))

max_score = max(scores)

tmp = 0
for score in scores:
    tmp += score/max_score * 100

print(tmp/n)