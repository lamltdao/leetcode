class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        c1: dp[i]: highest price on the right of i O(2n)
        c2: sliding window O(n) 
        """
        l = 0
        r = 1
        ans = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                ans = max(ans, prices[r] - prices[l])
                r += 1
            else:
                l = r
                r = l+1
        return ans
        