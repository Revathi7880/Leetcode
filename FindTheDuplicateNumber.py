def findDuplicate(nums) -> int:
    n = len(nums)
    numsSet = set()
    for n in nums:
        if n in numsSet:
            return n
        else:
            numsSet.add(n)

print(findDuplicate([1,3,4,2,2]))