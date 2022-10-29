class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for _ in range(len(text2)+1)] for _ in range(len(text1)+1)]
        for i1 in range(1,len(text1)+1):
            for i2 in range(1,len(text2)+1):
                if text1[i1-1] == text2[i2-1]:
                    dp[i1][i2] = 1 + dp[i1-1][i2-1]
                else:
                    dp[i1][i2] = max(dp[i1-1][i2], dp[i1][i2-1])
        return dp[len(text1)][len(text2)]