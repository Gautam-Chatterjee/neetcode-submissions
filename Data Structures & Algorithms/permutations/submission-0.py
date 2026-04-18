class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        permutations = []
        
        def dfs(i, picked):
            if len(permutations) == len(nums):
                res.append(permutations.copy())
                return

            for i in range(len(nums)):
                if not picked[i]:
                    permutations.append(nums[i])
                    picked[i] = True
                    dfs(i+1,picked)
                    permutations.pop()
                    picked[i]=False
                
        dfs(0,[False] *len(nums))
        return res

            

        