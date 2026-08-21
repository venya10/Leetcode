class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(node):
            vis[node]=True
            for neighbour in adj[node]:
                if vis[neighbour]==False:
                    dfs(neighbour)
        n=len(isConnected)
        adj=[[] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if isConnected[i][j]==1 and i!=j:
                    adj[i].append(j)
        
        vis=[False]*n
        count=0
        for i in range(n):
            if vis[i]==False:
                dfs(i)
                count+=1
        return count
