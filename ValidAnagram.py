def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    sCharDict = {}
    tCharDict = {}
    for i in s:
        if i in sCharDict:
            sCharDict[i] += 1
        else:
            sCharDict[i] = 1

    for i in t:
        if i in tCharDict:
            tCharDict[i] += 1
        else:
            tCharDict[i] = 1
    if sCharDict == tCharDict:
        return True
    return False

print(isAnagram('anagram', 'nagaram' ))

        