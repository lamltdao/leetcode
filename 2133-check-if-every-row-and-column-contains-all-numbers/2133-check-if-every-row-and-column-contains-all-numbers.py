class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        row_filled = [set() for _ in range(n)]
        col_filled = [set() for _ in range(n)]
        for r in range(n):
            for c in range(n):
                val = matrix[r][c]
                row_filled[r].add(val)
                col_filled[c].add(val)
        for i in range(n):
            if len(row_filled[i]) < n:
                return False
            if len(col_filled[i]) < n:
                return False
        return True