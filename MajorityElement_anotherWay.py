def majorityElement(nums) -> int:
    sortedNums = sorted(nums)
    n = len(nums)
    maxCount = 1
    maxNum = sortedNums[0]
    currentCount = 1
    for i in range(1,n):
        if sortedNums[i] == sortedNums[i-1]:
            currentCount += 1
            if currentCount > maxCount:
                maxCount = currentCount
                maxNum = sortedNums[i]
        else:
            currentCount = 1
    return maxNum

print(majorityElement([3,2,3]))


