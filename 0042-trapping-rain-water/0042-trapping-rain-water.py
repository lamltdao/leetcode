class Solution:
    def trap(self, height: List[int]) -> int:
        """
        water at idx i = min(max_height on left, max_height on right) * (dist between left and right max heights)
        """
        n = len(height)
        max_heights_l = [0 for _ in range(n)] # idx of max height on left
        max_heights_r = [0 for _ in range(n)] # idx of max height on right
        max_heights_l[0] = 0
        tmp_heighest_idx = 0
        for i in range(1,n):
            if height[i] > height[tmp_heighest_idx]:
                tmp_heighest_idx = i
            max_heights_l[i] = tmp_heighest_idx
        max_heights_r[-1] = n-1
        tmp_heighest_idx = n-1
        for i in range(n-1,-1,-1):
            if height[i] > height[tmp_heighest_idx]:
                tmp_heighest_idx = i
            max_heights_r[i] = tmp_heighest_idx
        ans = 0
        for i in range(n):
            ans += max( min(height[max_heights_l[i]], height[max_heights_r[i]]) - height[i], 0 )
        return ans