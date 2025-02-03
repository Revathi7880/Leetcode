def numSubarrayProductLessThanK(nums, k: int) -> int:
    count = 0
    product = 1
    n = len(nums)
    left = 0
    for right in range(n):
        product = product * nums[right]
        while left <= right and product >= k:
            product = product / nums[left]
            left += 1
        count = count + (right - left + 1)
    return count

print(numSubarrayProductLessThanK([10,9,10,4,3,8,3,3,6,2,10,10,9,3], 19))