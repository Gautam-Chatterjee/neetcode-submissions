class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0: return 0

        l, r = 0,1
        max_length = 1
        letters = set()
        letters.add(s[0])

        while r < len(s) and l < r:
            while s[r] in letters:
                letters.remove(s[l])
                l+=1
            max_length = max(r-l+1, max_length)
            letters.add(s[r])
            r+=1
        
        return max_length



