import sys
input = sys.stdin.readline

n = int(input())

dungchi = []
for _ in range(n):
    x, y = map(int, input().split())
    dungchi.append([x, y])

result = [] # 등수 저장
for i in range(n):
    rank = 0
    for j in range(n):
        # 자기 자신과의 비교는 제외
        if i == j:
            pass
        else:
            if (dungchi[i][0] < dungchi[j][0]) and (dungchi[i][1] < dungchi[j][1]):
                rank += 1
    result.append(rank+1)
print(*result)