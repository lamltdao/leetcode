class Solution:
    def minimumKeypresses(self, s: str) -> int:
        """
        store {char: occurences}
        start from min occurences, press 1
        ...
        """
        d = {}
        for c in s:
            if c not in d:
                d[c] = 0
            d[c] += 1
        arr = [(-v, k) for k,v in d.items()]
        arr.sort()
        ans = 0
        cnt = 0
        mult = 1
        for neg_num_occur, char in arr:
            if cnt < 9:
                cnt += 1
            else:
                cnt = 1
                mult += 1
            ans += mult * (-neg_num_occur)
        return ans