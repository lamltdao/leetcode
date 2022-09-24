class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        """
        sum(r1,c1,r2,c2) = prefix(r2,c2) - prefix(r1-1 c2) - prefix (r2, c1-1) + prefix(r1-1, c1-1)
        """
        nrow = len(matrix)
        ncol = len(matrix[0])
        self.prefix = [[0 for _ in range(ncol+1)] for _ in range(nrow+1)]
        self.prefix[1][1] = matrix[0][0]
        for r in range(2, nrow+1):
            self.prefix[r][1] = self.prefix[r-1][1] + matrix[r-1][0]
        for c in range(2, ncol+1):
            self.prefix[1][c] = self.prefix[1][c-1] + matrix[0][c-1]
        for r in range(2, nrow+1):
            for c in range(2, ncol+1):
                self.prefix[r][c] = matrix[r-1][c-1] + self.prefix[r-1][c] + self.prefix[r][c-1] - self.prefix[r-1][c-1]
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.prefix[row2+1][col2+1] - self.prefix[row1][col2+1] - self.prefix[row2+1][col1] + self.prefix[row1][col1]
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)