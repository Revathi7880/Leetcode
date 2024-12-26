def findTargetSumWays(nums, target: int) -> int:
    sumMap = {}
    def SumCalculator(index, currentSum):
        if (index, currentSum) in sumMap:
            return sumMap[(index, currentSum)]
        if index == len(nums):
            return 1 if currentSum == target else 0
        
        sumMap[(index, currentSum)] = (SumCalculator(index + 1, currentSum + nums[index]) + SumCalculator(index + 1,  currentSum - nums[index]))

        return sumMap[(index, currentSum)]
    return SumCalculator(0, 0)

print(findTargetSumWays([1,1,1,1,1], 3))
    