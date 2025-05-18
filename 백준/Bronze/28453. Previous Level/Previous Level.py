import sys
input = sys.stdin.readline

n = int(input())
m_list = list(map(int, input().split()))

for m in m_list:
    # 구간 1
    if m == 300:
        print(1, end=' ')
    # 구간 2
    elif m >= 275:
        print(2, end=' ')
    # 구간 3
    elif m >= 250:
        print(3, end=' ')
    else:
        print(4, end=' ')