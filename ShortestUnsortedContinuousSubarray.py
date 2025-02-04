def findUnsortedSubarray(nums) -> int:
    start = -1
    end = -1
    n = len(nums)
    for i in range(n - 1):
        j = i + 1
        if nums[i] > nums[j]:
            if start == -1:
                start = i
            end = j
    if end - start + 1 == 1:
        return 0
    
    minNum = min(nums[start:end+1])
    maxNum = max(nums[start:end+1])

    while start - 1 > -1 and nums[start - 1] > minNum:
        start -= 1
    while end + 1 < n and nums[end+1] < maxNum:
        end += 1
    return end - start + 1

print(findUnsortedSubarray([4,6,1,2,5,8,3,7]))
