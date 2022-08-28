- C1: Loop from right, check for a redundant element at idx i by checking if nums[i] == nums[i-1] == nums[i-2]. If it is, shift all elements after it to the left, then append it to the end. Complexity: O(n^2)
- C2: First loop: Change all redundant element to NMAX. 
 Second Loop: Loop through array. If nums[i] == NMAX, keep traversing until we find a number other than NMAX, swap it with nums[i]. Otherwise, break the loop, since there's no more number other than NMAX. COmplexity: O(n), since variable junk keeps increasing