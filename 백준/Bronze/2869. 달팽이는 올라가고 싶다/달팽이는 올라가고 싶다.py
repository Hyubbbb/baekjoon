a, b, v = map(int, input().split())

v -= a # 막판 스퍼트
day = 1

add_day, remainder = divmod(v, (a-b))

if remainder == 0:
    day += add_day

else:
    day += add_day + 1

print(day)