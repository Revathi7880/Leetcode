def shiftingLetters(s: str, shifts) -> str:
    diffArray = [0]*(len(s) + 1)
    shiftedS = ""
    for left, right, shift in shifts:
        diffArray[left] += -1 if shift == 0 else 1
        diffArray[right + 1] += 1 if shift == 0 else -1
    
    prefixSumDA = [diffArray[0]]
    prefixSumDA.extend(prefixSumDA[i - 1] + diffArray[i] for i in range(1, len(diffArray)))

    for i in range(len(s)):
        shiftedS += chr(ord('a') + ((ord(s[i]) - ord('a') + prefixSumDA[i]) % 26))
    return shiftedS
        
print(shiftingLetters("abc", [[0,1,0],[1,2,1],[0,2,1]]))
    