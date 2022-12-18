class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        dp[i]: idx of next greater
        """
        n = len(temperatures)
        dp = [-1 for _ in temperatures]
        stk = [n-1]
        for i in range(n-2, -1, -1):
            while len(stk) > 0 and temperatures[i] >= temperatures[stk[-1]]:
                stk.pop()
            if len(stk) > 0:
                dp[i] = stk[-1]
            stk.append(i)
        ans = [0 for _ in range(n)]
        for i in range(n-1):
            ans[i] = dp[i]-i if dp[i] != -1 else 0
        return ans