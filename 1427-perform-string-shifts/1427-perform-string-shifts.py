class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        for di, am in shift:
            am = am % len(s)
            if di:
                s = s[len(s)-am:] + s[:len(s)-am]
            else:
                s = s[am:] + s[:am]
        return s