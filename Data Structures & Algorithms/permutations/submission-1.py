class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
       

        def dfs(i, curr, dictionary):
            if len(curr) == len(nums):
                res.append(curr.copy())
                return 
            
    
            
            for i in range(len(nums)):
                if not dictionary[i]:
                    dictionary[i] = True
                    curr.append(nums[i])
                    dfs(i+1,curr, dictionary)
                    curr.pop()
                    dictionary[i] = False
                    
        dfs(0,[], [False]*len(nums))
        return res


