class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        res = []

        def dfs(i, curr, prev):
            if i == len(nums):
                res.append(curr.copy())
                return
            
            
            curr.append(nums[i])
            dfs(i+1, curr, nums[i])
            while i+1 < len(nums) and nums[i+1] == nums[i]:
                i+=1
            curr.pop()
            dfs(i+1, curr, prev)
        
        nums.sort()
        dfs(0,[],0)
    
        return res
            

            
        