To loop through every diagonal, create a helper function
def helper(start_r, start_c):
r = start_r, c = start_c
while r < nrow and c < ncol:
do sth with matrix[r][c]
r++
c++
-------
In this problem, in the while-loop body of helper, we create a tmp array to store all elements in the diagonal, then sort it, then update diagonal of original matrix with sorted array. We start helper(bottom leftmost) up to helper(0,0) then proceed to helper(0,c) for 1 <= c < ncol.