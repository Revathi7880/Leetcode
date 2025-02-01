def findValidPair(s: str) -> str:
    countDict = {}
    res = ""
    for i in s:
        if i in countDict:
            countDict[i] += 1
        else:
            countDict[i] = 1
    n = len(s)
    for i in range(n-1):
        num = int(s[i])
        nextNum = int(s[i+1])
        if num != nextNum and countDict[s[i]] == num and countDict[s[i+1]] == nextNum:
            res = f'{num}{nextNum}'
            break
    return res

print(findValidPair("2523533"))
        
