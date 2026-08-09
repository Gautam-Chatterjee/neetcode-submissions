class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = collections.defaultdict(list)
        indegree = [0] * numCourses
        count = 0
        res = []


        for dst,src in prerequisites:
            adj[src].append(dst)
            indegree[dst]+=1
        
        q = deque()

        for i in range(numCourses):
            if indegree[i] == 0:
               
                q.append(i)
        

        while q:
            curr = q.pop()
            res.append(curr)
            count+=1
            for dst in adj[curr]:
                indegree[dst]-=1
                if indegree[dst] == 0:
                    q.append(dst)
        
        return res if count==numCourses else []
            
            



        



            