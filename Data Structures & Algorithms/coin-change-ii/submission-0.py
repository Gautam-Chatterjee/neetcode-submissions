class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}
        def dfs(i, amt):
            if (i,amt) in memo.keys():
                return memo[(i,amt)]

            if amt < 0 or i==len(coins):
                return 0
            
            if amt == 0:
                return 1
            
    
            take = dfs(i,amt-coins[i])
            skip = dfs(i+1,amt)
            memo[(i,amt)] = skip + take
            return memo[(i,amt)]
                
        return dfs(0,amount)