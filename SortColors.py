def sortColors(nums):
    countDict = {0:0, 1:0, 2:0}
    initialIndex = 0
    for n in nums:
        countDict[n] += 1
    
    for color in countDict.keys():
        for i in range(initialIndex,initialIndex + countDict[color]):
            nums[i] = color
        initialIndex += countDict[color]
    return nums

print(sortColors([2,0,2,1,1,0]))
    