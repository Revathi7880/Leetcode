def setZeroes(self, matrix) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    col0Tracker = 1
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                if j == 0:
                    col0Tracker = 0
                else:
                    matrix[0][j] = 0
    
    for i in range(1,len(matrix)):
        for j in range(1,len(matrix[0])):
            if j == 0:
                if col0Tracker == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0
            else:
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
    for j in range(1,len(matrix[0])):
        if matrix[0][0] == 0:
            matrix[0][j] = 0
    for i in range(len(matrix)):
        if col0Tracker == 0:
            matrix[i][0] = 0
    
    return matrix

print(setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]]))
    
    

    