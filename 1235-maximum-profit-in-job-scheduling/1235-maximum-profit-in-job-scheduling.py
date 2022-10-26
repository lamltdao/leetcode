import bisect
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        """
        sort by start time
        dp[i]: max profit from i to end
        for each idx i, use binary search to find idx j such that i j dont intersect and j rightmost
        """
        n = len(startTime)
        intervals = [(startTime[i], endTime[i], profit[i]) for i in range(n)]
        intervals.sort()
        dp = [0 for _ in range(n+1)]
        starts = [intervals[i][0] for i in range(n)]
        for i in range(n-1, -1, -1):
            tmp = bisect.bisect_left(starts, intervals[i][1])
            dp[i] = max(dp[tmp] + intervals[i][2], dp[i+1])
        return dp[0]