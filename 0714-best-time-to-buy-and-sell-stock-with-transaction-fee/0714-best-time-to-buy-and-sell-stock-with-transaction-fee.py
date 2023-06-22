class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        """
        if buy - sell <= fee, not worth buying
        
        for each idx i, find next element > fee + prices[i]
        
        [1,3,5,7,11,3], fee = 3
        buy 1 sell 5, buy 7 sell 11 => 2
        
        buy 1 sell 11 => 8
        
        max_profit
        [0,0,1,3,8,8]
        
        each idx: either hold 1 stock or no stock
        if hold 1 stock, can sell 
        
        dp[i][0]: max profit without holding stock
        dp[i][1]: max profit holding stock
        each stock, either buy (if not hold), sell (if hold), or nothing
        dp[i][0] = max(dp[i][0]
            dp[i-1][0] # nothing
            dp[i-1][1] + prices[i] - fee  # sell. previously must hold stock
        )
        dp[i][1] = max(dp[i][1],
            dp[i-1][1], # nothing
            dp[i-1][0] - prices[i] # buy. previously must not hold
        )
        
        """
        dp = [[0,0] for _ in prices]
        dp[0][1] = -prices[0]
        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i-1][1] + prices[i] - fee, dp[i-1][0])
            dp[i][1] = max(dp[i-1][0] - prices[i], dp[i-1][1])
        return max(0, dp[-1][0])