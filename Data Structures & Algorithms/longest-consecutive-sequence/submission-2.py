class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == [] or nums is None:
            return 0
        hash_set = set(nums)
        maxi = 1

        for n in nums:
            if n-1 not in hash_set:
                count = 1
                x = n
                while True:
                    x = x+1
                    if x in hash_set:
                        count+=1
                        maxi = max(count,maxi)
                    else:
                        break
        
        return maxi

        