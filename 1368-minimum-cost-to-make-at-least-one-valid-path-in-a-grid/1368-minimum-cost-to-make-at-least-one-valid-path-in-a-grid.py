from heapq import heapify, heappush, heappop
from collections import deque
class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        """
        pq (cost, r,c, set())
        
        [0, 0, 0]
        visited
        pop
            push (cost, visited, nr, nc)
            
            push(cost+1, ...)
        """
        nrow = len(grid)
        ncol = len(grid[0])
        dirs = [(0,1,1), (0,-1,2), (1,0,3), (-1,0,4)]
        INF = 100000
        dist = [[INF for _ in range(ncol)] for _ in range(nrow)]
        dist[0][0] = 0
        q = deque()
        q.append((0,0))
        while len(q) > 0:
            r,c = q.popleft()
            for dr,dc,di in dirs:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < nrow and 0 <= nc < ncol:
                    if di == grid[r][c] and dist[r][c] < dist[nr][nc]:
                        dist[nr][nc] = dist[r][c]
                        q.append((nr,nc))
                    elif dist[r][c]+1 < dist[nr][nc]:
                        dist[nr][nc] = dist[r][c] + 1
                        q.append((nr,nc))
        return dist[nrow-1][ncol-1] if dist[nrow-1][ncol-1] != INF else -1
        # pq = [(0, 0, 0)]
        # heapify(pq)
        # dirs = [(0,1,1), (0,-1,2), (1,0,3), (-1,0,4)]
        # visited = [[False for _ in range(ncol)] for _ in range(nrow)]
        # while len(pq) > 0:
        #     cost, r,c = heappop(pq)
        #     visited[r][c] = True
        #     if r == nrow-1 and c == ncol-1:
        #         return cost
        #     for dr,dc,di in dirs:
        #         nr = r + dr
        #         nc = c + dc
        #         if 0 <= nr < nrow and 0 <= nc < ncol and not visited[nr][nc]:
        #             if di == grid[r][c]:
        #                 heappush(pq,(cost, nr, nc))
        #             else:
        #                 heappush(pq,(cost+1, nr, nc))
        # return -1
        