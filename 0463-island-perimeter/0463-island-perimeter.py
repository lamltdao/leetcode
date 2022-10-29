class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        """
        for each cell in the island, count the number of surrounding 0. Account for edge as well
        """
        nrow = len(grid)
        ncol = len(grid[0])
        visited = [[False for _ in range(ncol)] for _ in range(nrow)]
        perimeter = 0
        dirs = [(0,1), (0,-1), (1,0), (-1,0)]
        def dfs(r,c):
            nonlocal perimeter, nrow, ncol
            cell_peri = 0
            if r == 0 or grid[r-1][c] == 0:
                cell_peri += 1
            if r+1 == nrow or grid[r+1][c] == 0:
                cell_peri += 1
            if c == 0 or grid[r][c-1] == 0:
                cell_peri += 1
            if c+1 == ncol or grid[r][c+1] == 0:
                cell_peri += 1
            perimeter += cell_peri
            visited[r][c] = True
            for d in dirs:
                nr = r+d[0]
                nc = c+d[1]
                if 0 <= nr < nrow and 0 <= nc < ncol and grid[nr][nc] == 1 and not visited[nr][nc]:
                    dfs(nr,nc)
        for r in range(nrow):
            for c in range(ncol):
                if grid[r][c] == 1 and not visited[r][c]:
                    dfs(r,c)
                    return perimeter
        return None
