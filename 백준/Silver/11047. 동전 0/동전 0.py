import sys
input = sys.stdin.readline

n, k = map(int, input().split())

# k보다 작은 가치만 스택에 저장
stack = []
for _ in range(n):
    a = int(input())
    if a <= k:
        stack.append(a)
    else:
        pass

# 가치가 큰 동전부터 차례대로 꺼내보자
cnt = 0
for i in stack[::-1]:
    cnt_tmp, k = divmod(k, i)
    cnt += cnt_tmp
    
    if k == 0 :
        break

print(cnt)