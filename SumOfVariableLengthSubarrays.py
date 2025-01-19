def subarraySum(nums) -> int:
    prefixSum = [nums[0]]
    n = len(nums)
    for i in range(1,n):
        prefixSum.append(prefixSum[i-1]+nums[i])
    totalSum = 0
    for i in range(n):
        start, end = max(0, i-nums[i]), i
        if start == end:
            totalSum += nums[start]
            continue
        if start == 0:
            totalSum += prefixSum[end]
        else:
            totalSum += (prefixSum[end] - prefixSum[start-1])
    return totalSum

print(subarraySum([3,1,1,2]))