class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        """
        for each cell in the first row
            check each cell in the diagonal starting from that cell
        for each cell in the first col excluding the top left
            check same thing
        Time: O(mn), as each cell is visited once
        Space: O(1)
        """
        nrow = len(matrix)
        ncol = len(matrix[0])
        for c in range(ncol):
            val = matrix[0][c]
            tmp_r = 1
            tmp_c = c+1
            while tmp_r < nrow and tmp_c < ncol:
                if matrix[tmp_r][tmp_c] != val:
                    return False
                tmp_r += 1
                tmp_c += 1
        for r in range(1, nrow):
            val = matrix[r][0]
            tmp_r = r+1
            tmp_c = 1
            while tmp_r < nrow and tmp_c < ncol:
                if matrix[tmp_r][tmp_c] != val:
                    return False
                tmp_r += 1
                tmp_c += 1
        return True