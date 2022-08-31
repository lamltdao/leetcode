import bisect
class Solution:
    def matrixMedian(self, grid: List[List[int]]) -> int:
        nrow = len(grid)
        ncol = len(grid[0])
        half = (nrow * ncol) // 2 + 1
        l = 0
        r = 10**6
        while l < r:
            m = (l+r) // 2
            num_greater = 0
            for row in range(nrow):
                num_greater += bisect.bisect_right(grid[row], m)
            if num_greater >= half:
                r = m
            else:
                l = m+1
        return r                