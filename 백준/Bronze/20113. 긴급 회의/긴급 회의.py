N = int(input())

votes = map(int, input().split()) # 0이면 skip

members = [0] * (N+1)
for vote in votes:
    members[vote] += 1

members[0] = 0 # skip한 표는 의미 없으니 0으로 만들어줌

m = max(members)
max_mem = [index for index, vote in enumerate(members) if vote == m]

if len(max_mem) > 1:
    print('skipped')
elif len(max_mem) == 1:
    print(*max_mem)