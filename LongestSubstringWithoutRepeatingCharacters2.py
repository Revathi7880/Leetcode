def lengthOfLongestSubstring(s: str) -> int:
    l, r, maxLen = 0, 0, 0
    subArray = []

    while r < len(s):
        while s[r] in subArray:
            subArray.remove(s[l])
            l += 1
        subArray.append(s[r])
        maxLen = max(len(subArray), maxLen)
        r += 1
    return maxLen
            
print(lengthOfLongestSubstring("abcabcbb"))