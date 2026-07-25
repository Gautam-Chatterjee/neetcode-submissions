# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None or subRoot is None:
            return False
        return self.isSameTree(root, subRoot) or self.isSubtree(root.right, subRoot) or self.isSubtree(root.left, subRoot)
    



    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        res = True
        def dfs(p,q):
            nonlocal res
            if (not p) ^ (not q):
                res = False
                return

            if p and q and p.val != q.val:
                res = False
                return

            if p and q:
                dfs(p.right,q.right)
                dfs(p.left,q.left)
        
        dfs(p,q)
        return res