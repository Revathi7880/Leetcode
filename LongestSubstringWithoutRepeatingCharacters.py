def lengthOfLongestSubstring(s):
    i, j = 0, 0
    charDict = {}
    subLength = 0

    for c in range(len(s)):
        if s[c] in charDict:
            index = charDict[s[c]]
            if index >= i:
                if j - i > subLength:
                    subLength = j - i
                i = index + 1
            charDict[s[c]] = c
            
        else:
            charDict[s[c]] = c
        j += 1

    return j - i  if j - i > subLength else subLength 


s = input("Enter a string: ")
print(lengthOfLongestSubstring(s))
        