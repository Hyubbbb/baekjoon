

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

dq = deque()
for _ in range(n):
    prompt = list(map(int, input().split()))
    
    # 1 X: 정수 X를 덱의 앞에 넣는다. (1 ≤ X ≤ 100,000)
    if prompt[0] == 1:
        dq.appendleft(prompt[1])
        
    # 2 X: 정수 X를 덱의 뒤에 넣는다. (1 ≤ X ≤ 100,000)
    elif prompt[0] == 2:
        dq.append(prompt[1])
        
    # 3: 덱에 정수가 있다면 맨 앞의 정수를 빼고 출력한다. 없다면 -1을 대신 출력한다.
    elif prompt[0] == 3:
        if dq:
            print(dq.popleft())
        else:
            print(-1)
            
    # 4: 덱에 정수가 있다면 맨 뒤의 정수를 빼고 출력한다. 없다면 -1을 대신 출력한다.
    elif prompt[0] == 4:
        if dq:
            print(dq.pop())
        else:
            print(-1)
            
    # 5: 덱에 들어있는 정수의 개수를 출력한다.
    elif prompt[0] == 5:
        print(len(dq))
        
    # 6: 덱이 비어있으면 1, 아니면 0을 출력한다.
    elif prompt[0] == 6:
        if dq: # 덱이 비어 있지 않은 경우
            print(0)
        else:
            print(1)
    # 7: 덱에 정수가 있다면 맨 앞의 정수를 출력한다. 없다면 -1을 대신 출력한다.
    elif prompt[0] == 7:
        if dq: # 덱이 비어 있지 않은 경우
            print(dq[0])
        else:
            print(-1)
    # 8: 덱에 정수가 있다면 맨 뒤의 정수를 출력한다. 없다면 -1을 대신 출력한다.
    elif prompt[0] == 8:
        if dq:
            print(dq[-1])
        else:
            print(-1)