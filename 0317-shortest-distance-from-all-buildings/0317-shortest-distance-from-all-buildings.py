from collections import deque

class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        """
        for each building, calc the min dist from it to other empty lands
        for each empty land, check the one with minimum sum of dist of all buildings
        """
        nrow = len(grid)
        ncol = len(grid[0])
        buildings = set()
        for r in range(nrow):
            for c in range(ncol):
                if grid[r][c] == 1:
                    buildings.add((r,c))
        INF = 100000
        dist = [[[INF for _ in range(len(buildings))] for _ in range(ncol)] for _ in range(nrow)]
        def bfs(r,c,idx):
            nonlocal nrow, ncol
            dist[r][c][idx] = 0
            q = deque()
            q.append((r,c))
            dirs = [(0,1), (0,-1), (1,0), (-1,0)]
            while len(q) > 0:
                row,col = q.popleft()
                for d in dirs:
                    nr = row + d[0]
                    nc = col + d[1]
                    if 0 <= nr < nrow and 0 <= nc < ncol and grid[nr][nc] == 0 and dist[nr][nc][idx] > dist[row][col][idx] + 1:
                        dist[nr][nc][idx] = dist[row][col][idx] + 1
                        q.append((nr,nc))
        idx = 0
        for r,c in buildings:
            bfs(r,c, idx)
            idx += 1
        ans = INF
        for r in range(nrow):
            for c in range(ncol):
                if grid[r][c] == 0:
                    ans = min(ans, sum(dist[r][c]))
        return ans if ans != INF else -1