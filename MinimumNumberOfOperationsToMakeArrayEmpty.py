import math

def minOperations(nums) -> int:
    countDict = {}
    totalOps = 0
    for n in nums:
        if n in countDict:
            countDict[n] += 1
        else:
            countDict[n] = 1
    for value in countDict.values():
        if value == 1:
            return -1
        else:
            totalOps += math.ceil(value/3)
    return totalOps
    
print(minOperations([14,12,14,14,12,14,14,12,12,12,12,14,14,12,14,14,14,12,12]))




        
    
