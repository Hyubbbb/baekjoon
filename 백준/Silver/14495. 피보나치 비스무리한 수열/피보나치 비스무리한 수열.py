n = int(input())

nums = [1]*116

if n <= 3:
    print(1)
else:
    # 4번째부터 계산
    for i in range(3, n):
        nums[i] = nums[i-1] + nums[i-3]

    print(nums[n-1])