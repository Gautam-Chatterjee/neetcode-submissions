class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        max_len = len(nums)
        memo = {}

        def dfs(amt, i):
            if (amt,i) in memo.keys():
                return memo[(amt,i)]

            if i == max_len and amt == target:
                return 1
            if i == max_len:
                return 0
            
            sm = dfs(amt + nums[i],i+1) + dfs(amt - nums[i],i+1)
            
            memo[(amt,i)] = sm
            return sm
        
        return dfs(0, 0)


        