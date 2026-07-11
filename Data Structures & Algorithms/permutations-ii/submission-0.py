class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = set()
       

        def dfs(i, curr, dictionary):
            if len(curr) == len(nums):
                res.add(tuple(curr.copy()))
                return 
            
    
            
            for i in range(len(nums)):
                if not dictionary[i]:
                    dictionary[i] = True
                    curr.append(nums[i])
                    dfs(i+1,curr, dictionary)
                    curr.pop()
                    dictionary[i] = False
                    
        dfs(0,[], [False]*len(nums))
        return list(res)
