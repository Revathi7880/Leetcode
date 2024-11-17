def minSubArrayLen(target: int, nums):
    l, r, sum = 0, 0, 0
    minLength = float('inf')

    while r < len(nums):
        sum += nums[r]
        while sum >= target:
            minLength = min(minLength, r-l+1)
            sum -= nums[l]
            l += 1
        r += 1
    if minLength ==  float('inf'):
        return 0
    return minLength

print(minSubArrayLen(7, [2,3,1,2,4,3]))


        