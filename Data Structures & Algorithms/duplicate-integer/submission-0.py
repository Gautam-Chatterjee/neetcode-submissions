class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_set = set()
        for c in nums:
            if c in hash_set:
                return True
            else:
                hash_set.add(c)
        return False