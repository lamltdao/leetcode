class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        window_sum = 0
        l = 0
        MAX = len(nums)+1
        ans = MAX
        for r in range(len(nums)):
            window_sum += nums[r]
            while l < r and window_sum - nums[l] >= target:
                window_sum -= nums[l]
                l += 1
            if window_sum >= target:
                ans = min(ans, r-l+1)
        return ans if ans < MAX else 0
            