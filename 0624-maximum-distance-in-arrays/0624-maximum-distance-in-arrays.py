class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        """
        For each array, only care about smallest & largest
        
        Create an array arr
        For each array at idx i, append (smallest_el, i) and (largest_el, i) to arr
        Sort arr
        The first and last values of arr should form a max distance if they belong to different arrays, otherwise get the max of (last - second) and (second last - first)
        
        Edge: (1,0) (2,1)  (4,1) (6,0)
        
        Time: O(n log n), n = 2m
        """
        val_idx_arr = []
        for i in range(len(arrays)):
            val_idx_arr.append([arrays[i][0], i])
            if len(arrays[i]) > 1:
                val_idx_arr.append([arrays[i][-1], i])
        # val_idx_arr.sort()
        # l = 0
        # r = len(val_idx_arr)-1
        # if val_idx_arr[l][1] != val_idx_arr[r][1]:
        #     return val_idx_arr[r][0] - val_idx_arr[l][0] 
        # else:
        #     return max(val_idx_arr[r][0] - val_idx_arr[l+1][0], val_idx_arr[r-1][0] - val_idx_arr[l][0])
        min_val, min_val_arr_idx = min(val_idx_arr)
        max_val, max_val_arr_idx = max(val_idx_arr)
        if min_val_arr_idx != max_val_arr_idx:
            return max_val - min_val
        second_min_val = None
        second_max_val = None
        for i in range(len(val_idx_arr)):
            idx = val_idx_arr[i][1]
            if idx != min_val_arr_idx and (second_min_val is None or second_min_val >= val_idx_arr[i][0]):
                second_min_val = val_idx_arr[i][0]
            if idx != max_val_arr_idx and (second_max_val is None or second_max_val <= val_idx_arr[i][0]):
                second_max_val = val_idx_arr[i][0]
        return max(max_val - second_min_val, second_max_val - min_val)
        