class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        for i in range(len(numbers)) :
            lo = i+1
            hi = len(numbers) -1
            tmp = target - numbers[i]
        
            while lo <= hi:
                mid = lo + (hi - lo)//2
                if tmp == numbers[mid]:
                    return [i+1,mid+1]
                if tmp > numbers[mid]:
                    lo = mid+1
                if tmp <numbers[mid]:
                    hi = mid-1
                    
        return []


    # def binarySearch(self,nums,target):
        

    #     return -1






        