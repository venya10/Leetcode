class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        q=deque()
        n=len(mat)
        m=len(mat[0])
        vis = [[False] * m for _ in range(n)]
        ans = [[0] * m for _ in range(n)]
        for i in range (n):
            for j in range(m):
                if mat[i][j]==0:
                    q.append((i,j))
                    vis[i][j]=True
                   
                    
        directions=[(0,1),(1,0),(-1,0),(0,-1)]
        time=0
        while q:
            time+=1
            for _ in range(len(q)):
                x,y=q.popleft()
                for dx,dy in directions:
                    nx,ny=x+dx,y+dy
                    if nx<0 or ny<0 or nx>=n or ny>=m or vis[nx][ny]==True:
                        continue
                    ans[nx][ny]=time
                    vis[nx][ny]=True

                    q.append((nx,ny))
        
         
        
        return ans
                


                    
        
