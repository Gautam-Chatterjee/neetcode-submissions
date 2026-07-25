# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
      
        res = []
        q = deque()
        q.append(root)

        while q:
            length = len(q)
            new_arr = []
            for _ in range(length):
                    node = q.popleft()
                    if node:
                        new_arr.append(node.val)
                        q.append(node.left)
                        q.append(node.right)
            if new_arr:
                res.append(new_arr)
        
        return res
            


      
            

        
        