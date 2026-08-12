class Solution:
    def rob(self, nums: List[int]) -> int:
        
        memo = {}
        def dfs(i):
            if i in memo.keys():
                return memo[i]
            if i >= len(nums):
                return 0
            

            memo[i] = max(dfs(i+2)+nums[i],dfs(i+1))

            return memo[i]
        
        dfs(0)
        return memo[0]
        

        
    
            

        