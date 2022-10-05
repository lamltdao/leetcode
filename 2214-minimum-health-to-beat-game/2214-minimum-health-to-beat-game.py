class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:
        """
        minimize health
        -2-7-3 = -13
        -2-3-4-3 = -12
        13
        dp[0] = [0,0]
        dp[i][0]: num_health with amor not used yet
        dp[i][1]: with amor used already
        dp[i][0] = dp[i-1][0] - max(damage[i]-armor, 0)
        dp[i][1] = dp[i-1][1] - damage[i]
        
        """
        # dp = [[0,0] for _ in range(len(damage)+1)]
        # for i in range(len(damage)):
        #     dp[i+1][1] = dp[i][0] - max(damage[i]-armor, 0)
        #     dp[i+1][0] = dp[i][0] - damage[i]
        # return max(-dp[i][0], -dp[i][1])+1
        m = max(damage)
        return sum(damage) - m + max(m - armor, 0) + 1