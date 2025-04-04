n, k = map(int, input().split())

temp = list(map(int, input().split()))


# # sol 1 (Time Out)
# for i in range(n-k):
#     sum_temp = sum(temp[i:i+k])
#     if i == 0:
#         max_temp = sum_temp
#     else:
#         max_temp = max(max_temp, sum_temp)

# print(max_temp)

# sol 2 (Sliding Window)
max_temp = float('-inf')
sum_temp = 0
for i in range(n):
    sum_temp += temp[i]
    
    if i >= k-1:
        max_temp = max(max_temp, sum_temp)
        sum_temp -= temp[i-(k-1)]

print(max_temp)