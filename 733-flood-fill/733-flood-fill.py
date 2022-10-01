class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        """
        Select the flood region using dfs
        color
        """
        if image[sr][sc] == color:
            return image
        nrow = len(image)
        ncol = len(image[0])
        visited = [[False for _ in range(ncol)] for _ in range(nrow)]
        tmp_color = image[sr][sc]
        def dfs(r,c):
            nonlocal tmp_color, nrow, ncol
            visited[r][c] = True
            if r > 0 and not visited[r-1][c] and image[r-1][c] == tmp_color:
                dfs(r-1,c)
            if r+1 < nrow and not visited[r+1][c] and image[r+1][c] == tmp_color:
                dfs(r+1,c)
            if c > 0 and not visited[r][c-1] and image[r][c-1] == tmp_color:
                dfs(r,c-1)
            if c+1 < ncol and not visited[r][c+1] and image[r][c+1] == tmp_color:
                dfs(r,c+1)
            image[r][c] = color
        dfs(sr,sc)
        return image
            