def nextPermutation(nums) -> None:
    n = len(nums)
    breakInd = -1
    for i in range(n-2,-1,-1):
        if nums[i] < nums[i+1]:
            breakInd = i
            break
    
    if breakInd == -1:
        nums.reverse()


    for i in range(n-1,breakInd,-1):
        if nums[i] > nums[breakInd]:
            temp = nums[i]
            nums[i] = nums[breakInd]
            nums[breakInd] = temp
            nums[breakInd+1:] = reversed(nums[breakInd+1:])
            break

    return nums

print(nextPermutation([2,1,5,4,3,0,0]))
    
    
    