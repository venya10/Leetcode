class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj=[[] for _ in range(n+1)]
        for i,j,m in times:
            adj[i].append((j,m))
        print(adj)
        dist = [float('inf')] * (n + 1)
        dist[k]=0
        dist[0]=-1

        pq=[(0,k)]
        while pq:
            cur_dist,node=heapq.heappop(pq)
            for neigh,weight in adj[node]:
                new_dist=cur_dist+weight
                if new_dist<dist[neigh]:
                    dist[neigh]=new_dist
                    heapq.heappush(pq,(new_dist,neigh))
        ans=max(dist[1:])
        if ans== float('inf'):
            return -1
        return ans
