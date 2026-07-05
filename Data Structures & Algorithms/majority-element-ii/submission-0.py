from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        limit = len(nums)/3
        mp = Counter()
        res = []
        for num in nums:
            if num not in res:
                mp[num] +=1
                if mp[num] > limit:
                    res.append(num)
        
        return res


        