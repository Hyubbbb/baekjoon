import sys
input = sys.stdin.readline

# Input
N = int(input())
M = int(input())
S = input().rstrip()

# Define index
i = 0
cnt = 0
ans = 0

# Count IOI
while i < (M-2):
    if S[i:i+3] == 'IOI':
        i += 2
        cnt += 1
        
        if cnt == N:
            ans += 1
            cnt -= 1
    else:
        i += 1
        cnt = 0

print(ans)