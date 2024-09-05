def twoSum(nums: list[int], target: int) -> list[int]:
    numDict = {}
    length = len(nums)
    for i in range(0, length):
        diffNum = target - nums[i]
        if diffNum in numDict:
            return [numDict[diffNum], i]
        else:
            numDict[nums[i]] = i

print(twoSum([3,2,4], 6))