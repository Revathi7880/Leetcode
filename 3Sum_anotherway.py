def threeSum(nums):
    resList = []
    n = len(nums)
    sortedNums = sorted(nums)

    for i in range(n):
        if i > 0 and sortedNums[i] == sortedNums[i-1]:
            continue
        j = i + 1
        k = n-1
        while j < k:
            threeSum = sortedNums[i] + sortedNums[j] + sortedNums[k]
            if threeSum == 0:
                resList.append([sortedNums[i],sortedNums[j],sortedNums[k]])
                j += 1
                k -= 1
                while j < k and sortedNums[j] == sortedNums[j-1]:
                    j += 1
                while j < k and sortedNums[k] == sortedNums[k+1]:
                    k -= 1
            elif threeSum < 0:
                j += 1
            else:
                k -= 1
    
    return resList
        
print(threeSum([-1,0,1,2,-1,-4]))
        