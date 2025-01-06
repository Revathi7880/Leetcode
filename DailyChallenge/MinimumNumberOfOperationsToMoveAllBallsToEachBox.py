def minOperations(boxes: str):
    boxIndex = []
    n = len(boxes)
    for i in range(n):
        if boxes[i] == "1":
            boxIndex.append(True)
        else:
            boxIndex.append(False)
    
    result = []
    for i in range(n):
        count = 0
        for j in range(n):
            if boxIndex[j]:
                count += abs(i - j)
        result.append(count)
    return result

print(minOperations("001011"))
