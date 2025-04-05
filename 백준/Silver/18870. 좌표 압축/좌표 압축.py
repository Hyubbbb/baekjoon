import sys
input = sys.stdin.readline

n = int(input())

nums = list(map(int, input().split()))

# 중복일 수 있어서, set() 적용
nums_prime = sorted(set(nums))

nums_cnt = {}
for i, num_prime in enumerate(nums_prime):
    nums_cnt[num_prime] = i

# 최종 출력
for num in nums:
    print(nums_cnt[num], end=' ')