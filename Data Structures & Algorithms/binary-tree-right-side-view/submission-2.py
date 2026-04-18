# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        stack = [(root,0)]
        res = []

        while stack:
            curr = stack.pop() 
            idx = curr[1]
            if curr[0]:
                if len(res)<idx+1:
                    res.append([curr[0].val if curr[0] else None])
                else:
                    res[idx].append(curr[0].val)
                if curr[0].right: stack.append((curr[0].right,idx+1))
                if curr[0].left: stack.append((curr[0].left,idx+1))
        ans = []
        for arr in res:
            ans.append(arr[-1])
        return ans


