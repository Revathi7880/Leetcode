def canConstruct(s: str, k: int) -> bool:
    countDict = {}
    oddFreq = 0
    if len(s) < k:
        return False
    for l in s:
        if l in countDict:
            countDict[l] += 1
        else:
            countDict[l] = 1
    
    for value in countDict.values():
        if value % 2 != 0:
            oddFreq += 1
    return True if k >= oddFreq else False

print(canConstruct("annabelle", 2))
    



    