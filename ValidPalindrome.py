def isPalindrome(s: str) -> bool:
    lastIndex =  len(s)
    i, j = 0, lastIndex - 1

    while i < j:
        if not s[i].isalnum():
            i += 1
            continue
        if not s[j].isalnum():
            j -= 1
            continue
        if s[i].lower() != s[j].lower():
            print(s[i].lower())
            return False
        i += 1
        j -= 1
    return True

print(isPalindrome("A man, a plan, a canal: Panama"))
        