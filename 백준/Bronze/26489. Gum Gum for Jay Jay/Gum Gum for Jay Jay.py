import sys

data = sys.stdin.read().split('\n')

cnt = 0
for i in data:
    if (i == 'gum gum for jay jay'):
        cnt += 1


print(cnt)