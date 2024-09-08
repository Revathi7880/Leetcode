from collections import defaultdict 
def isValidSudoku(board: list[list[str]]):
    rowMap = defaultdict(set)
    colMap = defaultdict(set)
    boxMap = defaultdict(set)

    for i in range(0,9):
        for j in range(0,9):
            if board[i][j] == '.':
                continue
            if board[i][j] in rowMap[i] or board[i][j] in colMap[j] or board[i][j] in boxMap[(i//3, j//3)]:
                return False
 
            rowMap[i].add(board[i][j])
            colMap[j].add(board[i][j])
            boxMap[(i//3, j//3)].add(board[i][j])
    return True
    
print(isValidSudoku([["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))


        