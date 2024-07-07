def findMin(nums):
    low = 0
    high = len(nums) - 1

    while low < high:
        mid = int((low + high)/2)
        if nums[mid] > nums[high]:
            low = mid + 1
        else:
            high = mid
    return nums[low]

consoleInput = input('Enter an rotated sorted array: ')
nums = [int(n) for n in consoleInput.split()]

print(findMin(nums))