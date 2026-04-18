class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLUMNS = len(grid), len(grid[0])
        num_islands = 0

        def dfs(i, j):
                if grid[i][j] == "0":
                    return
                if grid[i][j] == "1":
                    grid[i][j] = "0"
                for t in [(0,1), (1,0), (-1,0), (0,-1)]:
                    row = i + t[0]
                    column = j + t[1]
                    if row >= 0 and row < ROWS and column >= 0 and column < COLUMNS:
                        dfs(row, column)
                     
        for i in range(ROWS):
            for j in range(COLUMNS):
                if grid[i][j] == "1":
                    dfs(i,j)
                    num_islands+=1
                   

        return num_islands
                    


            

        