class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        
        live with < 2 live neighbors => dead
        live with 2 or 3 live neighbors => live
        live with > 3 live neighbors => dead
        dead with =3 live neightbors => live
        
        live_neighbor[i][j]
        """
        nrow = len(board)
        ncol = len(board[0])
        live_neighbor = [[0 for _ in range(ncol)] for _ in range(nrow)]
        for r in range(nrow):
            for c in range(ncol):
                if board[r][c] == 1:
                    if r > 0 and c > 0:
                        live_neighbor[r-1][c-1] += 1
                    if r > 0:
                        live_neighbor[r-1][c] += 1
                    if r > 0 and c+1 < ncol:
                        live_neighbor[r-1][c+1] += 1
                    if c+1 < ncol:
                        live_neighbor[r][c+1] += 1
                    if r+1 < nrow and c+1 < ncol:
                        live_neighbor[r+1][c+1] += 1
                    if r+1 < nrow:
                        live_neighbor[r+1][c] += 1
                    if r+1 < nrow and c > 0:
                        live_neighbor[r+1][c-1] += 1
                    if c > 0:
                        live_neighbor[r][c-1] += 1
        for r in range(nrow):
            for c in range(ncol):
                if board[r][c] == 1:
                    if not (live_neighbor[r][c] == 2 or live_neighbor[r][c] == 3):
                        board[r][c] = 0
                elif live_neighbor[r][c] == 3:
                    board[r][c] = 1
        