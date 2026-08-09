class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = collections.defaultdict(list)
        indegree = [0] * numCourses
        count = 0

        for dst,src in prerequisites:
            adj[src].append(dst)
            indegree[dst]+=1
        
        q = deque()

        for i in range(numCourses):
            if indegree[i] == 0:
                count+=1
                q.append(i)
        

        while q:
            curr = q.pop()
            for dst in adj[curr]:
                indegree[dst]-=1
                if indegree[dst] == 0:
                    count+=1
                    q.append(dst)
        
        return count == numCourses
            
            



        


