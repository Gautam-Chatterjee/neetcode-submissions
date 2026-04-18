class Solution:
    def longestPalindrome(self, s: str) -> str:
        substr = ""
        for i in range(len(s)):
            for j in range(len(s)):
                if self.isPalindrome(s[i:j+1]) and len(s[i:j+1])> len(substr):
                  substr = s[i:j+1]
        
        return substr
    





    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1

        while l<=r:
            if s[l] == s[r]:
                r-=1
                l+=1
            else:
                return False
        
        return True

        