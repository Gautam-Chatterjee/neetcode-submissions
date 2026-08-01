class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lo = 0
        col = len(matrix[0])
        hi = (len(matrix) * len(matrix[0]))-1
        

        while lo <= hi:
            mid = (lo+hi) // 2
            c = mid % col
            r = mid // col

            if matrix[r][c] == target:
                return True
            
            if matrix[r][c] > target:
                hi = mid -1
            
            else:
                lo = mid +1
        
        return False


        