class Solution:
    def mySqrt(self, x: int) -> int:
        lo = 0
        hi = x
        res = 0

        while lo <= hi:

            mid = (lo+hi) // 2
            val = mid*mid
            if val == x:
                return mid
            
            if val > x:
                hi = mid-1
            
            if val < x:
                lo = mid+1
                res = mid
        
        return res
        

      

        