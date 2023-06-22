class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        """
        find longest window with at most 1 zeros
        """
        window = 0 # number of zeros
        l = 0
        ans = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                window += 1
            while l < r and window > 1:
                if nums[l] == 0:
                    window -= 1
                l += 1
            ans = max(ans, r-l+1)
        return ans
        