class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        hi = max(piles)
        lo = 1
        mini = hi
        while lo <= hi:
            mid = (lo+hi)//2
            hours = self.hours_needed(piles,mid)
            if hours <= h:
                mini = mid
                hi = mid-1
            else:
                lo = mid +1
                
        
        return mini
            


    
    def hours_needed(self,piles,k):
        hours = 0
        for pile in piles:
            hours+= math.ceil(float(pile)/k)
        return hours


        