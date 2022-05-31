class Solution:
    def lastStoneWeightII(self, stones: list[int]) -> int:
        """
        Try to divide the list into 2 parts with minimum diff
        dp[i][j]: Up to ith stone, return the maximum sum of elements not exceeding j
        result: 
        val1 = dp[len(stones)-1][sums[len(stones)-1]//2]
        val2 = sums[len(stones)-1] - val1
        return abs(val1 - val2)
        
        """
        if len(stones) == 1:
            return stones[0]
        if len(stones) == 2:
            return abs(stones[0] - stones[-1])
        stones.insert(0, 0) #dummy value
        stones = [e*2 for e in stones]
        sums = [0 for _ in stones]
        for i in range(1, len(stones)):
            sums[i] += sums[i-1] + stones[i]
        dp = [[0 for _ in range(sums[-1]//2 + 1)] for _ in stones]
        for i in range(1,len(stones)):
            for j in range(sums[-1]//2 + 1):
                if stones[i] > j:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i-1][j-stones[i]] + stones[i])
        val1 = dp[len(stones)-1][sums[len(stones)-1]//2]
        val2 = sums[len(stones)-1] - val1
        return abs(val1 - val2)//2