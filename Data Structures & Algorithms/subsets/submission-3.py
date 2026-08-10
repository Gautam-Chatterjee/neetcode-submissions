class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def dfs(i, vals):
           
            if i == len(nums):
                res.append(vals.copy())
                return
             
    
            vals.append(nums[i])
            dfs(i+1,vals)
            vals.pop()
            dfs(i+1, vals)
        
        dfs(0,[])
        return res




