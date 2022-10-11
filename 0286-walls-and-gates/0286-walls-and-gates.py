from collections import deque

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        INF = 2147483647
        nrow = len(rooms)
        ncol = len(rooms[0])
        def bfs(r,c):
            nonlocal nrow, ncol
            q = deque()
            q.append((r,c,0))
            while len(q) > 0:
                row,col,d = q.popleft()
                if row > 0 and rooms[row-1][col] > 0 and d+1 < rooms[row-1][col]:
                    rooms[row-1][col] = d+1
                    q.append((row-1, col, d+1))
                if row+1 < nrow and rooms[row+1][col] > 0 and d+1 < rooms[row+1][col]:
                    rooms[row+1][col] = d+1
                    q.append((row+1, col, d+1))
                if col > 0 and rooms[row][col-1] > 0 and d+1 < rooms[row][col-1]:
                    rooms[row][col-1] = d+1
                    q.append((row, col-1, d+1))
                if col+1 < ncol and rooms[row][col+1] > 0 and d+1 < rooms[row][col+1]:
                    rooms[row][col+1] = d+1
                    q.append((row, col+1, d+1))
        for r in range(nrow):
            for c in range(ncol):
                if rooms[r][c] == 0:
                    bfs(r,c)
        return rooms