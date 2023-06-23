class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        char_freq = {}
        num_char_multiple_freq = 0
        l = 0
        ans = 0
        for r in range(len(s)):
            if s[r] not in char_freq:
                char_freq[s[r]] = 0
            char_freq[s[r]] += 1
            if char_freq[s[r]] > 1:
                num_char_multiple_freq += 1
            # move l until no repeated character
            while l < r and (num_char_multiple_freq > 0 or len(char_freq) > k):
                char_freq[s[l]] -= 1
                if char_freq[s[l]] == 1:
                    num_char_multiple_freq -= 1
                if char_freq[s[l]] == 0:
                    char_freq.pop(s[l])
                l += 1
            if r-l+1 == k:
                ans += 1
                
        return ans