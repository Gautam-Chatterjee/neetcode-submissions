class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        pos = set()
        neg = set()
        
        res = []
        
        board = [["."] * n for i in range(n)]
        

        def dfs(r):
            if r==n:
                res.append(["".join(row) for row in board])
                return
            
            for c in range(n):
                if c in cols or (r+c) in pos or (r-c) in neg:
                    continue
                
                board[r][c] = "Q"
                cols.add(c)
                pos.add(r+c)
                neg.add(r-c)

                dfs(r+1)

                board[r][c] = "."
                cols.remove(c)
                pos.remove(r+c)
                neg.remove(r-c)
        dfs(0)
        return res