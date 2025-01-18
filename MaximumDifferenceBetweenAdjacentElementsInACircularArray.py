def maxAdjacentDistance(nums) -> int:
    l = len(nums)
    maxDiff = abs(nums[l-1] - nums[0])
    for i in range(1,l):
        diff = abs(nums[i] - nums[i-1])
        maxDiff = max(diff,maxDiff)
    return maxDiff

print(maxAdjacentDistance([1,2,4]))