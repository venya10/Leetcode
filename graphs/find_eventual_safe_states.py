class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n=len(graph)
        safe=[]
        q=deque()
        indegree=[0]* n
        rev=[[]for _ in range(n)]
        for i in range(n):
            indegree[i] = len(graph[i])
            for j in graph[i]:
                rev[j].append(i)
        
        for i in range(n):
            if indegree[i]==0:
                q.append(i)
                safe.append(i)
        while q:
            node=q.popleft()
            for neigh in rev[node]:
                indegree[neigh]-=1
                if indegree[neigh]==0:
                    q.append(neigh)
                    safe.append(neigh)
        safe.sort()
        return safe
