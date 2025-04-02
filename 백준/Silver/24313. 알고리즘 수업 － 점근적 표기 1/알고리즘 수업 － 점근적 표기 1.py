a_1, a_0 = map(int, input().split())
c   = int(input())
n_0 = int(input())

valid = True
for n in range(n_0, 101):
    if a_1*n + a_0 > c * n:
        valid = False
        break

print(1 if valid else 0)