n, x = map(int, input().split())

day_costs = list(map(int, input().split()))
# costs = [0]*n

min_cost = max(day_costs)*2*x
for i in range(n-1):
    tmp = (day_costs[i] + day_costs[i+1])*x
    if min_cost > tmp:
        min_cost = tmp

print(min_cost)