def majorityElement(nums) -> int:
    countDict = {}
    maxKey = -1
    maxValue = 0
    for n in nums:
        if n in countDict:
            countDict[n] += 1
        else:
            countDict[n] = 1

    for key in countDict.keys():
        if countDict[key] > maxValue:
            maxValue = countDict[key]
            maxKey = key
    return maxKey

print(majorityElement([3,2,3]))

    
    