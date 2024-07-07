def searchMatrix(matrix, target):

    row =  0
    low = 0
    high = len(matrix) - 1

    while(low <= high):
        midRow = int((low + high)/2)
        if matrix[midRow][0] == target:
            return True
        elif matrix[midRow][0] > target:
            high = midRow - 1
        else:
            low = midRow + 1
    
    if matrix[midRow][0] > target :
        row = midRow -1
    else :
        row = midRow

    low = 0
    high = len(matrix[0]) - 1

    while (low <= high):
        midCol = int((low + high)/2)
        if matrix[row][midCol] == target:
            return True
        elif matrix[row][midCol] > target:
            high = midCol - 1
        else:
            low = midCol + 1
    return False

n = int(input("Enter number of arrays: "))
matrix = []
for i in range(n):
    consoleInput = input(f"Enter {i + 1} array: ")
    arr = [int(n) for n in consoleInput.split()]
    matrix.append(arr)
target = int(input('Enter the target to be searched: '))
result = searchMatrix(matrix, target)
print(result)