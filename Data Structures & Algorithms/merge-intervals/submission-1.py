class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sorted_intervals = sorted(intervals, key = lambda x: (x[0],x[1]))
        res = [sorted_intervals[0]]
        for start,end in sorted_intervals:
            last_end = res[-1][1]

            if start <= last_end:
                res[-1][1] = max(end,last_end)
            else:
                res.append([start,end])
        
        return res

            
