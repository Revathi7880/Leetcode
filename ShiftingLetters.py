def shiftingLetters(s: str, shifts) -> str:
    n = len(shifts)
    suffixShiftsSum = [0]*n
    shiftedS = ""
    suffixShiftsSum[n-1] = shifts[n-1]
    for i in range(n-2, -1, -1):
        suffixShiftsSum[i] = shifts[i] + suffixShiftsSum[i+1]
    
    for i in range(n):
        shiftedS += chr(ord('a') + ((ord(s[i]) - ord('a') + suffixShiftsSum[i]) % 26))
    return shiftedS

print(shiftingLetters("abc",[3,5,9]))