class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def dfs(node):
            vis[node]=True
            pathvis[node]=1
            for neigh in adj[node]:
                if vis[neigh]==False:
                    if dfs(neigh)==True: 
                        return True
                elif pathvis[neigh]==1:
                    return True
            pathvis[node]=0
            return False
            
        adj=[[] for _ in range(numCourses)]
        n=len(prerequisites)
        for i,j in prerequisites:
            adj[j].append(i)
        
        vis=[False]*numCourses
        pathvis=[0]*numCourses
        for i in range(numCourses):
            if vis[i]==False:
                if dfs(i)==True: return False
        return True
