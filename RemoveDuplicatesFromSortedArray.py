def removeDuplicates(nums):
    if len(nums) == 1:
        return 1
    
    i = 0
    for j in range(len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]
    return nums[:i]

print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))