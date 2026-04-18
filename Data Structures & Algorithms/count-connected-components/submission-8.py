class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par = [i for i in range(n)]
        rank = [1] * n

        def find(node):
            p = par[node]
            while p != par[p]:
                par[p] = par[par[p]]
                p = par[p]
            return p

        def union(n1,n2):
            p1,p2 = find(n1),find(n2)
            if p1==p2:
                return True

            if rank[p1] > rank[p2]:
                par[p2]=p1
                rank[p1]+=rank[p2]
            else:
                par[p1]=p2
                rank[p2]+=rank[p1]
            return False

        

        for i,j in edges:
            union(i,j)
         
        connected = set()
        for v in par:
           connected.add(find(v))
        
        return len(connected)

