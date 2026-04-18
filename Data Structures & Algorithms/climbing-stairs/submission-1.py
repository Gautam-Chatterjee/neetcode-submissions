class Solution:
    def climbStairs(self, n: int) -> int:
        ways = {}

        def numWays(n):
            if n == 0:
                return 1
            if n < 0:
                return 0
            
            ans  = (ways[n-1] if n-1 in ways else numWays(n-1)) + (ways[n-2] if n-2 in ways else numWays(n-2))
            ways[n] = ans
            return ans
        
        return numWays(n)

                