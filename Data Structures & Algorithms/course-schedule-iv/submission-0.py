class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        indegree = [0] * numCourses
        adj_list = [[]for i in range(numCourses)]
        q = deque()
        prereqs = [set() for i in range(numCourses)]

        for src,dest in prerequisites:
            adj_list[src].append(dest)
            indegree[dest]+=1

        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        

        while q:
            node = q.popleft()
            for n in adj_list[node]:
                prereqs[n].add(node)
                prereqs[n].update(prereqs[node])
                indegree[n]-=1
                if indegree[n]==0:
                    q.append(n)
        
        return [a in prereqs[b] for a,b in queries]