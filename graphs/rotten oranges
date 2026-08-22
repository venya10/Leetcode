from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #get rows and cols
        n=len(grid)
        m=len(grid[0])

        rotten=0
        fresh=0
        q=deque()
        for i in range (n):
            for j in range (m):
                if grid[i][j]==2:
                    rotten+=1
                    q.append((i,j))
                if grid[i][j]==1:
                    fresh+=1
        
        directions=[(0,1),(1,0),(0,-1),(-1,0)]
        time=0
        while q and fresh>0:
            for _ in range(len(q)):
                x,y=q.popleft()

                for dx,dy in directions:
                    nx,ny=x+dx,y+dy
                    if nx < 0 or ny < 0 or nx >= n or ny >= m or grid[nx][ny] != 1:
                        continue
                    grid[nx][ny]=2
                    fresh-=1
                    q.append((nx,ny))
            time+=1
        if (fresh>0):
            return -1 
        else:
            return time



