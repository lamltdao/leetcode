class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        color = 2
        dic = {} # color: area
        nrow = len(grid)
        ncol = len(grid[0])
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        def dfs(r,c,co):
            grid[r][c] = co
            area = 1
            for d in dirs:
                nr = r + d[0]
                nc = c + d[1]
                if 0 <= nr < nrow and 0 <= nc < ncol and grid[nr][nc] == 1:
                    area += dfs(nr,nc,co)
            return area
        for r in range(nrow):
            for c in range(ncol):
                if grid[r][c] == 1:
                    dic[color] = dfs(r,c, color)
                    color += 1
        areas = dic.values()
        ans = max(areas) if len(areas) > 0 else 0
        for r in range(nrow):
            for c in range(ncol):
                if grid[r][c] == 0:
                    s = set()
                    for d in dirs:
                        nr = r + d[0]
                        nc = c + d[1]
                        if 0 <= nr < nrow and 0 <= nc < ncol and grid[nr][nc] >= 2:
                            s.add(grid[nr][nc])
                    ans = max(ans, 1 + sum([dic[colorr] for colorr in s]))
        return ans