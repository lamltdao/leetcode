class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_island = 0
        nrow = len(grid)
        ncol = len(grid[0])
        visited = [[False for _ in range(ncol)] for _ in range(nrow)]
        def dfs(r,c):
            nonlocal nrow, ncol
            visited[r][c] = True
            if r > 0 and not visited[r-1][c] and grid[r-1][c] == "1":
                dfs(r-1,c)
            if r+1 < nrow and not visited[r+1][c] and grid[r+1][c] == "1":
                dfs(r+1,c)
            if c > 0 and not visited[r][c-1] and grid[r][c-1] == "1":
                dfs(r,c-1)
            if c+1 < ncol and not visited[r][c+1] and grid[r][c+1] == "1":
                dfs(r,c+1)
        for r in range(nrow):
            for c in range(ncol):
                if not visited[r][c] and grid[r][c] == "1":
                    dfs(r,c)
                    num_island += 1
        return num_island
                    