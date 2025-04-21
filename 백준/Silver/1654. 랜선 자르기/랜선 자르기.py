import sys
sys.setrecursionlimit(10**6)

k, n = map(int, sys.stdin.readline().split())

lines = list(map(int, sys.stdin.read().splitlines()))

min_size = 1
max_size = max(lines)

result = 0
while min_size <= max_size:
    cnt = 0
    mid_size = (min_size + max_size) // 2
    
    for line in lines:
        # 자른 후 전선의 개수
        if line >= mid_size:
            cnt += line//mid_size
    
    # 전선이 부족한 경우, 더 짧게 많이 자르기
    if cnt < n:
        max_size = mid_size-1
    # 전선이 충분한 경우, 더 길게 적게 자르기
    else:
        result = mid_size
        min_size = mid_size+1

print(result)