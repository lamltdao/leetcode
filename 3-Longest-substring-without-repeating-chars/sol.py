# C1
class Solution1:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {}
        ans = 0
        count = 0
        last = 0
        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]] = i
                count += 1
            else:
                count = i - d[s[i]]
                temp = d[s[i]]
                for j in range(last, d[s[i]]):
                    if s[j] in d:
                        del d[s[j]]
                d[s[i]] = i
                last = temp+1
            ans = max(ans, count)
        return ans
# C2: Sliding window
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        d = set()
        l = r = 0
        while r < len(s) and s[r] not in d:
            d.add(s[r])
            r += 1
        ans = r-l
        while r < len(s):
            d.remove(s[l])
            l += 1
            while r < len(s) and s[r] not in d:
                d.add(s[r])
                r += 1
            ans = max(ans, r-l)
        return ans