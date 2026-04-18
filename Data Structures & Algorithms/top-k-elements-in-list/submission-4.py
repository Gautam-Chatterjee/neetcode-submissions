class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = collections.defaultdict(int)
        ans = []
        for n in nums:
            count[n]+=1

        for v in sorted(count.items(),key =lambda x:x[1], reverse=True):

            ans.append(v[0])
    
        return ans[:k]