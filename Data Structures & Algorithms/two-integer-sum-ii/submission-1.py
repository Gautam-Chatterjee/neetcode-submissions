class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:



        l = 0
        r = len(numbers)-1

        while l<r:
            curr = numbers[l] + numbers[r]
            if curr == target:
                return [l+1,r+1]
            
            if curr < target:
                l+=1
            if curr>target:
                r-=1
        
        return []
        # for i in range(len(numbers)) :
        #     lo = i+1
        #     hi = len(numbers) -1
        #     tmp = target - numbers[i]
        
        #     while lo <= hi:
        #         mid = lo + (hi - lo)//2
        #         if tmp == numbers[mid]:
        #             return [i+1,mid+1]
        #         if tmp > numbers[mid]:
        #             lo = mid+1
        #         if tmp <numbers[mid]:
        #             hi = mid-1
                    
        # return []


 




        