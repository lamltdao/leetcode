class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [[0,0] for _ in nums]
        dp[0][0] = nums[0]
        for i in range(1,len(nums)):
            dp[i][0] = nums[i] + max(dp[i-2])
            dp[i][1] = max(dp[i-1])
        return max(dp[-1])