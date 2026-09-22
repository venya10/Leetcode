class Solution:
    def numEnclaves(self, grid: list[list[int]]) -> int:
        count=0
        def dfs(i,j):
            vis[i][j]=1
            for dx,dy in neighbours:
                nx,ny=dx+i,dy+j
                if nx>=n or ny>=m or nx<0 or ny<0 or grid[nx][ny]!=1 or vis[nx][ny]==1:
                    continue
                dfs(nx,ny)

   
        n=len(grid)
        m=len(grid[0])
        neighbours=[(1,0),(0,1),(-1,0),(0,-1)]
        vis=[[0] *m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if (i==0 or j==0 or i==n-1 or j==m-1):
                    if grid[i][j]==1 and vis[i][j]==0:
                        dfs(i,j)
        count=0
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1 and vis[i][j]==0:
                    count+=1
        return count
            
        
