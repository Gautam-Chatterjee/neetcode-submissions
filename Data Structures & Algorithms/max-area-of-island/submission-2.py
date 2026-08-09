class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        maxi_area = 0
        visit = set()

        def dfs(i,j):
        
            if i < 0 or i >= ROW or j < 0 or j >= COL or (i,j) in visit or grid[i][j]==0:
                return 0
            
            visit.add((i,j))
            return 1 + dfs(i+1,j) + dfs(i-1,j)+ dfs(i,j+1) + dfs(i,j-1)
        

        
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1:
                    maxi_area = max(dfs(r,c), maxi_area)
        
        return maxi_area
        






        