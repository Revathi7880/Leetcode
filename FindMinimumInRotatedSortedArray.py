def findMin(nums: list[int]) -> int:
    l , r = 0, len(nums) - 1
    minValue = float('inf')
    

    while l <= r :
        if nums[l] < nums[r]:
            return min(nums[l], minValue)

        mid = (l + r) // 2
        minValue = min(minValue, nums[mid])

        if  nums[mid] >= nums[l]:
            l = mid + 1
        else :
            r = mid - 1
    return minValue

print(findMin([4,5,6,7,0,1,2]))

    