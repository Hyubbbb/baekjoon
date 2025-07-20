import sys
input = sys.stdin.readline
N, r, c = map(int, input().split())

result = 0

# N이 2 이상일 때
while N >= 0:
    N -= 1
    # 1사분면
    if r < 2**N and c < 2**N:
        result += (2**N * 2**N) * 0
        
        # Shifting
        r -= (2**N) * 0
        c -= (2**N) * 0

    # 2사분면
    if r < 2**N and c >= 2**N:
        result += (2**N * 2**N) * 1
        
        # Shifting
        r -= (2**N) * 0
        c -= (2**N) * 1

    # 3사분면
    if r >= 2**N and c < 2**N:
        result += (2**N * 2**N) * 2
        
        # Shifting
        r -= (2**N) * 1
        c -= (2**N) * 0

    # 4사분면
    if r >= 2**N and c >= 2**N:
        result += (2**N * 2**N) * 3
        
        # Shifting
        r -= (2**N) * 1
        c -= (2**N) * 1

print(int(result))