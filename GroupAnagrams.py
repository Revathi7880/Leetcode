def groupAnagrams(strs: list[str]):

    resultDict= {}
    for word in strs:
        sortedWord = ''.join(sorted(word))
        if sortedWord in resultDict:
            resultDict[sortedWord].append(word)
        else:
            resultDict[sortedWord] = [word]
    return list(resultDict.values())
        

print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))

                

        