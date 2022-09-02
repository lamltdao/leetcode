class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        """
        sort nums O(n log n)
        for each num at idx i:
            use two sum ii to find j,k such that j<k, j,k > i whose values sum up to -nums[i] 
        O(n^2)
        """
        nums.sort()
        for i in range(len(nums)-2):
            j = i+1
            k = len(nums)-1
            while j < k:
                if nums[j] + nums[k] == -nums[i]:
                    ans.add(tuple([nums[i], nums[j], nums[k]]))
                    j += 1
                    k -= 1
                elif nums[j] + nums[k] < -nums[i]:
                    j += 1
                else:
                    k -= 1
        return ans