class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        res = 10000000
        for i in range(len(nums)):
            # target - nums[i]
            l = 0
            while l == i:
                l += 1
            r = len(nums) - 1
            while r == i:
                r -= 1
            while l < r:
                if abs(res-target) > abs(nums[l] + nums[r] + nums[i] - target):
                    res = nums[l] + nums[r] + nums[i]
                if nums[l] + nums[r] == target - nums[i]:
                    return target
                if nums[l] + nums[r] < target - nums[i]:
                    l += 1 
                    while l == i:
                        l += 1
                else:
                    r -= 1
                    while r == i:
                        r -= 1
        return res
            