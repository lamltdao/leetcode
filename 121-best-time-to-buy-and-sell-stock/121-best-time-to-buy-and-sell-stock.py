class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        c1: dp[i]: highest price on the right of i O(n) with 2 loops
        c2: sliding window
        
        4 5 3 6 8 4 2
        """
        if len(prices) == 1:
            return 0
        l = 0
        r = 1
        ans = 0
        while r < len(prices):
            while r < len(prices) and prices[l] <= prices[r]:
                ans = max(ans, prices[r] - prices[l])
                r += 1
            l = r
            r = l+1
        return ans
        