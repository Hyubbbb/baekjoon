import sys
input = sys.stdin.readline

n = int(input())
times = map(int, input().split())
times = sorted(times, reverse=False)

result = 0
for i in range(len(times)):
    result += sum(times[0:i+1])

print(result)