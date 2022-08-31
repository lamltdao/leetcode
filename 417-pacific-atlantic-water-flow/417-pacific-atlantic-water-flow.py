class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        num_row = len(heights)
        num_col = len(heights[0])
        pac = [[False if r != 0 and c != 0 else True for c in range(num_col)] for r in range(num_row)]
        atl = [[False if r != num_row-1 and c != num_col-1 else True for c in range(num_col)] for r in range(num_row)]
        def dfs(r,c, oce, visited):
            visited[r][c] = True
            oce[r][c] = True
            # N,E,S,W
            if r > 0 and not visited[r-1][c] and heights[r][c] <= heights[r-1][c]:
                dfs(r-1,c,oce,visited)
            if c+1 < num_col and not visited[r][c+1] and heights[r][c] <= heights[r][c+1]:
                dfs(r,c+1,oce,visited)
            if r+1 < num_row and not visited[r+1][c] and heights[r][c] <= heights[r+1][c]:
                dfs(r+1,c,oce,visited)
            if c > 0 and not visited[r][c-1] and heights[r][c] <= heights[r][c-1]:
                dfs(r,c-1,oce,visited)
        visited_pac = [[False for _ in range(num_col)] for _ in range(num_row)]
        visited_atl = [[False for _ in range(num_col)] for _ in range(num_row)]
        for i in range(num_col):
            dfs(0,i,pac, visited_pac)
        for i in range(num_row):
            dfs(i,0,pac, visited_pac)
        for i in range(num_col):
            dfs(num_row-1,i,atl, visited_atl)
        for i in range(num_row):
            dfs(i,num_col-1,atl, visited_atl)
        res = []
        for r in range(num_row):
            for c in range(num_col):
                if pac[r][c] and atl[r][c]:
                    res.append([r,c])
        return res