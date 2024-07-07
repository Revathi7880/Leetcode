def searchInsertPosition(nums, target):
    low, high = 0, len(nums) - 1

    while (low <= high):
        mid = int((low + high) / 2)
        if target == nums[mid]:
            return mid
        elif target < nums[mid]:
            high = mid - 1
        else :
            low = mid + 1

    return mid if nums[mid] > target else mid + 1

consoleInput = input("Enter an array : ")
nums = [int(n) for n in consoleInput.split()]
target = int(input('Enter the key to be searched: '))

print(searchInsertPosition(nums, target))
