def mergeSimilarItems(items1: list[list[int]], items2: list[list[int]]) -> list[list[int]]:
    countDict = {}
    
    for i in items1:
        if i[0] in countDict:
            countDict[i[0]] += i[1]
        else:
            countDict[i[0]] = i[1]
    
    for i in items2:
        if i[0] in countDict:
            countDict[i[0]] += i[1]
        else:
            countDict[i[0]] = i[1]

    return sorted(countDict.items())

print(mergeSimilarItems([[1,1],[4,5],[3,8]], [[3,1],[1,5]]))

        
        