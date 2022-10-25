class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        """
        for each worker idx i:
            choose job with most profitable and whose difficulty <= worker[i]
            
        arr = (diff, profit).sort()
        
        dp[i]: max profit of worker = i
        diff[0->arr[0][0]-1] = 0
        
        """
        total = 0
        n = len(difficulty)
        m = len(worker)
        arr = [(difficulty[i], profit[i]) for i in range(n)]
        arr.sort()
        dp = [0 for _ in range(1+arr[-1][0])]
        cur_idx = 0
        for i in range(len(arr)):
            diff = arr[i][0]
            p = arr[i][1]
            for j in range(cur_idx+1, diff):
                dp[j] = dp[cur_idx]
            dp[diff] = max(dp[diff-1], p)
            cur_idx = diff
        for w in worker:
            total += dp[min(w, len(dp)-1)]
        return total