def xorQueries(arr: list[int], queries: list[list[int]]) -> list[int]:
    xorArray = [arr[0]]
    resultArray = []
    for i in range(1, len(arr)):
        xorArray.append(xorArray[i - 1] ^ arr[i])
    
    for i in queries:
        if i[0] > 0:
            resultArray.append(xorArray[i[1]] ^ xorArray[i[0] - 1])
        else:
            resultArray.append(xorArray[i[1]])

    return resultArray

print(xorQueries([4,8,2,10], [[2,3],[1,3],[0,0],[0,3]]))






        