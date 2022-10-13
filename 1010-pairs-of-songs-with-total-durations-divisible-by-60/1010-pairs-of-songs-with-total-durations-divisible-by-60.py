class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        # Time: O(n), n = len(time)
        # Space: O(n)
        d = {}
        for t in time:
            r = t % 60
            if r not in d:
                d[r] = 0
            d[r] += 1
        ans = 0
        for k in d.keys():
            if k == 0 or k == 30:
                ans += d[k] * (d[k]-1) // 2
            elif 60-k in d and k < 60-k:
                ans += d[k] * d[60-k]
        return ans
