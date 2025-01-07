def generate(numRows: int):
    pascalTriangle = [[1]]
    for i in range(1,numRows):
        temp = [1]*(i+1)
        for j in range(1,i):
            temp[j] = pascalTriangle[i-1][j-1] + pascalTriangle[i-1][j]
        pascalTriangle.append(temp)
    return pascalTriangle

print(generate(10))