def vowelStrings(words, queries):
    n = len(words)
    prefixCount = [0]*n
    resultCount= []
    vowels = {'a', 'e', 'i', 'o', 'u'}

    for i in range(n):
        isVowel = False
        if words[i][0] in vowels and words[i][-1] in vowels:
            isVowel = True
        if i == 0:
            if isVowel:
                prefixCount[i]= 1
        else:
            if isVowel:
                prefixCount[i] = prefixCount[i-1] + 1
            else:
                prefixCount[i] = prefixCount[i-1] + 0
    
    for p,q in queries:
        if p == 0:
            resultCount.append(prefixCount[q])
        else:
            resultCount.append(prefixCount[q] - prefixCount[p-1])  
    return resultCount


print(vowelStrings(["aba","bcb","ece","aa","e"],[[0,2],[1,4],[1,1]]))



    