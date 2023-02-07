class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        """
        find the longest subsequence with at most 2 types
        """
        ans = 0
        window = {}
        l = 0
        for r in range(len(fruits)):
            if fruits[r] not in window:
                window[fruits[r]] = 0
            window[fruits[r]] += 1
            while l < r and len(window) > 2:
                if fruits[l] in window:
                    window[fruits[l]] -= 1
                    if window[fruits[l]] == 0:
                        del window[fruits[l]]
                l += 1
            ans = max(ans, r-l+1)
        return ans