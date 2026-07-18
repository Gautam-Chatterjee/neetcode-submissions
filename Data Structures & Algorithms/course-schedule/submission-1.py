class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        adj_list = [[]for i in range(numCourses)]
        q = deque()
        visited = 0

        for src,dest in prerequisites:
            adj_list[src].append(dest)
            indegree[dest]+=1

        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        

        while q:
            node = q.popleft()
            visited +=1
            for n in adj_list[node]:
                indegree[n]-=1
                if indegree[n]==0:
                    q.append(n)
        
        return visited == numCourses
            


