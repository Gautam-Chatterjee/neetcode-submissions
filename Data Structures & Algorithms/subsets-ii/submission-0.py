class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subset = []
        res =  set()
        
        def dfs(i):
            if len(nums) == i:
                res.add(tuple(subset.copy()))
                return
            
            subset.append(nums[i])
            dfs(i+1)
            subset.pop()
            dfs(i+1)

        nums.sort()  
        dfs(0)
        return [list(t) for t in res]
        