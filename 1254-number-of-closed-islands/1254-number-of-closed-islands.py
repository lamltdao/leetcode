class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        """
        closed island: no 0 block on the edge
        """
        cnt = 0
        nrow = len(grid)
        ncol = len(grid[0])
        visited = [[False for _ in range(ncol)] for _ in range(nrow)]
        def dfs(r,c):
            visited[r][c] = True
            is_closed_island = not (r == 0 or r == nrow-1 or c == 0 or c == ncol-1)
            if r > 0 and not visited[r-1][c] and grid[r-1][c] == 0:
                is_closed_island = dfs(r-1,c) and is_closed_island
            if c+1 < ncol and not visited[r][c+1] and grid[r][c+1] == 0:
                is_closed_island = dfs(r,c+1) and is_closed_island
            if r+1 < nrow and not visited[r+1][c] and grid[r+1][c] == 0:
                is_closed_island = dfs(r+1,c) and is_closed_island
            if c > 0 and not visited[r][c-1] and grid[r][c-1] == 0:
                is_closed_island = dfs(r,c-1) and is_closed_island
            return is_closed_island
        for r in range(nrow):
            for c in range(ncol):
                if grid[r][c] == 0 and not visited[r][c]:
                    is_closed_island = dfs(r,c)
                    if is_closed_island:
                        cnt += 1
        return cnt