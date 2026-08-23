class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        q=deque()
        n=len(grid)
        directions=[(0,1),(1,0),(-1,0),(0,-1),(-1,-1),(-1,1),(1,-1),(1,1)]
        if grid[0][0]==1 or grid[n-1][n-1]==1:
            return -1
        q.append((0,0,1))
        while q:
            x,y,dist=q.popleft()

            if x == n - 1 and y == n - 1:
                return dist
            for dx,dy in directions:
                nx,ny=x+dx,y+dy
                if nx<0 or ny<0 or nx>=n or ny>=n or grid[nx][ny]!=0:
                    continue
                grid[nx][ny]=1
                q.append((nx,ny,dist+1))
        return -1
                
