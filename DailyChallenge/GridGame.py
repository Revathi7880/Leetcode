def gridGame(grid) -> int:
    n = len(grid[0])
    firstRow = [grid[0][0]]
    secondRow = [0]*n
    secondRow[n-1] = grid[1][n-1]

    for i in range(1,n):
        firstRow.append(grid[0][i] + firstRow[i-1])
        secondRow[n-i-1] = grid[1][n-i-1] + secondRow[n-i]

    minValue = float('inf')
    for i in range(n):
        maxValue = max((firstRow[n-1] - firstRow[i]),(secondRow[0] - secondRow[i]))
        if maxValue < minValue:
            minValue = maxValue
    return minValue

print(gridGame([[20,3,20,17,2,12,15,17,4,15],[20,10,13,14,15,5,2,3,14,3]]))


            

    