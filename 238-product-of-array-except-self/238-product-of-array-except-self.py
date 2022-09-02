class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        dp_l[i]: prod [0..i-1]
        dp_r[i]: prod[i+1..end]
        """
        dp_l = [1 for _ in nums]
        dp_r = [1 for _ in nums]
        for l in range(1, len(nums)):
            dp_l[l] = dp_l[l-1] * nums[l-1]
        for r in range(len(nums)-2, -1, -1):
            dp_r[r] = dp_r[r+1] * nums[r+1]
        result = [None for _ in nums]
        for i in range(len(nums)):
            result[i] = dp_l[i] * dp_r[i]
        return result