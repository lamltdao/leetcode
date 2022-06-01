class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1)+len(s2) != len(s3):
            return False
        """
        dp[i][j] = true if interleaving of s1[:i] and s2[:j] forms s3[:i+j]
        base: dp[i][0] = true if s1[i] == s3[i]
        if s3[i+j] == s1[i]:
            dp[i][j] = dp[i][j] or dp[i-1][j]
        if s3[i+j] == s2[j]:
            dp[i][j] = dp[i][j] or dp[i][j-1]
        """
        if len(s3) == 0:
            return len(s1) == 0 and len(s2) == 0
        if len(s1) == 0:
            return s2 == s3
        if len(s2) == 0:
            return s1 == s3
        dp = [[False for _ in range(len(s2)+1)] for _ in range(len(s1)+1)]
        dp[0][0] = True
        for i in range(1,len(s1)+1):
            if s1[i-1] == s3[i-1] and dp[i-1][0]: # NOTE: need both conditions
                dp[i][0] = True
        for j in range(1,len(s2)+1):
            if s2[j-1] == s3[j-1] and dp[0][j-1]: # NOTE: need both conditions
                dp[0][j] = True
        for i in range(1, len(s1)+1):
            for j in range(1, len(s2)+1):
                if s3[i+j-1] == s1[i-1]:
                    dp[i][j] = dp[i][j] or dp[i-1][j]
                if s3[i+j-1] == s2[j-1]: # use if, not elif here
                    dp[i][j] = dp[i][j] or dp[i][j-1]
        return dp[len(s1)][len(s2)]
