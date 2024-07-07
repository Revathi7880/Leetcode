def searchRange(nums, target):
    low = 0
    high = len(nums) - 1
    startPosition = -1

    while (low <= high):
        mid = int((low + high)/2)
        if nums[mid] == target:
            startPosition = mid
            high = mid - 1
        elif nums[mid] > target:
            high = mid - 1
        else :
            low = mid + 1
    
    low = 0
    high = len(nums) - 1
    endingPosition = -1

    while (low <= high):
        mid = int((low + high)/2)
        if nums[mid] == target:
            endingPosition = mid 
            low = mid + 1
        elif nums[mid] > target:
            high = mid - 1
        else :
            low = mid + 1
            
    return [startPosition, endingPosition]

consoleInput = input("Enter an array : ")
nums = [int(n) for n in consoleInput.split()]
target = int(input('Enter the target to be searched: '))
startEndIndex = searchRange(nums, target)
print(startEndIndex)

    