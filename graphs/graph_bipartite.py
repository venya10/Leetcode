class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        def dfs(node,color):
            vis[node]=color
            newcolor = 1 - color
            for i in graph[node]:
                if vis[i]==-1:
                    if not dfs(i,newcolor):
                        return False
                else:
                    if vis[i]==color:
                        return False
            return True

        n=len(graph)
        vis=[-1]*n
        for i in range(n):
            if vis[i] == -1:
                if not dfs(i, 0):
                    return False
        return True
                    
