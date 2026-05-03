class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dirs = [[0,1], [1,0]]
        grid = [[0 for _ in range(n)] for _ in range(m)] 
        grid[m-1][n-1] = 1

        def dfs(i,j):
            if grid[i][j] != 0:
                return grid[i][j]
            
            val = 0
            for d in dirs:
                x = i + d[0]
                y = j + d[1]
            
                if x >= 0 and x < m and y >= 0 and y < n:
                    if grid[x][y] != 0:
                        val += grid[x][y]
                    else:
                        val += dfs(x,y)
            
            grid[i][j] = val
            return val
        
        return dfs(0,0)


