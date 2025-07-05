import sys
input = sys.stdin.readline

N = int(input())
S = list(map(int, input().split()))

from collections import defaultdict # 처음 보는 키에 대한 Default 값을 지정해주는 딕셔너리

cnt = defaultdict(int) # 각 과일별 개수 기록용 딕셔너리
kind = 0 # 윈도우 내 과일 종류 개수
l = 0 # 왼쪽 슬라이딩 윈도우 포인터
max_len = 0 # 정답용

for r in range(N): # 오른쪽 포인터를 점점 우측으로 이동
    if cnt[S[r]] == 0: # 처음보는 과일 종류이면
        kind += 1
    cnt[S[r]] += 1 
    
    # 과일 종류 개수 점검
    while kind > 2: # 과일 종류가 2개를 넘으면
        cnt[S[l]] -= 1 # 왼쪽 슬라이드 이동
        if cnt[S[l]] == 0:
            kind -= 1
        l += 1
    
    max_len = max(max_len, r-l+1)
print(max_len)
    


"""
Sol 1: Brute Force (시간 초과)
len_full = len(S)
len_set = len(set(S))

flag = False # 반복문 탈출용
for i in range(0, len_full): # 제거할 과일 개수
    # print(f'i = {i}')
    for a in range(i+1):
        b = i-a
        # print(f'a, b = {a}, {b}')
        tmp = S[a:len_full-b]
        len_set = len(set(tmp))
        if len_set <= 2:
            flag = True
    if flag:
        break

print(len(tmp))
"""