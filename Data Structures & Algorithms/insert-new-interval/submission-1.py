class Solution:
    def insert(self, intervals: List[List[int]], new_interval: List[int]) -> List[List[int]]:


        res = []

        for i,interval in enumerate(intervals):
            if new_interval[1] < interval[0]:
                res.append(new_interval)
                return res + intervals[i:]
            elif new_interval[0] > interval[1]:
                res.append(interval)
            
            else:
                new_interval = (min(interval[0],new_interval[0]), max(interval[1],new_interval[1]))
        
        res.append(new_interval)
        return res

        