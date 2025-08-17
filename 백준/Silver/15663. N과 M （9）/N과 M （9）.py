import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = sorted(map(int, input().split()))

visited = [False] * N
answer = []

def dfs(depth):
    if depth == M:
        print(*answer)
        return

    last = None # 해당 깊이에서 마지막으로 쓴 값 기록 (중복 방지)
    for i in range(N):
        if visited[i]:
            continue
        if last == nums[i]:
            continue
        
        visited[i] = True
        answer.append(nums[i])
        last = nums[i]
        
        dfs(depth + 1)
        
        visited[i] = False
        answer.pop()
        
dfs(0)