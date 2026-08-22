class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n=len(grid)
        m=len(grid[0])
        q=deque()
        count=0
        directions=[(0,1),(1,0),(-1,0),(0,-1)]
        for i in range(n):
            for j in range(m):
                if grid[i][j]=='1':
                    q.append((i,j))
                   
                    while q:
                        x,y=q.popleft()
                        for dx,dy in directions:
                            nx,ny=x+dx,y+dy
                            if nx<0 or ny<0 or nx>=n or ny>=m or grid[nx][ny]!='1':
                                continue
                            q.append((nx,ny))
                            grid[nx][ny]="0"
                            
                    count+=1
        return count

        
