class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs[0])
        num_str = len(strs)
        ans = 0
        for i in range(n):
            for j in range(num_str-1):
                if strs[j][i] > strs[j+1][i]:
                    ans += 1
                    break
        return ans