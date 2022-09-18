class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def bt(cur_subset, cur_idx):
            if cur_idx == len(nums):
                ans.append(cur_subset[::])
                return
            bt(cur_subset, cur_idx+1)
            cur_subset.append(nums[cur_idx])
            bt(cur_subset, cur_idx+1)
            cur_subset.pop()
        bt([], 0)
        return ans