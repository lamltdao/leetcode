class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        diff_idx = []
        for i in range(len(s)):
            if s[i] != goal[i]:
                diff_idx.append(i)
        if len(diff_idx) == 0 and len(set(s)) < len(s):
            return True
        if len(diff_idx) != 2:
            return False
        idx1 = diff_idx[0]
        idx2 = diff_idx[1]
        if s[idx1] == goal[idx2] and s[idx2] == goal[idx1]:
            return True
        return False