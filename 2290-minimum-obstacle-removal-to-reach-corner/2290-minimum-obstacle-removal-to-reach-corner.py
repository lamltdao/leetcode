from collections import deque
from heapq import heapify, heappush, heappop
class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        """
        find min path from 0,0 to m-1,n-1 with min ob
        """
        nrow = len(grid)
        ncol = len(grid[0])
        INF = 100000
        dist = [[INF for _ in range(ncol)] for _ in range(nrow)]
        dist[0][0] = 0
        dirs = [(0,1), (0,-1), (1,0), (-1,0)]
        # C1: Dijkstra
        # Time: O(mn * log(mn)), as each cell can be pushed and popped at most once
        # Space: O(mn) for the pq
        
        pq = [(0, 0, 0)] # num_obs_removed, r, c
        heapify(pq)
        while len(pq) > 0:
            num_removed,r,c = heappop(pq)
            if dist[r][c] != num_removed: # already found a more optimal for (r,c)
                continue
            for d in dirs:
                nr = r + d[0]
                nc = c + d[1]
                if 0 <= nr < nrow and 0 <= nc < ncol:
                    if grid[r][c] == 0 and num_removed < dist[nr][nc]:
                        dist[nr][nc] = num_removed
                        heappush(pq, (dist[nr][nc], nr, nc))
                    elif grid[r][c] == 1 and num_removed+1 < dist[nr][nc]:
                        dist[nr][nc] = num_removed+1
                        heappush(pq, (dist[nr][nc], nr, nc))
        return dist[nrow-1][ncol-1]
        
        # C2: 0-1 BFS
        # Time: O(mn), as each cell can be pushed and popped at most once
        # Space: O(mn) for the deque
        # q = deque()
        # q.append((0,0))
        # while len(q) > 0:
        #     r,c = q.popleft()
        #     for d in dirs:
        #         nr = r + d[0]
        #         nc = c + d[1]
        #         if 0 <= nr < nrow and 0 <= nc < ncol and dist[r][c] + grid[r][c] < dist[nr][nc]:
        #             dist[nr][nc] = dist[r][c] + grid[r][c]
        #             if grid[r][c] == 0:
        #                 q.appendleft((nr,nc))
        #             else:
        #                 q.append((nr,nc))
        # return dist[nrow-1][ncol-1]