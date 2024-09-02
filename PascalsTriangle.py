class Solution(object):
    def generate(self, numRows):

        pascalTree = [[1]]
        if numRows == 1:
            return pascalTree

        for i in range(1, numRows):
            pascalTreeRow = []
            for j in range(i + 1): 
                ele = 0
                if j - 1 >= 0:
                    ele += pascalTree[i-1][j-1]
                if j <= i - 1:
                    ele += pascalTree[i-1][j]
                pascalTreeRow.append(ele)
            pascalTree.append(pascalTreeRow)
        
        return pascalTree
    
numRows = int(input("Enter number of rows: "))
solution = Solution() 
print(solution.generate(numRows))