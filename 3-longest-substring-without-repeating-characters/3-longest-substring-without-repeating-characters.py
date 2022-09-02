class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        temp_set = set()
        l = 0
        r = 0
        while r < len(s) and s[r] not in temp_set:
            temp_set.add(s[r])
            r += 1
        ans = r - l
        while r < len(s):
            temp_set.remove(s[l])
            l += 1
            while r < len(s) and s[r] not in temp_set:
                temp_set.add(s[r])
                r += 1
            ans = max(ans, r-l)
        return ans