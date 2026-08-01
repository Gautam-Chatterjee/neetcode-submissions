class TimeMap:

    def __init__(self):
        self.store = collections.defaultdict(list)


    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((value, timestamp))
        

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        arr = self.store[key]
        lo = 0
        hi = len(arr)-1

        while lo <=hi:
            mid = (lo+hi) //2
            
            if arr[mid][1] == timestamp:
                return arr[mid][0]
            
            if arr[mid][1] > timestamp:
                hi = mid -1
            
            else:
                lo = mid +1
                res = arr[mid][0]
        
        return res




        
