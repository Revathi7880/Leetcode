def findAnagrams(s: str, p: str):
    resultIndex = [] 
    p = sorted(p)
    left = 0
    right = len(p)
    while left < len(s) and right <= len(s):
        if p == sorted(s[left : right]):
            resultIndex.append(left)
        left += 1
        right += 1
        
    return resultIndex

print(findAnagrams("ababba","ba"))