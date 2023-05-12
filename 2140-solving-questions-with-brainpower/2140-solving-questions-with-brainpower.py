from heapq import heapify, heappush, heappop
class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        """
            dp[i][j]: max point up to question i
                j = 0: solve question i
                j = 1: skip question i
                
            max_dp
            max_dp_1
            arr = [k | k+brainpower[k] < i] -> pq
            dp[i][1] = max(dp[i+1])
            dp[i][0] = max(dp[i+brainpower[i]+1])
            dp[-1][0] = questions[-1]
        """
        dp = [[0 for _ in range(2)] for _ in questions]
        dp[-1][0] = questions[-1][0]
        for i in range(len(questions)-2, -1, -1):
            dp[i][1] = max(dp[i+1])
            if i+questions[i][1]+1 < len(questions):
                dp[i][0] = max(dp[i+questions[i][1]+1])
            dp[i][0] += questions[i][0]
        return max(dp[0])
        