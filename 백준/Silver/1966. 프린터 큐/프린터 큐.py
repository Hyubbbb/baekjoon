import sys
from collections import deque
input = sys.stdin.readline

t = int(input())

for _ in range(t): # t: 테스트 개수
    n, m = map(int, input().split())
    imp_dq = deque(list(map(int, input().split())))
    
    # 인덱스 배열 생성
    idx_dq = deque(range(0, n))
    
    cnt = 1 # 몇 번째로 출력되는지 확인하기 위한 변수
    while True:        
        tmp_imp = imp_dq.popleft()
        tmp_idx = idx_dq.popleft()

        if imp_dq and max(imp_dq) > tmp_imp:
            imp_dq.append(tmp_imp)
            idx_dq.append(tmp_idx)
        else:
            if tmp_idx == m:
                print(cnt)
                break
            else:
                cnt += 1