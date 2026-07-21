import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        res = []

        for p in points:
            dist = -math.sqrt(math.pow(p[0],2)+math.pow(p[1],2))
            heapq.heappush(res, (dist, p[0],p[1]))
        
        while len(res) > k:
            heapq.heappop(res)
        ans = []
        for item in res:
            ans.append([item[1],item[2]])
        
        return ans

        

        

        