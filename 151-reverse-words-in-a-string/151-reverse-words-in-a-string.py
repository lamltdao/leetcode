class Solution:
    def reverseWords(self, s: str) -> str:
        s = list(s)
        s.reverse()
        # remove leading spacces or trailing spaces
        space_idx_l = 0
        while s[space_idx_l] == ' ':
            space_idx_l += 1
        s = s[space_idx_l:]
        space_idx_r = len(s)-1
        while s[space_idx_r] == ' ':
            space_idx_r -= 1
        s = s[:space_idx_r+1]
        # reverse each word in s
        i = 0
        ans = ''
        while i < len(s) and s[i] != ' ':
            j = i+1
            while j < len(s) and s[j] != ' ':
                j += 1
            ans += ''.join(s[i:j][::-1])
            i = j
            while i < len(s) and s[i] == ' ':
                i += 1
            if i < len(s):
                ans += ' '
        return ans
        