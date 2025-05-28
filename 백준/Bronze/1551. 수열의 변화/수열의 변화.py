n, k = map(int, input().split())
nums = list(map(int, input().split(',')))

if k ==0:
    print(','.join(map(str, nums)))
else:
    for j in range(k):
        result = []
        for i in range(1, len(nums)):
            result.append(nums[i] - nums[i-1])
        nums = result
    print(','.join(map(str, result)))