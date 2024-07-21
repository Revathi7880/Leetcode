def restoreMatrix(rowSum, colSum):
    matrix = [[0] * len(colSum) for _ in range(len(rowSum))]

    i , j = 0, 0

    while i < len(rowSum) and j < len(colSum):
        minimum = min(rowSum[i], colSum[j])
        matrix[i][j] = minimum
        rowSum[i] -= minimum
        colSum[j] -= minimum

        if rowSum[i] == 0:
            i += 1
        if colSum[j] == 0:
            j += 1
    
    return matrix

consoleInput1 = input("Enter rowSum array: ")
consoleInput2 = input("Enter colSum array: ")

rowSum = [int(n) for n in consoleInput1.split()]
colSum = [int(n) for n in consoleInput2.split()]
print(colSum)

print(restoreMatrix(rowSum, colSum))
            
            

        