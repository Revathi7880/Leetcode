from collections import deque

class Solution:
    def levelOrder(self, root):
        res = []
        q = deque()
        q.append(root)

        while q:
            level = []
            n = len(q)
            for i in range(n):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
                
            if level:
                res.append(level)
        return res