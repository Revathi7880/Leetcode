def zigzagTraversal(grid):
    m = len(grid)
    n = len(grid[0])
    skip = 0
    result = []
    for i in range(m):
        if i%2 != 0:
            grid[i].reverse()
        for j in range(n): 
            if not skip:
                result.append(grid[i][j])
            skip = not skip
    return result
