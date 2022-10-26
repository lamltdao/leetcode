from heapq import heapify, heappush, heappop
class Solution:
    def maximumMinimumPath(self, grid: List[List[int]]) -> int:
        nrow = len(grid)
        ncol = len(grid[0])
        visited = [[False for _ in range(ncol)] for _ in range(nrow)]
        pq = [(-grid[0][0], 0, 0)]
        heapify(pq)
        dirs = [(0,1), (0,-1), (1,0), (-1,0)]
        while len(pq) > 0:
            val, r, c = heappop(pq)
            if r == nrow-1 and c == ncol-1:
                return -val
            for d in dirs:
                nr = r + d[0]
                nc = c + d[1]
                if 0 <= nr and nr < nrow and 0 <= nc and nc < ncol and not visited[nr][nc]:
                    visited[nr][nc] = True
                    heappush(pq, (max(val, -grid[nr][nc]), nr, nc))
        return -1