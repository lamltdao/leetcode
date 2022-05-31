class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0 for _ in range(n+1)]
        for i in range(n+1):
            for k in range(1, i+1):
                dp[i] = max([dp[i], dp[i-k]*k, dp[k]*(i-k), (i-k)*k])
        return dp[n]