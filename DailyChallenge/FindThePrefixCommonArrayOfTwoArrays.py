def findThePrefixCommonArray(A, B):
    n = len(A)
    countDict = {}
    result = [0]*n
    for i in range(n):
        if A[i] in countDict:
            countDict[A[i]] += 1
        else:
            countDict[A[i]] = 1

        if B[i] in countDict:
            countDict[B[i]] += 1
        else:
            countDict[B[i]] = 1
    
        count = 0
        for key in countDict.keys():
            if countDict[key] == 2:
                count += 1
        result[i] = count
    return result

print(findThePrefixCommonArray([2,3,1],[3,1,2]))


    