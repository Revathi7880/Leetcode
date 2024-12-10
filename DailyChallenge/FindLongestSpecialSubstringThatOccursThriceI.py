def maximumLength(s: str) -> int:
    def validLength(length, s):
        start = 0
        end = length
        substringCount = {}
        while end <= len(s):
            substring = s[start: end]
            if len(set(substring)) == 1:
                if substring in substringCount:
                    substringCount[substring] += 1
                else:
                    substringCount[substring] =  1
            start += 1
            end += 1
        return any(value >= 3 for value in substringCount.values())
            
    left = 1
    right = len(s)
    maxLength = -1
    while left <= right:
        mid = (left + right) // 2
        valid = validLength(mid, s)
        if valid:
            maxLength = max(maxLength, mid)
            left = mid + 1
        else: 
            right = mid - 1
    return maxLength

print(maximumLength("ammmm"))
    