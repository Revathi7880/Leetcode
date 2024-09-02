def frequencySort(nums):
    freqDict = {}
    for i in nums:
        if i in freqDict:
            freqDict[i] += 1
        else:
            freqDict[i] = 1
    sortedDict = sorted(freqDict.items(), key = lambda kv: (kv[1], -kv[0]))
    resultList = []

    for i in sortedDict:
        resultList.extend([i[0]] * i[1])

    return resultList

consoleInput = input("Enter array: ")
nums = [int(i) for i in consoleInput.split()]
print(frequencySort(nums))

        