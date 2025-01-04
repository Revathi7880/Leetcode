def waysToSplitArray(nums) -> int:
    prefixSum = [nums[0]]
    splitCount = 0
    for i in range(1, len(nums), 1):
        prefixSum.append(nums[i]+ prefixSum[i - 1])
    
    for i in range(len(prefixSum) - 1):
        ele = prefixSum[i]
        if ele >= (prefixSum[-1] - ele):
            splitCount += 1
    return splitCount

print(waysToSplitArray([10,4,-8,7]))

    