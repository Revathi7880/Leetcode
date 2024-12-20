def convert(s: str, numRows: int) -> str:
    if numRows == 1 or numRows >= len(s):
        return s
    stringMatrix = [[] for _ in range(numRows)] 
    i = 0
    down = True
    for char in s:
        if i == 0:
            down = True
        elif i == numRows - 1:
            down = False
        stringMatrix[i].append(char)
        if down:
            i += 1
        else:
            i -= 1
    
    resultString = ''
    for row in stringMatrix:
        rowString = ''.join(row)
        resultString += rowString
    return resultString


print(convert("PAYPALISHIRING", 4))


    