def containsDuplicate(nums: list[int]) -> bool:
        countDict = {}
        for n in nums:
            if n in countDict:
                countDict[n] += 1
            else:
                countDict[n] = 1
                
        for n in countDict:
            if countDict[n] > 1:
                return True
        return False

print(containsDuplicate([1,1,1,3,3,4,3,2,4,2]))

        