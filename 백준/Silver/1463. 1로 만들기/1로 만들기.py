n = int(input()) # n <= 10**6

dp = [0] * (10**6+1)

dp[0] = float('inf')
dp[1] = 0

for i in range(2, len(dp)):
    # 1. 3으로 나누어 떨어지면, 
    mod, remainder = divmod(i, 3)
    if remainder == 0:
        a = dp[mod] + 1
    else:
        a = dp[0] # 안 되는 경우, 무한대로 할당
    
    # 2. 2로 나누어 떨어지면, 
    mod, remainder = divmod(i, 2)
    if remainder == 0:
        b = dp[mod] + 1
    else:
        b = dp[0] # 안 되는 경우, 무한대로 할당
    
    # 3. 1을 뺀다
    c = dp[i-1] + 1
    
    # 최솟값을 저장
    dp[i] = min(a, b, c)

print(dp[n])
# print(dp)