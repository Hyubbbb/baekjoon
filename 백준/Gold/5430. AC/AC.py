"""
1. R: 배열에 있는 수의 순서를 뒤집는 함수
2. D: 첫 번째 수를 버리는 함수
    - 배열이 비어있는데 D를 사용한 경우에는 에러가 발생
"""
import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

"""
각 테스트 케이스의 첫째 줄에는 수행할 함수 p가 주어진다. 
- p의 길이는 1보다 크거나 같고, 100,000보다 작거나 같다.

다음 줄에는 배열에 들어있는 수의 개수 n이 주어진다. 
- (0 ≤ n ≤ 100,000)

다음 줄에는 [x1,...,xn]과 같은 형태로 배열에 들어있는 정수가 주어진다. 
- (1 ≤ xi ≤ 100)

전체 테스트 케이스에 주어지는 p의 길이의 합과 n의 합은 70만을 넘지 않는다.
"""

for _ in range(T):
    is_error = False
    is_reversed = False
    
    p = list(input().rstrip()) # p: 함수
    n = int(input()) # 배열에 들어 있는 수
    
    arr_str = input().rstrip()
    if n == 0:
        arr = deque()
    else:
        arr = deque(map(int, arr_str[1:-1].split(',')))

    for func in p:
        if func == 'R':
            is_reversed = not is_reversed
        else:
            # 길이가 0인 경우 에러
            if len(arr) == 0:
                is_error = True
                break
            
            # 첫 번째 수를 제거 (is_reversed를 고려해서)
            else:
                if not is_reversed:
                    arr.popleft()
                else:
                    arr.pop()
    
    if is_error:
        print('error')
    elif not is_reversed:
        print(str(list(arr)).replace(' ', ''))
    else:
        print(str(list(arr)[::-1]).replace(' ', ''))