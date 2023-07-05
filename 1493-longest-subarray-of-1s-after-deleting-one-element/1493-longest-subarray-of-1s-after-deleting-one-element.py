class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        ans = 0
        cur_num_one = 0
        last_num_one = 0
        has_zero = False
        for i,n in enumerate(nums):
            if n == 1:
                cur_num_one += 1
                ans = max(ans, cur_num_one + last_num_one)
            else:
                has_zero = True
                last_num_one = cur_num_one
                cur_num_one = 0
        if not has_zero: # edge: no zeros. Have to delete one '1'
            return len(nums)-1
        return ans