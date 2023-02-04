class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window = {}
        for c in s1:
            if c not in window:
                window[c] = 0
            window[c] += 1
        tmp_window = {}
        for i in range(len(s2)):
            if i >= len(s1):
                removed_idx = i - len(s1)
                tmp_window[s2[removed_idx]] -= 1
                if tmp_window[s2[removed_idx]] == 0:
                    del tmp_window[s2[removed_idx]]
            if s2[i] not in tmp_window:
                tmp_window[s2[i]] = 0
            tmp_window[s2[i]] += 1
            if tmp_window == window:
                return True
        return False