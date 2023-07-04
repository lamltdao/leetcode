class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        nrow = len(picture)
        ncol = len(picture[0])
        num_black_rows = [0 for _ in range(nrow)]
        num_black_cols = [0 for _ in range(ncol)]
        """
        500*500*1000 = 10^7 * 25
        
        500*500 + 500 * 500
        """
        ans = 0
        for r in range(nrow):
            for c in range(ncol):
                if picture[r][c] == 'B':
                    num_black_rows[r] += 1
                    num_black_cols[c] += 1
        for i1,r in enumerate(num_black_rows):
            if r != 1:
                continue
            for i2, c in enumerate(num_black_cols):
                if c != 1:
                    continue
                if picture[i1][i2] == 'B':
                    ans += 1
        return ans