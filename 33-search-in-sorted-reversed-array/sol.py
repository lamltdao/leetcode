class Solution:
    def search(self, nums: list[int], target: int) -> int:
        if len(nums) == 1:
            return 0 if nums[0] == target else -1
        l = 0
        r = len(nums)-1
        while l <= r:
            mid = (l+r) // 2
            if nums[mid] == target:
                return mid
            # half left is sorted
            if nums[mid] >= nums[l]:
                if target >= nums[l] and target <= nums[mid]:
                    r = mid-1
                else:
                    l = mid+1
            # right half is sorted
            else:
                if target <= nums[r] and target >= nums[mid]:
                    l = mid+1
                else:
                    r = mid-1
        return -1
