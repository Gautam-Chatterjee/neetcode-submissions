class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(arr):

            if len(arr) == len(nums):
                res.append(arr.copy())
                return
            
            for num in nums:
                if num not in arr:
                    arr.append(num)
                    dfs(arr)
                    arr.pop()
        dfs([])
        return res
        