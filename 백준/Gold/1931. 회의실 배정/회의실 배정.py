import sys
input = sys.stdin.readline

N = int(input()) # 회의의 수

meetings = [tuple(map(int, input().split())) for _ in range(N)]

# 끝나는 시간 -> 시작하는 시간을 기준으로 정렬
meetings.sort(key=lambda x: (x[1], x[0]))

end_tmp = 0
cnt = 0
for start, end in meetings:
    # print(start, end)
    if start >= end_tmp:
        cnt += 1
        end_tmp = end
print(cnt)