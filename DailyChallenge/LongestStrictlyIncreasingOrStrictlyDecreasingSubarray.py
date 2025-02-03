def longestMonotonicSubarray(nums) -> int:
    n = len(nums)
    maxIncrease, maxDecrease, maxResult = 1, 1, 1
    
    for i in range(n-1):
        if nums[i] < nums[i+1]:
            maxIncrease += 1
            maxDecrease = 1
        elif nums[i] > nums[i+1]:
            maxIncrease = 1
            maxDecrease += 1
        else:
            maxIncrease = 1
            maxDecrease = 1

        maxResult = max(maxIncrease, maxDecrease, maxResult)
    
    return maxResult


    

    
    