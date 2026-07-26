class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        mini = math.inf
        l, total = 0,0

        for r in range(len(nums)):
            total += nums[r]

            while total >= target:
                mini = min(mini, r-l+1)
                total -= nums[l]
                l+=1
            
        
        return mini if mini!= math.inf else 0

