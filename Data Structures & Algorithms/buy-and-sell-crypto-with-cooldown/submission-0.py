class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}

        def dfs(i, buying):
             
            if (i,buying) in memo.keys():
                return memo[(i,buying)]
            if i >= len(prices):
                return 0
            
            
            cooldown = dfs(i+1, buying)
            if buying:
                buy = max(cooldown, dfs(i+1, not buying) - prices[i])
                memo[(i,buying)] = buy
                return buy
            
            else:
                sell = max(cooldown, prices[i] + dfs(i+2, not buying))
                memo[(i,buying)] = sell
                return sell
            
        return dfs(0, True)
