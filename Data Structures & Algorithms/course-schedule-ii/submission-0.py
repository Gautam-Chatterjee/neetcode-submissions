class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        adj_list = [[]for i in range(numCourses)]
        q = deque()
        res = []
        visited = 0

        for dest,src in prerequisites:
            adj_list[src].append(dest)
            indegree[dest]+=1

        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        

        while q:
            node = q.popleft()
            visited +=1
            res.append(node)
            for n in adj_list[node]:
                indegree[n]-=1
                if indegree[n]==0:
                    q.append(n)
        
        return res if visited == numCourses else []
            