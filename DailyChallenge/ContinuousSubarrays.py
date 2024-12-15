def continuousSubarrays(nums) -> int:
    subArrayCount = 0
    countDict = {}
    left, right = 0, 0

    while right < len(nums):
        if nums[right] in countDict:
            countDict[nums[right]] += 1
        else:
            countDict[nums[right]] = 1
        
        while max(countDict) - min(countDict) > 2:
            countDict[nums[left]] -= 1
            if countDict[nums[left]] == 0:
                del countDict[nums[left]]
            left += 1
        subArrayCount += right - left + 1
        right += 1
    return subArrayCount       

print(continuousSubarrays([1,2,3]))