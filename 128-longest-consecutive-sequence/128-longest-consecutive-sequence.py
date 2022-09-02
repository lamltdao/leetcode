class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        d = set(nums)
        ans = 0
        for n in d:
            if n-1 not in d:
                seq_len = 1
                tmp = n+1
                while tmp in d:
                    seq_len += 1
                    tmp += 1
                ans = max(ans, seq_len)
        return ans
        