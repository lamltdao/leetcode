class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        # (m by k) * (k by n) = m by n
        m = len(mat1)
        k = len(mat1[0])
        n = len(mat2[0])
        result = [[0 for _ in range(n)] for _ in range(m)]
        for r in range(m):
            for c in range(n):
                for i in range(k):
                    result[r][c] += mat1[r][i] * mat2[i][c]
        return result