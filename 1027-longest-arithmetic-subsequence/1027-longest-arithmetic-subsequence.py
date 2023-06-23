class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        """
        dp[i][d]: longest subsequence ending at i whose diff between 2 consecutive elements in the subsequence is d
        initialize dp = {} * len(nums)
        dp[i][d] = max(dp[i][d], dp[j][d] + 1) where nums[i] - nums[j] == d
        Time: O(n^2), n = len(nums)
        Space: O(n*500), as there're at most 500 values for difference of 2 numbers
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
        