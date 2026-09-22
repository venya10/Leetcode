class Solution:
    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def dfs(i,j):
            vis[i][j]=1
            for dx,dy in neighbours:
                nx,ny=i+dx,j+dy
                if (nx>=0 and ny>=0 and nx<n and ny<m and board[nx][ny]=='O' and vis[nx][ny]==0 ):
                    dfs(nx,ny)
        neighbours=[(0,1),(1,0),(-1,0),(0,-1)]
        n=len(board)
        m=len(board[0])
        vis=[[0]*m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if (i==0 or j==0 or i==n-1 or j==m-1):
                    if board[i][j]=='O'and vis[i][j]!=1:
                        dfs(i,j)
        for i in range(n):
            for j in range(m):
                if vis[i][j]==0:
                    board[i][j]='X'
        
