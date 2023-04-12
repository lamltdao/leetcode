class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        """
        dp[amount+1][len(coins)+1]: 
        dp[i][j]: number of comb to represent amount i using first j coins
        dp[0][j] = 1
        dp[i][0] = 1
        dp[i][j] = sum {dp[i-coins[j]*k][j-1]} (use multiples of jth coin) + dp[i][j-1] (dont use jth coin)
        """
        dp = [[0 for _ in range(len(coins)+1)] for _ in range(amount+1)]
        # for i in range(amount+1):
        #     dp[i][0] = 1
        for j in range(len(coins)+1):
            dp[0][j] = 1
        dp[0][0] = 1
        for am in range(1, amount+1):
            for num_coin in range(1, len(coins)+1):
                dp[am][num_coin] += dp[am][num_coin-1]
                if am >= coins[num_coin-1]:
                    for mul in range(1, am//coins[num_coin-1]+1):
                        dp[am][num_coin] += dp[am-mul*coins[num_coin-1]][num_coin-1]
        return dp[amount][len(coins)]