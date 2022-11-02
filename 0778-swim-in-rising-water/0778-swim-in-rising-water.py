from heapq import heapify, heappush, heappop
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        """
        find path with minimum score, where score = max value of cells in path
        values of cells are distinc, ranging from 0 -> n^2-1
        """
        # max heap
        nrow = len(grid)
        ncol = len(grid[0])
        INF = 100000
        dist = [[INF for _ in range(ncol)] for _ in range(nrow)]
        dist[0][0] = grid[0][0]
        dirs = [(0,1), (0,-1), (1,0), (-1,0)]
        pq = [(dist[0][0], 0, 0)]
        heapify(pq)
        while len(pq) > 0:
            dis, r, c = heappop(pq)
            # print(r,c)
            if r == nrow-1 and c == ncol-1:
                return dis
            for d in dirs:
                nr = r + d[0]
                nc = c + d[1]
                if 0 <= nr < nrow and 0 <= nc < ncol and max(dis, grid[nr][nc]) < dist[nr][nc]:
                    dist[nr][nc] = max(dis, grid[nr][nc])
                    heappush(pq, (dist[nr][nc], nr, nc))
        return None