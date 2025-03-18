import sys

t = int(sys.stdin.readline()) # 테스트 입력 개수

for _ in range(t):
    height, width, n = map(int, sys.stdin.readline().split(' ')) # 호텔의 층 수, 각 층의 방 수, 몇 번째 손님인지
    print(n%height if n%height else height, format(n//height if n%height==0 else n//height+1, '02'), sep='')