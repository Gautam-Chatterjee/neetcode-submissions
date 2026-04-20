class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        mini,maxi = 1,1

        for num in nums:
            tmp = maxi*num
            maxi = max(mini*num,tmp,num)
            mini = min(mini*num,tmp,num)
            res = max(res,maxi)

        return res


        