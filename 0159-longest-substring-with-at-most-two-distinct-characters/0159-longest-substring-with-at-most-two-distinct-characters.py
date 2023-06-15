class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        window = {}
        l = 0
        ans = 0
        for r in range(len(s)):
            if s[r] not in window:
                window[s[r]] = 0
            window[s[r]] += 1
            while l < r and len(window) > 2:
                if s[l] in window:
                    window[s[l]] -= 1
                    if window[s[l]] == 0:
                        del window[s[l]]
                l += 1
            ans = max(ans, r-l+1)
        return ans