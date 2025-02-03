def threeSumClosest(nums, target: int) -> int:
    closestSum = float('inf')
    sortedNums = sorted(nums)
    n = len(nums)
    for i in range(n):
        if i > 0 and sortedNums[i] == sortedNums[i-1]:
            continue
        j = i + 1
        k = n - 1
        while j < k:
            threeSum = sortedNums[i] + sortedNums[j] + sortedNums[k]
            if target == threeSum:
                return threeSum
            elif target > threeSum:
                j += 1
            else:
                k -= 1
            if abs(target - threeSum) < abs(target - closestSum):
                closestSum = threeSum
    return closestSum

print(threeSumClosest([1,1,1,0], -100))

            

    