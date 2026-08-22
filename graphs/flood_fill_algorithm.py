class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        def dfs(node1,node2):
            image[node1][node2]=color
            for dx,dy in directions:
                nx,ny=node1+dx,node2+dy
                if nx<0 or ny<0 or nx>=n or ny>=m or image[nx][ny]!=org:
                    continue
                dfs(nx,ny)
        n=len(image)
        m=len(image[0])
        directions=[(0,1),(1,0),(0,-1),(-1,0)]
        
        org=image[sr][sc]
        if org == color:return image
        dfs(sr,sc)
        return image

