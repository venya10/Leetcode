class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        q=deque()
        n=len(prerequisites)
        indegree=[0]*numCourses
        adj=[[] for _ in range(numCourses)]
        sort=[]
        for i,j in prerequisites:
            adj[j].append(i)
            indegree[i]+=1
        for k in range(numCourses):
            if indegree[k]==0:
                q.append(k)
        while q:
            node= q.popleft()
            sort.append(node)
            for neigh in adj[node]:
                indegree[neigh]-=1
                if indegree[neigh]==0:
                    q.append(neigh)
        if len(sort)==numCourses:
            return sort
        return []
