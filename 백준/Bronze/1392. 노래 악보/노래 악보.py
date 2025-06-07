import sys
input = sys.stdin.readline

N, Q = map(int, input().split())

secs = list(map(int, [input() for _ in range(N)]))
prefix = []
acc = 0
for s in secs:
    acc += s
    prefix.append(acc)

for _ in range(Q):
    t = int(input())
    for i in range(N):
        if t < prefix[i]:
            print(i + 1)
            break