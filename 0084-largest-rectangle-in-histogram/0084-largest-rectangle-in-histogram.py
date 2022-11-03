class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        find subarray such that maximizes min(subarr) * len(subarr)
        
        dp_l[i]: indices of next smaller on the left
        dp_r[i]: ... on the right
        
        for each height:
            ans = max(height[i] * (dp_l[i] + dp_r[i]) )
        """
        n = len(heights)
        dp_l = [-1 for _ in range(n)]
        dp_r = [n for _ in range(n)]
        mono_stk = []
        for i in range(n):
            if len(mono_stk) == 0:
                mono_stk.append(i)
            else:
                while len(mono_stk) > 0 and heights[mono_stk[-1]] >= heights[i]:
                    mono_stk.pop()
                if len(mono_stk) > 0:
                    dp_l[i] = mono_stk[-1]
                mono_stk.append(i)
        mono_stk = []
        for i in range(n-1,-1,-1):
            if len(mono_stk) == 0:
                mono_stk.append(i)
            else:
                while len(mono_stk) > 0 and heights[mono_stk[-1]] >= heights[i]:
                    mono_stk.pop()
                if len(mono_stk) > 0:
                    dp_r[i] = mono_stk[-1]
                mono_stk.append(i)
        ans = 0
        for i in range(n):
            idx_l = dp_l[i]
            idx_r = dp_r[i]
            """
            idx: 1
            idx_l: -1
            idx_r: 6
            """
            ans = max(ans, heights[i] * (idx_r-i-1 + i-idx_l-1 + 1))
        return ans
            