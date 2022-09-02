class Solution:
    def isPalindrome(self, s: str) -> bool:
        def get_next_l(start_idx):
            cur_idx = start_idx
            while cur_idx < len(s) and not s[cur_idx].isalnum():
                cur_idx += 1
            return cur_idx
        def get_next_r(start_idx):
            cur_idx = start_idx
            while cur_idx >= 0 and not s[cur_idx].isalnum():
                cur_idx -= 1
            return cur_idx
        l,r = -1, len(s)
        while l < r:
            l = get_next_l(l+1)
            r = get_next_r(r-1)
            if l <= r and s[l].lower() != s[r].lower():
                return False
        return True