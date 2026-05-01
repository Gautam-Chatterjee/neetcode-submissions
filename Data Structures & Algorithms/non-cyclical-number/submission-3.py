class Solution:
    def isHappy(self, n: int) -> bool:
        s = str(n)
        seen = set()
        
        while True:
            res = 0
            for c in s:
                print(c)
                res+=math.pow(int(c),2)
            
            if res == 1:
                return True
            if res in seen:
                return False
            s = str(int(res))
            seen.add(res) 

        
        return False
        