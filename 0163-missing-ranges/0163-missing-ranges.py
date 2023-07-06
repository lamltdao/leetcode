class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        nums_with_bounds = [lower-1]
        nums_with_bounds.extend(nums)
        nums_with_bounds.append(upper+1)
        ans = []
        for i in range(len(nums_with_bounds)-1):
            if nums_with_bounds[i+1] > nums_with_bounds[i]+1:
                ans.append([nums_with_bounds[i]+1, nums_with_bounds[i+1]-1])
        return ans
        