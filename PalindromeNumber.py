def isPalindrome(x):
    xString = str(x)
    i = 0
    j = len(xString) - 1

    while i != j and i < j:
        if xString[i] != xString[j]:
            return False
        i += 1
        j -= 1
    return True

x = int(input("Enter a number: "))
print(isPalindrome(x))
        