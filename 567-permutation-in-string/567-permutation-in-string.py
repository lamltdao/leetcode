class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_freq = {}
        for c in s1:
            if c not in s1_freq:
                s1_freq[c] = 0
            s1_freq[c] += 1
        l = 0
        r = 0
        temp_s2_freq = {}
        for c in s1_freq.keys():
            temp_s2_freq[c] = s1_freq[c]
        while r < len(s2) and r < len(s1):
            if s2[r] in temp_s2_freq:
                temp_s2_freq[s2[r]] -= 1
            r += 1
            
        while l < len(s2):
            if not any(temp_s2_freq.values()):
                return True
            if s2[l] in s1_freq:
                temp_s2_freq[s2[l]] = 1 if s2[l] not in temp_s2_freq else temp_s2_freq[s2[l]] + 1
            l += 1
            while r < len(s2) and r < l+len(s1):
                if s2[r] in temp_s2_freq:
                    temp_s2_freq[s2[r]] -= 1
                r += 1
        return False