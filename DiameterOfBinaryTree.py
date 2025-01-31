class Solution:
    def diameterOfBinaryTree(self, root) -> int:
        self.res = 0
        def maxHeight(node):
            if not node:
                return 0
            l = maxHeight(node.left)
            r = maxHeight(node.right)

            self.res = max(l+r, self.res) 
            return max(l,r) + 1
        maxHeight(root)
        return self.res