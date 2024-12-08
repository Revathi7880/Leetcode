def constructTransformedArray(nums):
    result= []
    n = len(nums)
    for i in range (n):
        if nums[i] == 0:
            result.append(nums[i])
        elif nums[i] > 0:
            indexNum = nums[i] % n
            result.append(nums[(i+indexNum) % n])
        else:
            indexNum = abs(nums[i]) % n
            result.append(nums[(i-indexNum) % n])
    return result

print(constructTransformedArray([3,-2,1,1]))