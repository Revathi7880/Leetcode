def fourSum(nums, target: int):
    n = len(nums)
    nums = sorted(nums)
    res = []
    for i in range(n):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        for j in range(i + 1, n):
            if j > i + 1 and nums[j] == nums[j-1]:
                continue
            k = j + 1
            l = n - 1
            while k < l:
                fourSum = nums[i] + nums[j] + nums[k] + nums[l]
                if fourSum == target:
                    res.append([nums[i], nums[j], nums[k], nums[l]])
                    k += 1
                    l -= 1
                    while k < l and nums[k] == nums[k - 1]:
                        k += 1
                    while k < l and nums[l] == nums[l+1]:
                        l -= 1

                elif fourSum < target:
                    k += 1
                else:
                    l -= 1
    return res

print(fourSum([-2,-1,-1,1,1,2,2]))
    