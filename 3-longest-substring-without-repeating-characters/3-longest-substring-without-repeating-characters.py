class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        temp_set = set()
        # Style 1
        # l = 0
        # r = 0
        # # increment r as long as the window [l,r) is still valid
        # def inc_r():
        #     nonlocal r, temp_set, s
        #     while r < len(s) and s[r] not in temp_set:
        #         temp_set.add(s[r])
        #         r += 1
        # inc_r()
        # ans = r - l
        # while r < len(s):
        #     temp_set.remove(s[l])
        #     l += 1
        #     inc_r()
        #     ans = max(ans, r-l)
        # return ans
        
        # Style 2
        l = 0
        ans = 0
        for r in range(len(s)):
            # extend l until the window [l,r] has no repeating char
            while s[r] in temp_set:
                temp_set.remove(s[l])
                l += 1
            temp_set.add(s[r])
            ans = max(ans, r-l+1)
        return ans