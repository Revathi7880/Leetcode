def countPrefixSuffixPairs(words) -> int:
    indexCount = 0
    n = len(words)
    for i in range(n):
        for j in range(i+1, n):
            if words[j].startswith(words[i]) and words[j].endswith(words[i]):
                indexCount += 1
    return indexCount

print(countPrefixSuffixPairs(["pa","papa","ma","mama"]))
    