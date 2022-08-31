binary search the ANSWER, which is in the range [1, 10^6].
while l < r:
m = (l+r) // 2
if m is greater than more than half of matrix then
r = m (narrow search range to the left)
else:
l = m+1 # narrow search range to the right.
return r