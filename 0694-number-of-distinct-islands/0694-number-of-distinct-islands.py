class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        islands = []
        nrow = len(grid)
        ncol = len(grid[0])
        visited = [[False for _ in range(ncol)] for _ in range(nrow)]
        def dfs(r,c,island,offset_r,offset_c):
            nonlocal nrow, ncol
            visited[r][c] = True
            island.append((r-offset_r, c-offset_c))
            dirs = [(0,1), (0,-1), (1,0), (-1,0)]
            for d in dirs:
                nr = r + d[0]
                nc = c + d[1]
                if 0 <= nr < nrow and 0 <= nc < ncol and not visited[nr][nc] and grid[nr][nc] == 1:
                    dfs(nr,nc,island,offset_r,offset_c)
        d = set()
        for r in range(nrow):
            for c in range(ncol):
                if not visited[r][c] and grid[r][c] == 1:
                    # store coordinates of island relative to the first visited cell
                    island = []
                    offset_r = r
                    offset_c = c
                    dfs(r,c,island, offset_r, offset_c)
                    island_s = frozenset(island)
                    d.add(island_s)
        return len(d)