import sys
input = sys.stdin.readline

m, n = map(int, input().split()) # m: 조카 수, n: 과자 수

cookies = list(map(int, input().split()))

low, high = 1, max(cookies)

max_cnt = 0
while low <= high:
    mid = (low + high)//2
    cnt_cookie = sum([cookie//mid for cookie in cookies])
    
    if cnt_cookie >= m:
        max_cnt = mid
        low = mid+1
    elif cnt_cookie < m:
        high = mid-1

print(max_cnt)