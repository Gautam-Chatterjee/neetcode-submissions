class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        par = list(range(n+1))
        rank = [1] * (n+1)

        def find(x):
            while x!= par[x]:
                par[x] = par[par[x]]
                x = par[x]
            
            return x
        

        for u,v in edges:
            par1,par2 = find(u),find(v)

            if par1 == par2:
                return [u,v]
            
            if rank[par1] > rank[par2]:
                par[par2] = par[par1]
                rank[par1]+=par[par2]
            else:
                par[par1] = par[par2]
                rank[par2]+=par[1]
            

