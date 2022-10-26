from collections import deque
class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        """
        bfs from current location
        return min dist[all food cells]
        """
        nrow = len(grid)
        ncol = len(grid[0])
        INF = 100000
        dist = [[INF for _ in range(ncol)] for _ in range(nrow)]
        food_cells = set()
        def bfs(r,c):
            nonlocal nrow, ncol
            dist[r][c] = 0
            q = deque()
            q.append((r,c))
            while len(q) > 0:
                r,c = q.popleft()
                if grid[r][c] == "#":
                    food_cells.add((r,c))
                if r > 0 and grid[r-1][c] != "X" and dist[r-1][c] > dist[r][c]+1:
                    dist[r-1][c] = dist[r][c] + 1
                    q.append((r-1,c))
                if r+1 < nrow and grid[r+1][c] != "X" and dist[r+1][c] > dist[r][c]+1:
                    dist[r+1][c] = dist[r][c] + 1
                    q.append((r+1,c))
                if c > 0 and grid[r][c-1] != "X" and dist[r][c-1] > dist[r][c]+1:
                    dist[r][c-1] = dist[r][c] + 1
                    q.append((r,c-1))
                if c+1 < ncol and grid[r][c+1] != "X" and dist[r][c+1] > dist[r][c]+1:
                    dist[r][c+1] = dist[r][c] + 1
                    q.append((r,c+1))
        print(dist, food_cells)
        for r in range(nrow):
            for c in range(ncol):
                if grid[r][c] == "*":
                    bfs(r,c)
                    break
        ans = INF
        for r,c in food_cells:
            ans = min(ans, dist[r][c])
        return ans if ans != INF else -1