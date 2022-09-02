class Solution:
    # return a num 0->8 indicating the region the number lies in the sudoku
    def get_grid(self,row, col) -> int:
        row_weight = 0
        col_weight = 0

        if row <= 2:
            row_weight = 0
        elif row <= 5:
            row_weight = 1
        else:
            row_weight = 2
            
        if col <= 2:
            col_weight = 0
        elif col <= 5:
            col_weight = 1
        else:
            col_weight = 2

        return 3 * row_weight + col_weight
    
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Time: O(row * col)
        cols = [set([]) for i in range(9)]
        rows = [set([]) for i in range(9)]
        grids = [set([]) for i in range(9)]
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] != ".":
                    # bc arr is 0-based index
                    num = int(board[row][col])
                    grid = self.get_grid(row, col)
                    num_idx = num - 1
                    # check for invalidation
                    if col in cols[num_idx] or row in rows[num_idx] or grid in grids[num_idx]:
                        return False
                    cols[num_idx].add(col)
                    rows[num_idx].add(row)
                    grids[num_idx].add(grid)
        return True