# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.depth(root, 0)
    
    def depth(self, root, val):
        if root == None:
            return val
            
        return max(self.depth(root.left,val+1), self.depth(root.right,val+1))



        