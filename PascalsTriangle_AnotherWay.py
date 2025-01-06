def generate(numRows: int):
    pascalTriangle = [[1]]
    for i in range(1,numRows):
        temp = []
        for j in range(i+1):
            if j == 0:
                temp.append(1)
            elif j == i:
                temp.append(1)
            else:
                temp.append(pascalTriangle[i-1][j-1] + pascalTriangle[i-1][j])
        pascalTriangle.append(temp)
    return pascalTriangle

print(generate(10))