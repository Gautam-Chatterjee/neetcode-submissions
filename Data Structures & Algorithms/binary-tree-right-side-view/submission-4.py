# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []


        def dfs(root, i):
            nonlocal res 
            if root is None:
                return None
            
            if i == len(res):
                res.append([])
            
            res[i].append(root.val)
            dfs(root.left,i+1)
            dfs(root.right,i+1)
        
        dfs(root,0)
        ans = []
        for r in res:
            ans.append(r[-1])
        return ans


