class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        l, r: area = min_height * (r-l)
        cur_max
        if area > cur_max:
            cur_max = area
            
        """
        l,r = 0, len(height)-1
        cur_max = 0
        while l < r:
            area = (r-l) * min(height[l], height[r])
            cur_max = max(cur_max, area)
            if height[l] < height[r]:
                l += 1
            elif height[l] > height[r]:
                r -= 1
            else:
                l += 1
                r -= 1
        return cur_max