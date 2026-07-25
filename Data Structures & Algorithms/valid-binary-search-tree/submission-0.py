# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        status = True
        def dfs(root,maxi,mini):
            nonlocal status
            if root is None:
                return
            if not ( (mini < root.val) and  (root.val < maxi) ):
                status = False
                return 
            
            dfs(root.left, root.val, mini)
            dfs(root.right, maxi, root.val)
        
        dfs(root,math.inf, -math.inf)
        return status



        