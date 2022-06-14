class Solution:
    def findMin(self, nums: list[int]) -> int:
        """
        Note: the min element a[i] satisfies:
        a[i] < a[i+1] and a[i] < a[i-1] (if i > 0)
        """
        l = 0
        r = len(nums) - 1
        # no rotation, aka min is not at 0th position
        if nums[r] > nums[l]:
            return nums[l]
        while l < r:
            mid = (l+r) // 2
            # minimum is next to mid
            if mid+1<len(nums) and nums[mid] >= nums[mid+1]:
                return nums[mid+1]
            # mid is the minimum.
            if mid > 0 and nums[mid] <= nums[mid-1]:
                return nums[mid]
            # if left half is sorted. Note that min is not at 0th pos, thus it must be on the right half
            if nums[mid] > nums[0]:
                l = mid+1
            # if right half is sorted. We already checked above if min is mid, thus min cannot be mid when we reach to this. Therefore, it must be the case that min is on the left half
            else:
                r = mid-1
        #l == r, just return nums[l]
        return nums[l]
