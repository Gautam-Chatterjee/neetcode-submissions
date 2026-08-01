class Solution:
    def mySqrt(self, x: int) -> int:
        lo = 1
        hi = x

        while lo <= hi:

            mid = (lo+hi) // 2
            val = mid*mid
            if val == x:
                return mid
            
            if val > x:
                hi = mid-1
            
            if val < x:
                lo = mid+1
        

        return lo -1

        