A, B = map(int, input().split()) # A: 패티, B: 치즈

# A > B: B + (B+1)
# A = B: B-1 + A
# A < B: A-1 + A

if A > B:
    print(2*B + 1)
elif A < B:
    print(2*A - 1)
else:
    print(A+B-1)