class Solution:
    def maxDepth(self, root) -> int:
        def maxHeight(rootNode, height):
            if not rootNode:
                return height
            
            lHeight = maxHeight(rootNode.left, height+1)
            rHeight = maxHeight(rootNode.right, height+1)
            return max(lHeight, rHeight)
        
        return maxHeight(root, 0)