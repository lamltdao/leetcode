class Solution:
    def trap(self, height: List[int]) -> int:
        """
        height of water at col i = min(highest cell on its left, highest cell on its right) - height[i] if diff > 0 else 0
        """
        dp_l = [0 for _ in height]
        dp_r = [0 for _ in height]
        cur_highest_l = height[0]
        dp_l[0] = cur_highest_l
        for i in range(1, len(height)):
            dp_l[i] = max(dp_l[i-1], height[i])
        
        cur_highest_r = height[-1]
        dp_r[-1] = cur_highest_r
        for i in range(len(height)-2, -1, -1):
            dp_r[i] = max(dp_r[i+1], height[i])
        ans = 0
        for i in range(len(height)):
            ans += max(0, min(dp_l[i], dp_r[i]) - height[i])
        return ans
        