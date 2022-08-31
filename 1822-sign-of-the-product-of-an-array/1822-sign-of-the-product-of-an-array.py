class Solution:
    def arraySign(self, nums: List[int]) -> int:
        is_pos = True
        for n in nums:
            if n == 0:
                return 0
            is_pos = is_pos if n > 0 else not is_pos
        return 1 if is_pos else -1