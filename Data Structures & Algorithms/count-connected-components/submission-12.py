class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par = list(range(n))
        rank = [1] * n
        connected = n

        def find(x):

            while par[x] != x:
                par[x] = par[par[x]]
                x = par[x]

            return x
        

        def union(x,y):
            nonlocal connected
            p1,p2 = find(x), find(y)

            if p1 == p2: 
                return

            if rank[p1] > rank[p2]:
                par[p2] = par[xp1]
                rank[yp2]+=rank[p1]
            else:
                par[p1] = par[p2]
                rank[p1]+=rank[p2]
            connected-=1
        

        for i, j in edges:
            union(i,j)
        

        return connected

        