def luckyNumbers (matrix):
        minSet = set()
        luckyNumber = []
        
        for i in matrix:
            minimum = min(i)
            minSet.add(minimum)
    
        j = 0
    
        while j < len(matrix[0]):
            max = 0
            i = 0
            while i < len(matrix):
                if matrix[i][j] > max:
                    max = matrix[i][j]
                i += 1  
            if max in minSet:
                luckyNumber.append(max)
            j += 1
 
        return luckyNumber

n = int(input("Enter number of arrays: "))
matrix = []
for i in range(n):
    consoleInput = input(f"Enter {i + 1} array: ")
    arr = [int(n) for n in consoleInput.split()]
    matrix.append(arr)
result = luckyNumbers(matrix)
print(result)


        
        