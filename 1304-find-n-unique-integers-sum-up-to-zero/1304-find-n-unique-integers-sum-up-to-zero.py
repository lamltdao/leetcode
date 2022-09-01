class Solution:
    def sumZero(self, n: int) -> List[int]:
        """
        n is odd
        [0, 1,-1,2,-2]
        n is even
        [1,-1,2,-1]
        """
        ans = []
        if n & 1: # odd
            ans.append(0)
        cnt = 1
        while len(ans) < n:
            ans.append(cnt)
            ans.append(-cnt)
            cnt += 1
        return ans