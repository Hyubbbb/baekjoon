import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split())) # 자료 구조를 나타내는 수열
b = list(map(int, input().split())) # 담고 있는 원소를 나타내는 수열

m = int(input())
c = list(map(int, input().split())) # 삽입할 원소를 나타내는 수열


dq = deque([])
for idx, q in enumerate(a):
    if not q:
        dq.appendleft(b[idx])

# print(dq)

result = []
if dq:
    for c_val in c:
        dq.append(c_val)
        result.append(dq.popleft())
    print(*result)
else: # 모든 자료구조가 스택인 경우
    print(*c)



# 10^9 * 10^5 = 10^14
# 최악의 경우 1초로는 절대 불가

# 결국, 맨 마지막 큐 값이 중요
# 큐가 없다면, 수열 C input이 중요