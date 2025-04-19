import sys, statistics
input = sys.stdin.readline

n = int(input())
word = list(map(int, sys.stdin.read().splitlines()))

'''
첫째 줄에는 산술평균을 출력한다. 소수점 이하 첫째 자리에서 반올림한 값을 출력한다.

둘째 줄에는 중앙값을 출력한다.

셋째 줄에는 최빈값을 출력한다. 여러 개 있을 때에는 최빈값 중 두 번째로 작은 값을 출력한다.

넷째 줄에는 범위를 출력한다.
'''

sort_word = sorted(word)

# 산술평균
mean = sum(word)/len(word)
print(int(round(mean, 0)))

# 중앙값
median = len(sort_word)//2
print(statistics.median(word))

# 최빈값
cnt = {}
for i in word:
    if i in cnt:
        cnt[i] +=1
    else:
        cnt[i] = 1

mode_list = [k for k, v in cnt.items() if v == max(cnt.values())]
if len(mode_list) == 1:
    print(*mode_list)
else:
    print(sorted(mode_list)[1])

# 범위
print(sort_word[-1] - sort_word[0])