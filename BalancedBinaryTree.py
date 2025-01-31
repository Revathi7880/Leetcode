class Solution:
    def isBalanced(self, root) -> bool:
        self.isBalanced = True
        def maxHeight(node):
            if not node:
                return 0
            
            l = maxHeight(node.left)
            r = maxHeight(node.right)

            if abs(l-r) > 1:
                self.isBalanced = False
            return max(l,r) + 1
        maxHeight(root)
        return self.isBalanced