import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

T = int(input()) # 테스트 케이스 개수

if T == 0:
    pass

else:
    # 1. DP
    N = 41 # N은 0보다 크거나 40보다 작거나 같다

    dp = [[0, 0]] * N # 내부 배열: [0 횟수, 1 횟수]

    # fib(0)
    dp[0] = [1, 0]
    # fib(1)
    dp[1] = [0, 1]

    for i in range(2, N):
        dp[i] = [dp[i-1][0] + dp[i-2][0], dp[i-1][1] + dp[i-2][1]]


    # 2. Print
    for _ in range(T):
        n = int(input())
        print(*dp[n])