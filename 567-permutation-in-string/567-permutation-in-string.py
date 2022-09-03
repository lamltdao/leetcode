class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window_freq = {}
        for c in s1:
            if c not in window_freq:
                window_freq[c] = 0
            window_freq[c] += 1
        l = 0
        for r in range(len(s2)):
            while l < r+1-len(s1):
                if s2[l] in window_freq:
                    window_freq[s2[l]] += 1
                l += 1
            if s2[r] in window_freq:
                window_freq[s2[r]] -= 1
            if not any(window_freq.values()):
                return True
        return False