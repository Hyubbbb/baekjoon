import sys
input = sys.stdin.readline

N, M = map(int, input().split()) # N: 저장된 사이트의 수, M: 찾으려는 사이트 수

# 저장된 사이트
dict = {}
for _ in range(N):
    site, pw = input().split()
    dict[site] = pw


# 찾으려는 사이트
for _ in range(M):
    want = input().rstrip()
    print(dict[want])