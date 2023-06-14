class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        """
        For each array, only care about smallest & largest
        
        Create an array arr
        For each array at idx i, append (smallest_el, i) and (largest_el, i) to arr
        Sort arr
        The first and last values of arr should form a max distance if they belong to different arrays, otherwise get the max of (last - second) and (second last - first)
        
        Edge: (1,0) (2,1)  (4,1) (6,0)
        """
        val_idx_arr = []
        for i in range(len(arrays)):
            val_idx_arr.append([arrays[i][0], i])
            if len(arrays[i]) > 1:
                val_idx_arr.append([arrays[i][-1], i])
        val_idx_arr.sort()
        l = 0
        r = len(val_idx_arr)-1
        if val_idx_arr[l][1] != val_idx_arr[r][1]:
            return val_idx_arr[r][0] - val_idx_arr[l][0] 
        else:
            return max(val_idx_arr[r][0] - val_idx_arr[l+1][0], val_idx_arr[r-1][0] - val_idx_arr[l][0])
        