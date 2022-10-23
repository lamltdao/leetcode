class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        """
        [twice, missing]
        """
        twice = None
        missing = None
        visited = [False for _ in nums]
        for n in nums:
            if visited[n-1]:
                twice = n
            visited[n-1] = True
        for i in range(len(nums)):
            if not visited[i]:
                missing = i+1
        return [twice, missing]