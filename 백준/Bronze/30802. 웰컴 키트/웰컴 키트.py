import sys, math
input = sys.stdin.readline

n = int(input()) # 사람 수
shirts = list(map(int, input().split())) # 사이즈별 티셔츠 수
t, p = map(int, input().split()) # t: 한 번에 주문할 티셔츠 수 / p: 한 번에 주문할 펜 수

# 티셔츠 주문 수
print(sum([math.ceil(shirt/t) for shirt in shirts]))

# 펜 주문 수
print(*divmod(n, p))