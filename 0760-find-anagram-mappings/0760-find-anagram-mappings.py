class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = {}
        n = len(nums1)
        ans = [-1 for _ in range(n)]
        for i,num in enumerate(nums2):
            if num not in d:
                d[num] = []
            d[num].append(i)
        for i,num in enumerate(nums1):
            ans[i] = d[num][-1]
            d[num].pop()
        return ans
            
        