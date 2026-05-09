class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {}
        def dfs(i,j):
            if (i,j) in memo.keys():
                return memo[(i,j)]

            if i == len(text1) or j == len(text2):
                return 0

            max_len = 0
            if text1[i] == text2[j]:
                max_len = 1 + dfs(i+1,j+1)
            
            else:
                max_len = max(dfs(i+1,j), dfs(i,j+1))
            
            memo[(i,j)] = max_len
            return max_len 
        
        return dfs(0,0)
                

        