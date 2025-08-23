import sys
input = sys.stdin.readline

A, B = map(int, input().split())
K, X = map(int, input().split())

if (A < K-X < B) and (A < K+X < B):
    print((K+X) - (K-X-1))
elif (K-X < A) and (A < K+X < B):
    print((K+X) - (A-1))
elif (A < K-X < B) and (B < K+X):
    print(B - (K-X-1))
elif (K-X < A) and (B < K+X):
    print(B - (A-1))
else:
    print('IMPOSSIBLE')