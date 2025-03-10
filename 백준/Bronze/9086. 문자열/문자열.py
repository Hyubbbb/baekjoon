import sys

# 첫 줄: 테스트 케이스 개수
num = int(sys.stdin.readline().strip())

# 이후 줄: 테스트 케이스
for i in range(num):
    word = sys.stdin.readline().strip()
    print(word[0] + word[-1])