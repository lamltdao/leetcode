class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            # check if we can delete 1 char from s to get t
            if len(s) != len(t)+1:
                return False            
            num_diff = 0
            t_idx = 0
            while t_idx < len(t):
                if s[t_idx+num_diff] != t[t_idx]:
                    if num_diff == 0:
                        num_diff += 1
                    else:
                        return False
                else:
                    t_idx += 1
        elif len(s) < len(t):
            # check if we can add 1 char to s to get t
            if len(s)+1 != len(t):
                return False
            num_diff = 0
            s_idx = 0
            while s_idx < len(s):
                if t[s_idx+num_diff] != s[s_idx]:
                    if num_diff == 0:
                        num_diff += 1
                    else:
                        return False
                else:
                    s_idx += 1
        else:
            # check if we can replace 1 char in s to get t
            num_diff = 0
            for i in range(len(t)):
                if t[i] != s[i]:
                    num_diff += 1
            if num_diff != 1:
                return False
        return True
            