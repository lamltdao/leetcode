class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        """
        for each cell in the island, count the number of surrounding 0. Account for edge as well
        """
        nrow = len(grid)
        ncol = len(grid[0])
        perimeter = 0
        for r in range(nrow):
            for c in range(ncol):
                if grid[r][c] == 1:
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
        return perimeter
