class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix = [0 for _ in nums]
        prefix[0] = nums[0]
        d = {}
        d[prefix[0] % k] = [0]
        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1] + nums[i]
            r = prefix[i] % k
            if r not in d:
                d[r] = []
            d[r].append(i)
        for k in d.keys():
            if k == 0 and d[k][-1] > 0:
                return True
            if len(d[k]) >= 2:
                if len(d[k]) == 2 and d[k][1] == d[k][0]+1:
                    continue
                return True
        return False