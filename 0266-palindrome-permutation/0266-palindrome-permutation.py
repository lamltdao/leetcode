class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        """
        palin if all chars has even occurences, only 1 chars has odd occurences
        """
        d = {}
        for c in s:
            if c not in d:
                d[c] = 0
            d[c] += 1
        num_odd_occ = 0
        for occ in d.values():
            if occ & 1:
                num_odd_occ += 1
        return num_odd_occ <= 1