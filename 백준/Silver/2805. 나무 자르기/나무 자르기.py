N, M = map(int, input().split())
trees = list(map(int, input().split()))

low = 0 # 이 때 가장 많이 썰린다
high = max(trees)
result = 0 # 조건을 만족하는 mid 값 저장용

while low <= high:
    mid = (low + high) // 2
    total = 0
    
    for tree in trees:
        total += (tree - mid if tree > mid else 0)
    
    if total >= M:
        result = mid # 중간 저장
        low = mid + 1
    else:
        high = mid - 1

print(result)