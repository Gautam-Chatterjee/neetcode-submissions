class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        res = set()
        nums.sort()

        def dfs(total, i, arr):
            if total==target:
                res.add(tuple(arr.copy()))
                return
            
            if total > target or len(nums) ==i:
                return
            
            arr.append(nums[i])
            dfs(total +nums[i],i+1, arr)
            arr.pop()
            dfs(total,i+1, arr)
        
        dfs(0,0,[])
        return [list(t) for t in res]

