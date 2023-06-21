class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        window_sum = 0
        max_window_size = 2 * k + 1
        ans = [-1 for _ in nums]
        for i, num in enumerate(nums):
            window_sum += num
            if i >= max_window_size:
                window_sum -= nums[i-max_window_size]
            if i >= max_window_size-1:      
                ans[i - k] = window_sum // max_window_size
        return ans