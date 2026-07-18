class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        visited = [False] * n
        for i, j in edges:
            adj[i].append(j)
            adj[j].append(i)
        

        def dfs(node):
            if visited[node]:
                return
            visited[node] = True
            for nei in adj[node]:
                dfs(nei)
        components = 0
        for node in range(n):
            if not visited[node]:
                components+=1
                dfs(node)
        
        return components


