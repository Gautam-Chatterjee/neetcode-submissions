class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq1 = [0] * 26
        freq2 = [0] * 26
        l = 0
        r = len(s1) -1
        
        for c in s1:
            freq1[ord(c) - ord('a')]+=1
        
        for c in s2[l:r+1]:
            freq2[ord(c) -ord('a')] +=1


        while r < len(s2):
            if freq1 == freq2:
                return True
            
            r+=1
            if r < len(s2):
                freq2[ord(s2[r]) - ord('a')]+=1
            else:
                return False
            freq2[ord(s2[l]) - ord('a')]-=1
            l+=1
        

        return False

    

   