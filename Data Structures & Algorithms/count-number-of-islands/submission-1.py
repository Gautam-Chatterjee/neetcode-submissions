class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dir = [(1,0),(0,1),(0,-1),(-1,0)]
        num_islands = 0
        ROWS, COLUMNS = len(grid), len(grid[0])

        def dfs(i,j):
            if grid[i][j] == "0":
                return
            if grid[i][j] == "1":
                grid[i][j] = "0"
            
            for x,y in dir:
                row = i + x
                column = j + y
                if row >= 0 and row < ROWS and column >= 0 and column < COLUMNS:
                    dfs(x+i,y+j)
        

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    dfs(i,j)
                    num_islands +=1
        
        return num_islands




        