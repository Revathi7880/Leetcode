def longestConsecutive(nums: list[int]) -> int:
    numSet = set(nums)
    maxLength = 0

    for i in nums:
        if i-1 not in numSet:
            consecutiveLength = 1
            while i + 1 in numSet:
                consecutiveLength += 1
                i = i + 1

            if consecutiveLength > maxLength:
                maxLength = consecutiveLength
    return maxLength

print(longestConsecutive([0,3,7,2,5,8,4,6,0,1]))