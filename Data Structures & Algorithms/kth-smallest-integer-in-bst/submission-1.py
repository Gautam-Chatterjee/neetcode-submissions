# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        num = 0
        ans = 0
        def dfs(root):
            nonlocal ans
            nonlocal num
            if root is None:
                return None
            
            dfs(root.left)
            num+=1
            if num == k:
                ans = root.val
                return
            dfs(root.right)
        
        dfs(root)
        return ans



        