n = int(input())

num_point = 2

for _ in range(n):
    num_point += num_point-1

print(num_point**2)