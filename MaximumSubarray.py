def maxSubArray(nums) -> int:
    maxSum = float('-inf')
    currentSum = 0

    for n in nums:
        currentSum += n
        maxSum = max(currentSum, maxSum)
        if currentSum < 0:
            currentSum = 0
    return maxSum

print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))


    