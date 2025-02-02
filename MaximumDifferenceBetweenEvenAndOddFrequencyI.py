def maxDifference( s: str) -> int:
    countDict = {}
    for i in s:
        if i in countDict:
            countDict[i] += 1
        else:
            countDict[i] = 1
    minEven = float('inf')
    maxOdd = 0
    for value in countDict.values():
        if value % 2 == 0:
            minEven = min(minEven, value)
        else:
            maxOdd = max(maxOdd, value)
    return maxOdd - minEven

print(maxDifference("mmsmsym"))