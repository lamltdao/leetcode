class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        nrow = len(mat)
        ncol = len(mat[0])
        def helper(start_r, start_c):
            tmp_r = start_r
            tmp_c = start_c
            tmp_arr = []
            while tmp_r < nrow and tmp_c < ncol:
                tmp_arr.append(mat[tmp_r][tmp_c])
                tmp_r += 1
                tmp_c += 1
            tmp_arr.sort()
            # update elements in sorted tmp_arr to mat
            tmp_r = start_r
            tmp_c = start_c
            tmp_idx = 0
            while tmp_idx < len(tmp_arr):
                mat[tmp_r][tmp_c] = tmp_arr[tmp_idx]
                tmp_r += 1
                tmp_c += 1
                tmp_idx += 1
        # loop from nrow-1 -> 0
        for r in range(nrow-1, -1, -1):
            helper(r,0)
        for c in range(1, ncol):
            helper(0,c)
        return mat
        