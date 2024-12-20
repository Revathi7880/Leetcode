class Solution:
    def reverseOddLevels(self, root):
        self.traverse(root.left, root.right, 1)
        return root

    def traverse(self, leftChild, rightChild, level):
        if leftChild is None or rightChild is None:
            return
        
        if level % 2 != 0:
            swapTemp = leftChild.val
            leftChild.val = rightChild.val
            rightChild.val = swapTemp
        
        self.traverse(leftChild.left, rightChild.right, level + 1)
        self.traverse(leftChild.right, rightChild.left, level + 1)
