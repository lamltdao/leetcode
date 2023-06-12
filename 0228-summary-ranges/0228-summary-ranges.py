class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans = []
        i = 0;
        while i < len(nums):
            j = i;
            while j+1 < len(nums) and nums[j]+1 == nums[j+1]:
                j+= 1
            if i < j :
                ans.append(f"{nums[i]}->{nums[j]}")
            else:
                ans.append(str(nums[i]))
            i = j+1
        return ans