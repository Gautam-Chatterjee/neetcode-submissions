class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i,total,arr):
            if total == target:
                res.append(arr.copy())
                return
            if total > target or i >= len(nums):
                return
            
            arr.append(nums[i])
            dfs(i, total +nums[i], arr)
            arr.pop()
            dfs(i+1,total,arr)
        
        dfs(0,0,[])
        return res
        