class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        """
        record {diff: [(num1, num2)]} where idx1 < idx2
        sort => find longest
        
        n^2 + n log n + n
        
        4,7,6,8,8,9,10
        
        -2: [4,6], [6,8], [6,8], [8,10], [8,10]
        dp[i][j]: longest subsequence ending at i whose diff is j
        j <= 500
        dp[i][j] = dp[k][j] + 1 where diff[i] - diff[k] == j
        base: dp[0][j] = 1
        => 1000*500
        """
        ans = 0
        dp = [{} for _ in nums]
        for i in range(len(nums)):
            for j in range(i):
                diff = nums[i] - nums[j]
                if diff not in dp[i]:
                    dp[i][diff] = 2
                if diff in dp[j]:
                    dp[i][diff] = max(dp[i][diff], dp[j][diff] + 1)
                ans = max(ans, dp[i][diff])
        return ans
        