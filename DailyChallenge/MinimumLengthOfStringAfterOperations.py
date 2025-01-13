def minimumLength(s: str) -> int:
    countDict = {}
    count = 0
    for char in s:
        if char in countDict:
            countDict[char] += 1
        else:
            countDict[char] = 1
    for value in countDict.values():
        charCount = 0
        while value >= 3:
            value -= 2
            charCount += 2
        count += charCount
    return len(s) - count

print(minimumLength("ucvbutgkohgbcobqeyqwppbxqoynxeuuzouyvmydfhrprdbuzwqebwuiejoxsxdhbmuaiscalnteocghnlisxxawxgcjloevrdcj"))

    