class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        """
        target: -2
        -4,-1,1,2
        """
        nums.sort()
        res = 10000000
        for i in range(len(nums)-2):
            # target - nums[i]
            # i < l < r
            l = i+1
            r = len(nums) - 1
            while l < r:
                if abs(res-target) > abs(nums[l] + nums[r] + nums[i] - target):
                    res = nums[l] + nums[r] + nums[i]
                # if nums[l] + nums[r] == target - nums[i]:
                #     return target
                if nums[l] + nums[r] < target - nums[i]:
                    l += 1 
                else:
                    r -= 1
        return res
            