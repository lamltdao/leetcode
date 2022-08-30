class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        """
        n = 3
        0,0 => 0,2 =>2,2 =>
        i,j => j, n-i-1 => n-i-1, n-j-1 => n-j-1, i
        n-1-j ,i => i,j
        if n is odd:
        1  2  3  4  5
        6  7  8  9  10
        11 12 13 14 15
        16 17 18 19 20
        21 22 23 24 25
        """
        n = len(matrix)
        if n == 1:
            return
        if n % 2 == 1:
            start_idx = 3
        else:
            start_idx = 2
        mid = n // 2
        for i in range(start_idx, n+1, 2):
            mid -= 1
            for j in range(i-1):
                temp = matrix[mid][mid+j]
                matrix[mid][mid+j] = matrix[n-1-mid-j][mid]
                matrix[n-1-mid-j][mid] = matrix[n-mid-1][n-mid-j-1]
                matrix[n-mid-1][n-mid-j-1] = matrix[mid+j][n-mid-1]
                matrix[mid+j][n-mid-1] = temp       
                    
                    