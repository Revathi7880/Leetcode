def threeSum(nums):
    size = len(nums)
    if size < 3:
        return []
    if size == 3:
        if nums[0] + nums[1] + nums[2] == 0:
            return [nums]
        else:
            return []
    result = []
    sortedNums = sorted(nums)

    for i in range(0,size):
        if i > 0 and sortedNums[i] == sortedNums[i - 1]:
            continue
        j = i + 1
        k = size - 1
        while (j < k) :
            if sortedNums[i] + sortedNums[j] + sortedNums[k] < 0:
                j = j + 1

            elif sortedNums[i] + sortedNums[j] + sortedNums[k] > 0:
                k = k - 1

            else: 
                result.append([sortedNums[i], sortedNums[j], sortedNums[k]])
                j = j + 1
                k = k - 1
                while j < k and sortedNums[j] == sortedNums[j - 1]:
                    j += 1 
                while j < k and sortedNums[k] == sortedNums[k + 1]:
                    k -= 1 

    return result

print(threeSum([-1,0,1,2,-1,-4]))
        