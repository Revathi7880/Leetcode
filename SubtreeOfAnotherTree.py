class Solution:
    def isSubtree(self, root, subRoot) -> bool:
        if not subRoot:
            return True
        if not root:
            return False 
            
        def checkSubtree(r, sr):
            if not r and not sr:
                return True
            if not r or not sr:
                return False
            if r.val != sr.val:
                return False
            return checkSubtree(r.left, sr.left) and checkSubtree(r.right, sr.right)
        if checkSubtree(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot) 