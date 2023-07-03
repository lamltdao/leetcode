class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        diff_idx = []
        for i in range(len(s)):
            if s[i] != goal[i]:
                diff_idx.append(i)
        # no difference, and there exists a char with >= 2 occurences, can just swap 2 occurences of that char
        if len(diff_idx) == 0 and len(set(s)) < len(s):
            return True
        # differ in != 2 chars, can't swap just 2
        if len(diff_idx) != 2:
            return False
        # check if swap-able
        idx1 = diff_idx[0]
        idx2 = diff_idx[1]
        if s[idx1] == goal[idx2] and s[idx2] == goal[idx1]:
            return True
        return False