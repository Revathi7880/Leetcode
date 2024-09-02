def maxDepth(root):
    if root == None:
        return 0

    leftDepth = maxDepth(root.left)
    rightDepth = maxDepth(root.right)

    return max(leftDepth, rightDepth) + 1





        