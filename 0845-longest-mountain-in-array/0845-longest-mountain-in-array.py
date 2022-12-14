class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        """
        less[i]: num increasing elements < i on the left
        greater[i]: num decreasing elements < i on the right
        """
        less_l = [0 for _ in arr]
        less_r = [0 for _ in arr]
        
        tmp_cnt = 0
        for i in range(1, len(arr)):
            if arr[i-1] < arr[i]:
                tmp_cnt += 1
            else:
                tmp_cnt = 0
            less_l[i] = tmp_cnt
        tmp_cnt = 0
        for i in range(len(arr)-2,-1,-1):
            if arr[i+1] < arr[i]:
                tmp_cnt += 1
            else:
                tmp_cnt = 0
            less_r[i] = tmp_cnt
        print(less_l, less_r)
        ans = 0
        for i in range(len(arr)):
            if less_l[i] > 0 and less_r[i] > 0:
                ans = max(ans, less_l[i] + less_r[i] + 1)
        return ans
        
            