class Solution:
    def findBlackPixel(self, picture: List[List[str]], target: int) -> int:
        nrow = len(picture)
        ncol = len(picture[0])
        num_black_rows = [0 for _ in range(nrow)]
        num_black_cols = [0 for _ in range(ncol)]
        for r in range(nrow):
            for c in range(ncol):
                if picture[r][c] == 'B':
                    num_black_rows[r] += 1
                    num_black_cols[c] +=1
        ans = 0
        for c_idx, c in enumerate(num_black_cols):
            if c != target:
                continue
            row_same = True
            cur_row = None
            for r_idx, r in enumerate(num_black_rows):
                if picture[r_idx][c_idx] != 'B':
                    continue
                if r != target:
                    row_same = False
                    break
                if cur_row is None:
                    cur_row = picture[r_idx]
                elif cur_row != picture[r_idx]:
                    row_same = False
                    break
            if row_same and cur_row is not None: # all rows the same + at least 1 row has black pixel
                ans += target
        return ans
                    
            