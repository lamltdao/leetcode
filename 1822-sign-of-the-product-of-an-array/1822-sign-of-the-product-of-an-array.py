class Solution:
    def arraySign(self, nums: List[int]) -> int:
        prod = 1
        for n in nums:
            if n == 0:
                return 0
            prod *= n // abs(n)
        return prod