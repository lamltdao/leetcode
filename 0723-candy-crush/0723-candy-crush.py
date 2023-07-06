class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        nrow = len(board)
        ncol = len(board[0])
        while True:
            crush = [[False for _ in range(ncol)] for _ in range(nrow)]
            # check each row
            for r_idx, row in enumerate(board):
                num_conse = 0
                conse_val = None
                for c_idx in range(ncol):
                    # first cell or continue streak
                    if conse_val is None or (conse_val != 0 and board[r_idx][c_idx] == conse_val):
                        num_conse += 1
                    # move to a cell with different value
                    else:
                        # mark previous streak as true in crush 2d array
                        if conse_val != 0 and num_conse >= 3:
                            for crush_c_idx in range(c_idx-num_conse, c_idx):
                                crush[r_idx][crush_c_idx] = True
                        # reset
                        num_conse = 1
                    conse_val = board[r_idx][c_idx]
                # crushes may be at end of row
                if num_conse >= 3:
                    for crush_c_idx in range(ncol-num_conse, ncol):
                        crush[r_idx][crush_c_idx] = True
            # check each col
            for c_idx in range(ncol):
                num_conse = 0
                conse_val = None
                for r_idx in range(nrow):
                    # first cell or continue streak
                    if conse_val is None or (conse_val != 0 and board[r_idx][c_idx] == conse_val):
                        num_conse += 1
                    # move to a cell with different value
                    else:
                        # mark previous streak as true in crush 2d array
                        if conse_val != 0 and num_conse >= 3:
                            for crush_r_idx in range(r_idx-num_conse, r_idx):
                                crush[crush_r_idx][c_idx] = True
                        # reset
                        num_conse = 1
                    conse_val = board[r_idx][c_idx]
                # crushes may be at end of col
                if num_conse >= 3:
                    for crush_r_idx in range(nrow-num_conse, nrow):
                        crush[crush_r_idx][c_idx] = True
            # has at least 1 crush
            if any([any(row) for row in crush]):
                for c_idx in range(ncol):
                    # shift non-crush in each col
                    offset = 0
                    for r_idx in range(nrow-1, -1, -1):
                        if crush[r_idx][c_idx]:
                            offset += 1
                        else:
                            board[r_idx+offset][c_idx] = board[r_idx][c_idx]
                    # replace empty with 0
                    for r_idx in range(offset):
                        board[r_idx][c_idx] = 0
            else:
                break
            
        return board