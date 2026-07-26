class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        mini = math.inf
        l,r = 0,0

        while r <= len(nums) and l <= r:
            if sum(nums[l:r+1]) >= target:
                mini = min(len(nums[l:r+1]), mini)
                l+=1
            else:
                r+=1
        
        return mini if mini!= math.inf else 0

