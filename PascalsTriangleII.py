def getRow(rowIndex: int):
    pascalTriangle = [[1]]
    if rowIndex == 0:
        return pascalTriangle[0]
    for i in range(1,rowIndex + 1):
        temp = [1]*(i+1)
        for j in range(1,i):
            temp[j] = pascalTriangle[i-1][j-1] + pascalTriangle[i-1][j]
        pascalTriangle.append(temp)
        if i == rowIndex:
            return temp

print(getRow(3))