class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for i in range(numCourses)]
        indegree = [0] * numCourses

        for nxt, prev in prerequisites:
            indegree[nxt] +=1
            adj[prev].append(nxt)
        
        output = []
        

        def dfs(node):
            output.append(node)
            indegree[node]-=1
            
            for nei in adj[node]:
                indegree[nei]-=1
                if indegree[nei] == 0:
                    dfs(nei)
        
        for i in range(numCourses):
            if indegree[i] == 0:
                dfs(i)
        
        return len(output) == numCourses 
        