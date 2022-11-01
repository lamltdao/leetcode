class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        """
        for each cell on the first row
            try dropping it
                if cell[r][c] ==1 and not (edge right or cell[r][c+1] == -1)
                    tmp_c += 1
                    r += 1
                elif cell[r][c] == -1 and not (edge left or cell[r][c-1] == 1):
                    tmp_c -= 1
                    r += 1
                else: # stuck
        Time: O(mn), Space: O(n), m:row, n: col
        """
        nrow = len(grid)
        ncol = len(grid[0])
        ans = [-1 for _ in range(ncol)]
        for c in range(ncol):
            tmp_c = c
            stuck = False
            for r in range(nrow):
                if grid[r][tmp_c] == 1 and not( (tmp_c+1 == ncol) or grid[r][tmp_c+1] == -1):
                    tmp_c += 1
                elif grid[r][tmp_c] == -1 and not( (tmp_c == 0) or grid[r][tmp_c-1] == 1):
                    tmp_c -= 1
                else:
                    stuck = True
                    break
            if not stuck:
                ans[c] = tmp_c
        return ans
            
        