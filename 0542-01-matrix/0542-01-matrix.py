from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        """
        if encounter 1, set dist = 1, bfs
        
        
        """
        m = len(mat)
        n = len(mat[0])
        INF = 1000000
        ans = [[INF for _ in range(n)] for _ in range(m)]
        visited = [[0 for _ in range(n)] for _ in range(m)]
        for r in range(m):
            for c in range(n):
                if mat[r][c] == 0:
                    ans[r][c] = 0
                    if r > 0 and mat[r-1][c] == 1:
                        ans[r-1][c] = 1
                    if r+1 < m and mat[r+1][c] == 1:
                        ans[r+1][c] = 1
                    if c > 0 and mat[r][c-1] == 1:
                        ans[r][c-1] = 1
                    if c+1 < n and mat[r][c+1] == 1:
                        ans[r][c+1] = 1
        def bfs(r,c):
            nonlocal m,n
            q = deque()
            q.append((r,c,1))
            while len(q) > 0:
                r,c,d = q.popleft()
                if r > 0 and mat[r-1][c] == 1 and ans[r-1][c] > d+1:
                    ans[r-1][c] = d+1
                    q.append((r-1,c,d+1))
                if r+1 < m and mat[r+1][c] == 1 and ans[r+1][c] > d+1:
                    ans[r+1][c] = d+1
                    q.append((r+1,c,d+1))
                if c > 0 and mat[r][c-1] == 1 and ans[r][c-1] > d+1:
                    ans[r][c-1] = d+1
                    q.append((r,c-1,d+1))
                if c+1 < n and mat[r][c+1] == 1 and ans[r][c+1] > d+1:
                    ans[r][c+1] = d+1
                    q.append((r,c+1,d+1))
        for r in range(m):
            for c in range(n):
                if mat[r][c] == 1 and ans[r][c] == 1:
                    bfs(r,c)
        return ans