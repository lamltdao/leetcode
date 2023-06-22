class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if k == 0:
            return 0
        window = {}
        l = 0
        ans = 0
        for r in range(len(s)):
            if s[r] not in window:
                window[s[r]] = 0
            window[s[r]] += 1
            while l < r and len(window) > k:
                window[s[l]] -= 1
                if window[s[l]] == 0:
                    window.pop(s[l])
                l += 1
            ans = max(ans, r-l+1)
        return ans