def isSubsequence(s: str, t: str) -> bool:
    count = 0
    i, j = 0, 0

    while i < len(t) and j < len(s):
        if (t[i] == s[j]):
            count += 1
            i += 1
            j += 1
        else :
            i += 1
    
    if count == len(s):
        return True
    else: 
        return False

print(isSubsequence("abc", "ahbgdc"))
            
    