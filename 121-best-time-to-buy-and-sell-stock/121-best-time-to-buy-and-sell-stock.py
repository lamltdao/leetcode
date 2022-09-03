class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        c1: dp[i]: highest price on the right of i O(2n)
        c2: sliding window O(n) 
        """
        # Style 1
        # l = 0
        # r = 1
        # ans = 0
        # while r < len(prices):
        #     if prices[l] < prices[r]:
        #         ans = max(ans, prices[r] - prices[l])
        #     else:
        #         l = r
        #     r += 1
        # return ans
        
        # Style 2
        l = 0
        ans = 0
        for r in range(len(prices)):
            if prices[l] < prices[r]:
                ans = max(ans, prices[r] - prices[l])
            else:
                l = r
        return ans
        