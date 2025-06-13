import sys
input = sys.stdin.readline

T = int(input()) # 테스트 케이스 개수

for _ in range(T):
    N = int(input()) # 학교 개수
    result = {}
    for i in range(N):
        S, L = input().split() # 학교명, 소비한 술의 양
        result[S] = int(L)
    print(max(result, key = result.get))