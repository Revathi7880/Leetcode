def sortedSquares(nums):
    sortedSquares= [0] * len(nums)
    left = 0
    right = len(nums) - 1

    for i in range(len(nums) - 1, -1, -1):
        if abs(nums[left]) >= abs(nums[right]):
            sortedSquares[i] = nums[left] * nums[left]
            left += 1
        else : 
            sortedSquares[i] = nums[right] * nums[right]
            right -= 1
    
    return sortedSquares

print(sortedSquares([-7,-3,2,3,11]))
            

        