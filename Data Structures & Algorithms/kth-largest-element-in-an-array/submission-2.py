class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []

        for num in nums:
            heapq.heappush(min_heap, num)
        
        count = 0
        while count  < len(nums) - k:
            heapq.heappop(min_heap)
            count+=1
        
        return min_heap[0]
           

        