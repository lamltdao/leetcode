# C1
class Solution1:
    def shift(self, nums, idx):
        tmp = nums[idx]
        for i in range(idx, len(nums)-1):
            nums[i] = nums[i+1]
        nums[-1] = tmp
    def removeDuplicates(self, nums: List[int]) -> int:
        # first iterate through array from right to find number of redundant elements
        num_redundant = 0
        for i in range(len(nums)-1,1,-1):
            if nums[i] == nums[i-1] and nums[i] == nums[i-2]:
                num_redundant += 1
                self.shift(nums,i)
        return len(nums) - num_redundant
# C2
class Solution2:
    def removeDuplicates(self, nums: list[int]) -> int:
        # first iterate through array from right to find number of redundant elements
        num_redundant = 0
        NMAX = 10**5
        for i in range(len(nums)-1,1,-1):
            if nums[i] == nums[i-1] and nums[i] == nums[i-2]:
                num_redundant += 1
                nums[i] = NMAX
        index = 0
        junk = 1
        count = len(nums)
        for index in range(len(nums)):
            if nums[index] == NMAX:
                nextInd = index + junk
                while nextInd < count and nums[nextInd] == NMAX:
                    nextInd += 1
                if nextInd == count: 
                    break
                junk = nextInd - index
                nums[index],nums[nextInd] = nums[nextInd],nums[index]
        return len(nums) - num_redundant
