class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        """
        dp[r][c]: lip from (r,c)
        """
        nrow = len(matrix)
        ncol = len(matrix[0])
        dp = [[0 for _ in range(ncol)] for _ in range(nrow)]
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        def dfs(r,c):
            nonlocal nrow, ncol
            if dp[r][c] != 0:
                return dp[r][c]
            for d in dirs:
                nr = r + d[0]
                nc = c + d[1]
                if 0 <= nr < nrow and 0 <= nc < ncol and matrix[nr][nc] > matrix[r][c]:
                    dp[r][c] = max(dp[r][c], dfs(nr,nc))
            dp[r][c] += 1
            return dp[r][c]
        ans = 1
        for r in range(nrow):
            for c in range(ncol):
                ans = max(ans, dfs(r,c))
        return ans