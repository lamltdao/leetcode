import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        k = max => len(piles) hour
        
        1 <= k<= max(piles)
        
        l < r:
            m = (l+r) // 2
        
        Time: n log m, Space: O(1), m = max(piles)
        
        idea: try possible val of k in range [1, max(piles)]
        if k is valid (num_hour <= h), try a smaller val
        else:
            try bigger
        """
        l = 1
        r = max(piles)
        def get_hour_finish(k):
            return sum([math.ceil(p / k) for p in piles])
        while l <= r:
            m = (l+r) // 2
            hour_finish = get_hour_finish(m)
            if hour_finish <= h:
                r = m-1
            else:
                l = m+1
        return l