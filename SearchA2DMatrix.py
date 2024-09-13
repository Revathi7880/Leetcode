def searchMatrix(matrix: list[list[int]], target: int) -> bool:

    n = len(matrix[0])
    for row in matrix:
        if row[n - 1] == target:
            return True
        elif row[n - 1] > target:
            l = 0
            r = n - 1
            while l <= r:
                mid = (l + r) // 2
                if row[mid] == target: 
                    return True
                elif row[mid] > target:
                    r = mid - 1
                else: 
                    l = mid + 1
    return False

print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))


        