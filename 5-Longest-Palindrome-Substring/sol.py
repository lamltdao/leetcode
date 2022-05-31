class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = [[0 for _ in s] for _ in s]
        l = 0
        r = 0
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                l = i
                r = i+1
                dp[i][i+1] = 1
            dp[i][i] = 1
        dp[len(s)-1][len(s)-1] = 1
        for stride in range(2, len(s)):
            for i in range(len(s)-stride):
                j = i + stride
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1]
                    if dp[i+1][j-1] == 1 and j-i > r - l:
                        l = i
                        r = j
                else:
                    dp[i][j] = 0
        return s[l:r+1]