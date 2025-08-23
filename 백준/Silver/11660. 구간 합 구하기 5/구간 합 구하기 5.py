import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = [ [0]*(N+1) ]
for _ in range(N):
    A.append([0] + list(map(int, input().split())))

# 2D prefix sum
P = [ [0]*(N+1) for _ in range(N+1) ]
for i in range(1, N+1):
    row_sum = 0
    Ai = A[i]
    Pi = P[i]
    Pim1 = P[i-1]
    for j in range(1, N+1):
        row_sum += Ai[j]
        Pi[j] = row_sum + Pim1[j]

out_lines = []
for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    res = P[x2][y2] - P[x1-1][y2] - P[x2][y1-1] + P[x1-1][y1-1]
    out_lines.append(str(res))

print("\n".join(out_lines))
