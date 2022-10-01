class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        """
        lcs
        
        dp[i][j]: longest common subarray of nums1[:i] and nums2[:j]
        i == 0 or j == 0 dp[i][j] = 0
        dp[i][j] = dp[i-1][j-1]+1 if nums1[i-1] == nums2[j-1]
                = max(dp[i][j-1], dp[i-1][j])
        """
        dp = [[0 for _ in range(len(nums2)+1)] for _ in range(len(nums1)+1)]
        ans = 0
        for i in range(1, len(nums1)+1):
            for j in range(1, len(nums2)+1):
                if nums1[i-1] == nums2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                ans = max(ans, dp[i][j])
        return ans