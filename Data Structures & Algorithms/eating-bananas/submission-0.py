class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        m = max(piles)

        lo = 1
        hi = m
        res = m

        while lo <= hi:
            mid = (lo + hi) // 2
            time = 0
            for num in piles:
                time += num // mid if num % mid == 0 else num // mid +1
            if time <=h:
                res = min(m,mid)
                hi = mid-1
            else:
                lo = mid +1
        

        return res



        