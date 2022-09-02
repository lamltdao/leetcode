class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        all replacements must be the same char
        
        window:
        - there are <= k chars that are not the most frequent
        """
        l = r = 0
        freqs = [0 for _ in range(26)]
        while r < len(s):
            # check whether r can be in the window
            freqs[ord(s[r]) - ord('A')] += 1
            num_most_freq = max(freqs)
            if r-l+1-num_most_freq <= k:
                r += 1
            else:
                freqs[ord(s[r]) - ord('A')] -= 1
                break
        ans = r-l
        while l < len(s):
            freqs[ord(s[l]) - ord('A')] -= 1
            l += 1
            while r < len(s):
                freqs[ord(s[r]) - ord('A')] += 1
                num_most_freq = max(freqs)
                if r-l+1-num_most_freq <= k:
                    r += 1
                else:
                    freqs[ord(s[r]) - ord('A')] -= 1
                    break
            ans = max(ans, r-l)
        return ans
                
        