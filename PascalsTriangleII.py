def getRow(rowIndex: int):
    pascalTriangle = [[1]]
    if rowIndex == 0:
        return pascalTriangle[0]
    for i in range(1,rowIndex + 1):
        temp = []
        for j in range(i+1):
            if j == 0:
                temp.append(1)
            elif j == i:
                temp.append(1)
            else:
                temp.append(pascalTriangle[i-1][j-1] + pascalTriangle[i-1][j])
        pascalTriangle.append(temp)
        if i == rowIndex:
            return temp

print(getRow(3))